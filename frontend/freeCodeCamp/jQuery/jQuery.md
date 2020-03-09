# jQuery
## $(document).ready(function() {})
title中的 `$(document).ready(function() {})`的意思是 等浏览器，文档加载完毕后再执行函数

## addClass
添加`class`属性

## removeClass
删除`class`属性

## by
可以`by type`, 也可以`by class`, 也可以`by id`

```js
$("button")
$(".class")
$("#id")
```

## css
改变css样式
```js
$("#target1").css("color", "red");
```

## prop
改变属性
```js
$("#target1").prop("disabled", true)
```

## remove
删除元素

## appendTo
**移动元素** 注意是移动元素，如果元素a在A处，使用了`$("#a").appendTo("#B")`, 那么**A处的a将会移动到B处**

## clone
拷贝元素

## parent
寻找父级元素

## children
所有的子级元素

## 指定第几个子级元素
注意是`:nth-child`, 计数从1开始的
```js
$(".target:nth-child(2)").addClass("animated bounce");
```

## 指定所有的奇数/偶数的子级元素 
```js
$(".target:odd").addClass("colorRed")
$(".target:even").addClass("colorBlue")
```

## 整个页面
`$("body")`