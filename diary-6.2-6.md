# 面经

## HTML+CSS

### 1、块级元素和行内元素有哪些？两者区别是什么？

所有的容器级标签以及p标签都是**块级元素**：p、div、h、ul、li、dt、dd、form、address、menu、table

除了p之外所有的文本级标签都是**行内元素**。span、a（锚点）、strong、em（强调）、br（换行）、img、input、label、select、textarea、cite

**区别**：

* 块级元素会独占一行，其宽度自动填满父元素宽度；行内元素不会独占一行，相邻的行元素会排列在同一行里，一行排不下才会换行，其宽度随元素内容而变化；
* 块级元素可以设置width和height属性，行内元素设置width、height无效；
* 块级元素可以设置margin和padding，当行内元素设置时只有水平方向有效，竖直方向无效；



*参考*：

https://www.cnblogs.com/greenal/archive/2013/01/05/2845513.html

https://www.cnblogs.com/stfei/p/9084915.html



### 2、两个div元素如何在一行排列？

HTML：

```html
<div class="box1">block1</div>
<div class="box2">block2</div>
<div class="box3">block3</div>
```

* **设置浮动**

  所有的标签一旦设置浮动，就能够并排且不区分块元素或行内元素。换言之，行内元素也能设置宽高了。

  ```css
  .box1 {
      width: 200px;
      height: 200px;
      background-color: yellow;
      float: left;
  }
  .box2 {
      width: 200px;
      height: 200px;
      background-color: red;
      float: left;
  }
  .box3 {
      width: 200px;
      height: 200px;
      background-color: blue;
      float: left;
  }
  ```

  关于浮动遵循的原则：永远不是一个盒子在浮动，要浮动就一起浮动。另外，有浮动一定要清除浮动。

  清除浮动的方法：

  * 给父盒子设置高度：使用不灵活，会固定父盒子的高度
  * clear: both;
  * 伪元素清除法
  * overflow: hidden;

