`js` 不像 `c` 那样认为`ascii`码和数字等价

```
"a" => 97
"a".charCodeAt(0)  => 97

97 => "a"
String.fromCharCode(97)
```