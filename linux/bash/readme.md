# bash 基础
## 变量
Bash does not have a type system,  `it can only save string values`.
```shell
NAME=Draymonder
AGE=20

echo $NAME $AGE
```

## read & echo
```shell
echo -n "Enter a name:"
read NAME
echo "Your name is:" $NAME

=> Enter a name: ⥢ Draymonder
=> Your name is: Draymonder
```

## 命令执行
`$(command)` expression will execute the command and returns the output of the command
```shell
PWD=$(pwd)
BASH_VERSION=`bash --version`
echo $PWD
echo $BASH_VERSION
```

## 字符串插值
只有双引号支持字符串插值， 单引号不可以
```shell
FIRST_NAME='JOHN'
echo "Hello ${FIRST_NAME}!;"
echo 'Hello ${FIRST_NAME}!;'
=> Hello JOHN!;
=> Hello ${FIRST_NAME}!;
```

## 数学运算
有三种方法`let`, `expr`, `$(())`
```shell
let RESULT=1+1
echo $RESULT
=> 2

expr 1 + 1   # prints to the STDOUT
RESULT=$(expr 3 \* 3)
echo $RESULT
=> 2
=> 9

RESULT=$((1 + 1))
echo $RESULT
=> 2
```

## 逻辑运算
`test`和`[ expression ]`效果是一样的
```shell
(test 5 -gt 9)
echo $?

[ 9 -gt 5 ] 
echo $?  

=> 1 (表示错误)
=> 0 (表示正确)
```
### if/else
```shell
if [ conditional expression ]
then
    # if code here
else
    # else code here
fi
```

### 生成list
```shell
echo {0..10} # step: 1
echo $(seq 0 10) # step: 1
echo $(seq 0 2 10) # step: 2
echo $(seq 10 -2 4) # step: -2
=> 0 1 2 3 4 5 6 7 8 9 10
=> 0 1 2 3 4 5 6 7 8 9 10
=> 0 2 4 6 8 10
=> 10 8 6 4
```

## for循环
```shell
for iterator
do
    # perform action per iteration
done

for (( i=n; i<N; n++ ))
do
    # perform action per iteration
done
```

## 函数function
```shell
function show_fruits(){
    echo "Local Args: \$1:$1 | \$2:$2"
}
show_fruits Apple Oranges
echo "Global Args: \$1:$1 | \$2:$2"

------

~$ bash fruits.sh
=> Local Args: $1:Apple | $2:Oranges
=> Global Args: $1:Mangos | $2:Grapes
```

## 数组array
we use `${#VAR}` to calculate the length of a variable `VAR`.

Likewise, using `*` as an `index` in the syntax`${#ARRAY[index]}`, we can calculate the length of an array.

```shell
arr=("1", "22", "333")
arr[3]="444"
echo "arr长度 "${#arr[*]}
echo ${arr[*]}
```

### 单个元素存在空格的情况
最佳选择 `"${arr[@]}"`, 别忘记了引号`""`

```shell
arr=("a bb", "ccc dddd")
echo ${#arr[*]}
for ele in ${arr[*]}; do
  echo "ele: " $ele
done


echo ${#arr[@]}
for ele in "${arr[@]}"; do
  echo "ele: " $ele
done

=> 2
=> ele:  a
=> ele:  bb,
=> ele:  ccc
=> ele:  dddd
=> 2
=> ele:  a bb,
=> ele:  ccc dddd
```

## 特殊字符
<script src="https://gist.github.com/thatisuday/10b6c065fd9c98d7fff74127fb356364.js"></script>