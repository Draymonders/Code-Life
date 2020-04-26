# JSX
JSX就是在javascript里面写html代码，省去了操作dom的复杂操作

## 注释
使用如下的注释 `{/* */}`， 记住是有花括号的 **{}**

## render
```js
ReactDOM.render(compentToRender, elementOnDOM)
```

## className
由于JSX和html一样，但是JSX是在js中，js已经有了关键字`class`, 因此使用`className`来替代 html中的`class`

In fact, the naming convention for all HTML attributes and event references in JSX become camelCase. For example, a click event in JSX is `onClick`, instead of `onclick`. Likewise, onchange becomes `onChange`. While this is a subtle difference, it is an important one to keep in mind moving forward.


## 组件
A stateless functional component is any function you write which accepts props and returns JSX. A stateless component, on the other hand, is a class that extends `React.Component`, but does not use internal state (covered in the next challenge). Finally, a stateful component is a class component that does maintain its own internal state. You may see stateful components referred to simply as components or React components.
### 方式一
```js
const MyComponent = function() {
  return (
    <div>component</div>
  );
}
```

### 方式二
推荐如下方式
```js
class MyComponent extends React.Componenet {
    render() {
        return (
            <div></div>
        )
    }
}
```

## 传递props
```js
const CurrentDate = (props) => {
  return (
    <div>
      <p>The current date is: {props.date}</p>
    </div>
  );
};

class Calendar extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>What date is it?</h3>
        <CurrentDate date={Date()}/>
      </div>
    );
  }
};
```

### 指定默认的props
```js
MyComponent.defaultProps = {
    items: 0
}
```

### props类型检查
注意： js的7个数据类型里面 `function` 被写为了`func`, `boolean` 被写为了`bool`

```js
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
};

Items.propTypes = {
  quantity: PropTypes.number.isRequired
}
```

## state
Note that if you make a component stateful, no other components are aware of its `state`. Its `state` is completely encapsulated, or local to that component, unless you pass state data to a child component as `props`. This notion of encapsulated `state` is very important because it allows you to write certain logic, then have that logic contained and isolated in one place in your code.
### 创建state
```js
class StatefulComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        name: "draymonder"
    }
  }
  render() {
    return (
      <div>
        <h1>{this.state.name}</h1>
      </div>
    );
  }
};
```
### 更新state
```js
this.setState({})
```

#### 需要之前状态的时候的更新state
```js
this.setState((state, props) => {
    cnt: state.cnt + props.cnt
})
```


## 子组件更新父组件的状态
通产数据流是单向的， 即父组件向子组件传数据，如何子组件改变父组件的状态呢， 通过**回调**

以下例子有三个`component`

分别是`MyApp`, `GetInput`, `RenderInput`

`MyApp`向`GetInput` 传送了初始的数据和改变后的回调

另外 `MyApp`向`RenderInput` 传送了数据

这样在`GetInput`改变了数据后，通过调用`onChange`绑定的方法，即`MyApp`的`handleChange`会改变`inputValue`的值，因此也会改变`RenderInput`渲染出来的`input`

```js
class MyApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inputValue: ''
    }
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({
      inputValue: event.target.value
    });
  }
  render() {
    return (
       <div>
        <GetInput input={this.state.inputValue} handleChange={this.handleChange} />
        <RenderInput input={this.state.inputValue}/>
       </div>
    );
  }
};

class GetInput extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>Get Input:</h3>
        <input
          value={this.props.input}
          onChange={this.props.handleChange}/>
      </div>
    );
  }
};

class RenderInput extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>Input Render:</h3>
        <p>{this.props.input}</p>
      </div>
    );
  }
};
```

## 生命周期函数
### shouldComponentUpdate
判断是否因为新的props, state而更新UI
```js
shouldComponentUpdate(nextProps, nextState)
```

## jsx渲染style
```js
/*
使用原生html
<div style="fontsize:72px; color: 'red';">Big Red</div>
*/
/*
使用JSX
为什么使用两个大花括号呢？  
其实很简单 外层的花括号是表示使用js code
内层的花括号是js的object表示(map表示)
*/
<div style={{fontSize: 72, color: "red"}}>Big Red
</div>
```

## redux异步样例
```js
const REQUESTING_DATA = 'REQUESTING_DATA'
const RECEIVED_DATA = 'RECEIVED_DATA'

const requestingData = () => { return {type: REQUESTING_DATA} }
const receivedData = (data) => { return {type: RECEIVED_DATA, users: data.users} }

const handleAsync = () => {
  return function(dispatch) {
    // dispatch request action here
    store.dispatch(requestingData())
    setTimeout(function() {
      let data = {
        users: ['Jeff', 'William', 'Alice']
      }
      // dispatch received data action here
      store.dispatch(receivedData(data))
    }, 2500);
  }
};

const defaultState = {
  fetching: false,
  users: []
};

const asyncDataReducer = (state = defaultState, action) => {
  switch(action.type) {
    case REQUESTING_DATA:
      return {
        fetching: true,
        users: []
      }
    case RECEIVED_DATA:
      return {
        fetching: false,
        users: action.users
      }
    default:
      return state;
  }
};

const store = Redux.createStore(
  asyncDataReducer,
  Redux.applyMiddleware(ReduxThunk.default)
);
```