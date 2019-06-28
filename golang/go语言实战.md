## append
函数`append`会智能地处理底层数组的容量增长。在切片的容量小于1000个元素时，总是会成倍地增加容量。一旦元素个数超过1000，容量的增长因子就会设为1.25，
也就是每次增加`25%`的容量，随着语言的演化，这种增长算法可能会有所改变。

### 测试代码 & 结果
```go
func main() {
	l1 := []int{0: 1}
	k := 1
    last := 0
	for k < 2000 {
		l1 = append(l1, k)
		k++
		if cap(l1) != last {
			fmt.Println(k, cap(l1))
			last = cap(l1)
		}
	}
}
```
![结果.png](https://s2.ax1x.com/2019/06/28/ZKimmq.md.png)

## 切片传到函数里面是传引用
代码测试
```
func foo(list []int) {
	for i := 0; i < len(list); i++ {
		list[i] = 10 + i
	}
	return
}
func main() {
	list := []int{0, 1, 2}
	foo(list)
	fmt.Printf("%v", list)
}

// 结果
[10, 11, 12]
```
## 切片和指针
在`64位`架构的机器上，一个切片需要`24字节`的内存，指针字段需要`8字节`，长度和容量各需要`8字节`。

## 方法集
---
Values | Methods Receivers<br>
---
T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|(t T)<br>
--- 
*T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| (t T) and (t *T)<br>
---
指向`T类型的值的`方法集只包含`值接收者`声明的方法。
指向`T类型的指针`的方法集包含`值接收者`声明和`指针接收者`声明的方法。

## 并发
`go`语言运行时默认会为每个可用的物理处理器分配一个`逻辑处理器`。
如果创建一个`goroutine`并准备运行，这个`goroutine`就会被到调度器的全局运行队列中。之后，调度器就将这些队列中的`goroutine`分配给一个逻辑处理器，并放到这个逻辑处理器对应的本地运行队列中。

**逻辑处理器**

**本地运行队列**

**调度器**

使用`go build -race`竞争检测器标志来编译程序
运行程序`./go_start.exe` 出现警告。

可以使用`atomic`和`sync`包下的方法或函数保证线程安全

```go
unbuffered := make(chan int)
buffered := make(chan string, 10)
```
第一个是无缓冲的通道，第二是有缓冲的通道

任务执行，需要考虑的情况:
1. 系统中断 
2. 完成情况(完成 or 失败)
3. 超时

### runner
runner自带超时与中断功能
```
type Runner struct {
	interrupt chan os.Signal

	complete chan error

	timeout <-chan time.Time

	tasks []func(int)
}

var ErrTimeOut = errors.New("received timeout")
var ErrInterrupt = errors.New("received interrupt")

// new a Runner
func New(d time.Duration) *Runner {
	return &Runner{
		interrupt: make(chan os.Signal, 1),
		complete:  make(chan error),
		timeout:   time.After(d),
	}
}

func (r *Runner) Add(tasks ...func(int)) {
	r.tasks = append(r.tasks, tasks...)
}

func (r *Runner) Start() error {
	signal.Notify(r.interrupt, os.Interrupt)

	go func() {
		r.complete <- r.run()
	}()

	select {
	case err := <-r.complete:
		return err
	case <-r.timeout:
		return ErrTimeOut
	}
}

func (r *Runner) run() error {
	for id, task := range r.tasks {
		if r.gotInterrupt() {
			return ErrInterrupt
		}
		task(id)
	}
	return nil
}

func (r *Runner) gotInterrupt() bool {
	select {
	case <-r.interrupt:
		signal.Stop(r.interrupt)
		return true
	default:
		return false
	}
}
```

### pool
资源管理池
```
package pool

import (
	"errors"
	"io"
	"log"
	"sync"
)

type Pool struct {
	m         sync.Mutex
	resources chan io.Closer
	factory   func() (io.Closer, error)
	closed    bool
}

var ErrPoolClosed = errors.New("Pool has been closed")

func New(fn func() (io.Closer, error), size uint) (*Pool, error) {
	if size <= 0 {
		return nil, errors.New("size value too small")
	}
	return &Pool{
		factory:   fn,
		resources: make(chan io.Closer, size),
	}, nil
}

// get a resource
func (p *Pool) Acquire() (io.Closer, error) {
	select {
	case r, ok := <-p.resources:
		log.Println("Acquire:", "shared Resource")
		if !ok {
			return nil, ErrPoolClosed
		}
		return r, nil
	default:
		log.Println("Acquire:", "New Resource")
		return p.factory()
	}
}

// release to reasoure
func (p *Pool) Release(r io.Closer) {
	p.m.Lock()
	defer p.m.Unlock()

	if p.closed {
		r.Close()
		return
	}

	select {
	case p.resources <- r:
		log.Println("Release:", "In queue")
	default:
		log.Println("Release:", "Closing")
		r.Close()
	}
}

// Close
func (p *Pool) Close() {
	p.m.Lock()
	defer p.m.Unlock()
	if p.closed {
		return
	}
	p.closed = true
	close(p.resources)

	for r := range p.resources {
		r.Close()
	}
	return
}
```