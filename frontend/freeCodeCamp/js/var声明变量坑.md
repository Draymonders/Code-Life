In JavaScript, scope refers to the visibility of variables. Variables which are defined outside of a function block have Global scope. This means, they can be seen everywhere in your JavaScript code.

Variables which are used without the var keyword are automatically created in the global scope. This can create unintended consequences elsewhere in your code or when running a function again. You should always declare your variables with var.

Variables which are declared within a function, as well as the function parameters have local scope. That means, they are only visible within that function.


翻译一下就是 
- 在函数外声明的var变量是`global`的, 在函数内生命的var变量是`local`
- 如果变量不用`var`声明，那么则是`global`，但是不建议