## Reduce方法
The callback function accepts four arguments. The first argument is known as the accumulator, which gets assigned the return value of the callback function from the previous iteration, the second is the current element being processed, the third is the index of that element and the fourth is the array upon which reduce is called.

大概是 reduce的回调函数有四个参数 (accumulator, item, index, arrayCalledReduce)   (index从0开始计数)

然后reduce的第二个参数是初始值

简单的demo
```js
const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const sumOfAges = users.reduce((sum, user) => sum + user.age, 0);
console.log(sumOfAges); // 64
```