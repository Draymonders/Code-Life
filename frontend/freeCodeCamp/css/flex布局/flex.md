# `flex`布局
css声明
```
display: flex
```

## flex-direction
有两个value
- col  按行去排列
- column 按列去排列


## justify-content
<img src="https://www.w3.org/TR/css-flexbox-1/images/flex-direction-terms.svg">

常用的value有
- center
- `flex-start`: aligns items to the start of the flex container. For a row, this pushes the items to the left of the container. For a column, this pushes the items to the top of the container. This is the default alignment if no justify-content is specified.
- `flex-end`: aligns items to the end of the flex container. For a row, this pushes the items to the right of the container. For a column, this pushes the items to the bottom of the container.
- `space-between`: aligns items to the center of the main axis, with extra space placed between the items. The first and last items are pushed to the very edge of the flex container. For example, in a row the first item is against the left side of the container, the last item is against the right side of the container, then the remaining space is distributed evenly among the other items.
- `space-around`: similar to space-between but the first and last items are not locked to the edges of the container, the space is distributed around all the items with a half space on either end of the flex container.
- `space-evenly`: Distributes space evenly between the flex items with a full space at either end of the flex container

## align-items
如果是行排列的，控制的垂直方向 
如果是列排列的，控制的水平方向

## flew-wrap
比如当前有3个`width: 50%`的div, 如果是`no-wrap`的话，三个div还是在一行的，如果使用`wrap`的话 就会排列成 `一行半`
- no-wrap
- wrap
- wrap-reverse
