同类选择器如果同时出现在某个元素上, 那么决定最终效果的是`css <style></style>`里面同类选择器的后面一部分

跟以下声明顺序无关
```
<div class="class1 class2"> </div>
```

We just proved that browsers read CSS from top to bottom in order of their declaration. That means that, in the event of a conflict, the browser will use whichever CSS declaration came last. 
## css选择器顺序
> !important > 内联 > id选择器 > class选择器

- 示例
最终颜色为粉红色
```html
<style>
  #orange-text {
    color: orange;
  }
  .pink-text {
    color: pink !important;
  }
  .blue-text {
    color: blue;
  }
</style>
<h1 id="orange-text" class="pink-text blue-text" style="color: white">Hello World!</h1>
```