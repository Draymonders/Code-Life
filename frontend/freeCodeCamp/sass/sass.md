# sass
sass是什么呢？ 就是一种css的拓展，目的是什么呢？
场景是 页面上很多元素用到了一个color,但是由于不可控的因素，要改变color, 不能每次都用全局替换，太麻烦了

因此，我们需要一种带有变量的css，这样可以定义一个局部变量
每次只需要改变量就可以了

## 语法
变量由 `$`加上`name`构成
```html
$colorRed : red;

h1 {
    color: $colorRed;
}
```

## 可嵌套
For example
```css
nav {
  background-color: red;

  ul {
    list-style: none;

    li {
      display: inline-block;
    }
  }
}
```

## mixin
在Sass中，mixin是一组可以在整个样式表中重用的CSS声明。

较新的CSS特性在完全被采用并准备在所有浏览器中使用之前需要一段时间。随着特性被添加到浏览器中，使用它们的CSS规则可能需要厂商的前缀。

例子有如下
```html
<style type='text/sass'>

  @mixin border-radius($a) {
    -webkit-border-radius: $a;
    -moz-border-radius: $a;
    -ms-border-radius: $a;
    border-radius: $a;
  } 

  #awesome {
    @include border-radius(15px);
  }
</style>
```

## if / else
配合 mixin使用
```html
<style type='text/sass'>
  @mixin border-stroke($val) {
    @if $val == light {
      border: 1px solid black;
    }
    @else if $val == medium {
      border: 3px solid black;
    }
    @else if $val == heavy {
      border: 6px solid black;
    }
    @else {
      border: none;
    }
  }

  #box {
    width: 150px;
    height: 150px;
    background-color: red;
    @include border-stroke(medium);
  }
</style>

<div id="box"></div>
```

## for
```css
注意`from through` 和 `from to`的区别
<style type='text/sass'>
  @for $j from 1 through 5 {
    .text-#{$j} { font-size: 10px * $j; }
  }
  
  
</style>

<p class="text-1">Hello</p>
<p class="text-2">Hello</p>
<p class="text-3">Hello</p>
<p class="text-4">Hello</p>
<p class="text-5">Hello</p>
```

## each
遍历list or map
```html
<style type='text/sass'>

  @each $color in blue, black, red {
    .#{$color}-bg {
      background: $color;
    } 
  }

  div {
    height: 200px;
    width: 200px;
  }
</style>

<div class="blue-bg"></div>
<div class="black-bg"></div>
<div class="red-bg"></div>
```

## while 
```html
<style type="text/sass">
    $i: 1;

    $while $i < 10 {
        font-#{$i} {
            font-size: 10px * (10 - $i);
        };
        $i: $i+1;
    }
</style>
```

## extend
[参考教程](https://www.freecodecamp.org/learn/front-end-libraries/sass/extend-one-set-of-css-styles-to-another-element)

可以复用css, 但感觉用处不大
for example
```html
<style type='text/sass'>
  h3{
    text-align: center;
  }
  .info{
    width: 200px;
    border: 1px solid black;
    margin: 0 auto;
  }

 
  .info-important{
    @extend .info;
    background-color: magenta;
  }

</style>
<h3>Posts</h3>
<div class="info-important">
  <p>This is an important post. It should extend the class ".info" and have its own CSS styles.</p>
</div>

<div class="info">
  <p>This is a simple post. It has basic styling and can be extended for other uses.</p>
</div>
```