* **设置display: inline;**

  但是这样有一个缺点，就是没办法设置每个元素的宽高，就是按字排列，并且中间会有一个空。如图：

  ![image-20210603102150221](https://i.loli.net/2021/06/03/oAJMjYBGxC6374U.png)

* **设置display: inline-block;**

  这个时候可以设置宽高，但是每个元素中间还是会有个空格，如图：

  ![image-20210603102847584](https://i.loli.net/2021/06/03/F2YmXjcCJhNGuQB.png)

  这个空格是可以清除的，具体看：https://blog.csdn.net/qiphon3650/article/details/75733328

* **设置display: table-cell**

  这个时候得改一下HTML，在外层包裹一个元素，设置class为wrap。在wrap中设置`display: table`，其余每个box中设置`display: table-cell`。

* **绝对定位**

  CSS代码为：

  ```CSS
  .wrap {
      position: relative;
  }
  .box1 {
      width: 200px;
      height: 200px;
      background-color: yellow;
      position: absolute;
      left: 0;
      top: 0;
  }
  .box2 {
      width: 200px;
      height: 200px;
      background-color: red;
      position: absolute;
      transform: translate(100%, 0);
  }
  .box3 {
      width: 200px;
      height: 200px;
      background-color: blue;
      position: absolute;
      transform: translate(200%, 0);
  }
  ```

  其中，translate填的是百分数的话，会以它本身的宽高作为参照。

* **flex布局**

  ```css
  .wrap {
      display: flex;
  }
  .box1 {
      width: 200px;
      height: 200px;
      background-color: yellow;
      flex: 1;
  }
  .box2 {
      width: 200px;
      height: 200px;
      background-color: red;
      flex: 1;
  }
  .box3 {
      width: 200px;
      height: 200px;
      background-color: blue;
      flex: 1;
  }
  ```

  可以得到下面的结果，即它总是三等分浏览器视区：

  ![image-20210603140709850](https://i.loli.net/2021/06/03/FtJiXlbzSRx8Z72.png)



# 一些学习记录

## Sass、Scss、LESS和Stylus区别

* **什么是CSS预处理器**

  CSS 预处理器是一种语言用来为 CSS 增加一些编程的特性，无需考虑浏览器的兼容性问题。例如可以在 CSS 中使用变量、简单的程序逻辑、函数等等在编程语言中的一些基本技巧，可以让CSS 更见简洁，适应性更强，代码更直观等诸多好处。

* **变量**
  * Sass：变量必须以$开头，变量和值之间使用冒号隔开
  * LESS：变量以@开头，已经被赋值的变量以及其他的常量（如像素、颜色等）都可以参与运算
  * Stylus：对变量没有设定，可以以$开头（但不能用@开头），或者其他的任何字符。

* **颜色函数**

  * Sass：lighten、darken、saturate、desaturate、grayscale、complement、invert、mix
  * LESS：lighten、darken、saturate、desaturate、spin、mix
  * Stylus：lighten、darken、saturate、desaturate

* **继承**

  * Sass：通过@extend来实现代码组合声明
  * Less：采用类似混入的写法

* **Minxins（混入）**

  Minxins有点像是函数或者是宏，当某段 CSS 经常需要在多个元素中使用时，可以为这些共用的 CSS 定义一个 Mixin，然后只需要在需要引用这些 CSS 地方调用该 Mixin 即可。



*参考*：

https://blog.csdn.net/qq_35430000/article/details/87097696



## Vue混入

混入 (mixin) 提供了一种非常灵活的方式，来分发 Vue 组件中的可复用功能。一个混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被“混合”进入该组件本身的选项。

* **选项合并**：当组件和混入对象含有同名选项时，选项将以恰当的方式进行合并。在发生冲突时，以组件数据优先。同名钩子函数将合并为一个数组，因此都将被调用，且混入对象的钩子在组件自身钩子之前调用。

* **全局混入**：一旦使用全局混入，它将影响每一个时候创建的Vue实例。

  ```javascript
  // 为自定义的选项 'myOption' 注入一个处理器。
  Vue.mixin({
    created: function () {
      var myOption = this.$options.myOption
      if (myOption) {
        console.log(myOption)
      }
    }
  })
  
  new Vue({
    myOption: 'hello!'
  })
  // => "hello!"
  ```

  

## Element UI中对Form表单验证的使用

* Form 组件提供了表单验证的功能，只需要通过 rules 属性传入约定的验证规则，并将 Form-Item的 prop 属性设置为需校验的字段名即可。

*参考*：https://www.cnblogs.com/xyyt/p/13366812.html



## Vuex

每一个 Vuex 应用的核心就是 store（仓库）。“store”基本上就是一个容器，它包含着你的应用中大部分的**状态 (state)**。Vuex和单纯的全局对象有以下两点不同

* **最简单的Store**

  ```javascript
  import Vue from 'vue'
  import Vuex from 'vuex'
  
  Vue.use(Vuex)
  
  const store = new Vuex.Store({
      state: {
          count: 0
      },
      mutations: {
          increment (state) {
              state.count ++;
          }
      }
  })
  ```

  之后通过`store.state`来获取状态对象，以及通过`store.commit`方法触发状态变更：

  ```javascript
  store.commit('increment')
  console.log(store.state.count)
  ```

  为了在Vue组件中访问`this.$store`property，需要为Vue实例提供创建好的store（以选项的方式“注入”）。之后可以从组件的方法提交一个变更：

  ```javascript
  methods: {
      increment() {
          this.$store.commit('increment')
          console.log(this.$store.state.count)
      }
  }
  ```

  通过提交mutation的方式而非直接改变`store.state.count`，可以更明确地追踪到状态的变化。

* **State**

  Vuex 使用**单一状态树**——用一个对象就包含了全部的应用层级状态。至此它便作为一个“唯一数据源”而存在。这也意味着，每个应用将仅仅包含一个 store 实例。单一状态树让我们能够直接地定位任一特定的状态片段，在调试的过程中也能轻易地取得整个当前应用状态的快照。

  当一个组件需要获取多个状态的时候，可以使用`mapState`辅助函数帮助生成计算属性。

  ```javascript
  import { mapState } from 'vuex'
  
  export default {
      computed: mapState({
          count: state => state.count,
          // 传字符串参数'count'等同于'state=>state.count'
          coutAlias: 'count',
          // 为了能够使用'this'获取局部状态，必须使用常规函数
          countPluseLocalState (state) {
              return state.count + this.localCount
          }
      })
  }
  ```

  `mapState`函数返回的是一个对象，通常需要使用一个工具函数将多个对象合并为一个，以使我们可以将最终对象传给computed属性。采用**对象展开运算符**时：

  ```javascript
  computed: {
  	localComputed () {/*...*/}
      // 使用对象展开运算符将此对象混入到外部对象中
      ...mapState({
          // ...
      })
  }
  ```

  

* **Getter**

  Vuex 允许我们在 store 中定义“getter”（可以认为是 store 的计算属性）。就像计算属性一样，getter 的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算。

  ```javascript
  const store = new Vuex.Store({
      state: {
          todos: [
              { id: 1, text: '...', done: true},
              { id: 2, text: '...', done: false}
          ]
      },
      getters: {
          doneTodos: state => {
              return state.todos.filter(todo => todo.done)
          }
      }
  })
  ```

  Getter会暴露为`store.getters`对象，可以**以属性的形式访问**这些值：

  `store.getters.doneTodos // -> [{ id: 1, text: '...', done: true}]`

  Getter也可以接受其他getter作为第二个参数：

  ```javascript
  getters: {
      // ...
      doneTodosCount: (state, getters) => {
          return getters.doneTods.length
      }
  }
  ```

  Getter在通过属性访问时时作为Vue的响应式系统的一部分缓存其中的。

  **通过方法访问**：通过让getter返回一个函数，来实现给getter传参。但getter在通过访问时，每次都会进行调用，不会缓存结果。

  ```javascript
  getters: {
  	// ...
      getTodoById: (state) => (id) => {
          return state.todos.find(todo => todo.id === id)
      }
  }
  store.getters.getTodoById(2) // -> { id: 2, text: '...', done: false }
  ```

  **mapGetters辅助函数**

  `mapGetters`辅助函数仅仅是将store中的getter映射到局部计算属性：

  ```javascript
  import { mapGetters } from 'vuex'
  export default {
      // ...
      computed: {
          ...mapGetters([
              'doneTodosCount',
              'anotherGetter',
              // 把`this.doneCount`映射为`this.$store.getters.doneTodosCount`的方式
              // doneCount: 'doneTodosCount'
          ])
      }
  }
  ```

  
