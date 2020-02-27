# grid布局
## grid-template-columns
后面可以跟多个参数， 每个参数为列宽

## grid-template-rows
后面可以跟多个参数， 每个参数为行高

### 参数 fr,auto,%
```
fr: sets the column or row to a fraction of the available space,

auto: sets the column or row to the width or height of its content automatically,

%: adjusts the column or row to the percent width of its container.
```

## 列间隙 grid-column-gap
列之间空留的地方

## 行间隙 grid-row-gap
行之间空留的地方

## 行列间隙 grid-gap
先行后列

## grid-column
如果 `grid-template-columns` 设定了3列，那么 就会有 四条竖线
grid-column的属性设置为 `start / end`

## grid-row
同`grid-column`一样 是 `start / end`

## justify-self
控制列
In CSS Grid, the content of each item is located in a box which is referred to as a cell. You can align the content's position within its cell horizontally using the `justify-self` property on a grid item. By default, this property has a value of `stretch`, which will make the content fill the whole width of the cell. This CSS Grid property accepts other values as well:

- `start`: aligns the content at the left of the cell,

- `center`: aligns the content in the center of the cell,

- `end`: aligns the content at the right of the cell.
### justify-items
控制容器内所有item列都...

## align-self
控制行
### align-items
控制容器内所有item行都..

## area
提供了一个容器属性`grid-template-areas`

example:
```css
grid-template-areas:
    "header header header"
    "advert content content"
    "footer footer footer";
```

然后item声明 
```css
grid-area: header;
```
