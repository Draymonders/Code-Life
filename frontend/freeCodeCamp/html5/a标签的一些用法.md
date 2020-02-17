- `a`标签不仅可以跳转外部链接，也可以跳转内部链接

```
<a href="#test">Contacts</a>
...
<h2 id="test">Contacts</h2>
```

- Remove the target="_blank" attribute from the anchor tag since this causes the linked document to open in a new window tab.

- 经试验， 换成`class`不可行