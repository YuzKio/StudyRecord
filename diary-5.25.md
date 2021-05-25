- [ 面经](#head1)
	- [ JavaScript](#head2)
		- [ 1、ES6新特性（一）](#head3)
		- [ 2、Map与普通Object的区别？](#head4)
		- [ 3、Symbol数据类型](#head5)
		- [ 4、JS原型链是如何连接的？原型链的产生？](#head6)
		- [ 5、事件循环？宏任务微任务执行完之后会做什么？](#head7)
	- [ 网络基础](#head8)
		- [ 1、TCP三次握手四次挥手](#head9)
		- [ 2、状态码](#head10)
- [ 前端学院](#head11)
	- [ 做一个在线简历（HTML篇）](#head12)
	- [Some Simple Question](#head13)
# <span id="head1"> 面经</span>

## <span id="head2"> JavaScript</span>

### <span id="head3"> 1、ES6新特性（一）</span>

这部分内容比较多，所以还是分开每天一小部分来学习好啦。

* **作用域**

  * 块级作用域
  * 块级变量let
  * 块级常量const

* **箭头函数**

  * `sum = (a, b) => a + b`
  * `nums.forEach( v => {console.log(v) })`
  * 词法this*（this的部分分开）*

* **参数处理**

  * 默认参数值
  
    允许在没有值或undefined被传入时使用默认形参。
  
    调用时解析。每次函数调用时都会创建一个新的参数对象。
  
    ```javascript
    function append(value, array = []) {
    array.push(value);
    return array;
    }
    
    append(1); //[1]
    append(2); //[2], not [1, 2]
    ```
  
  * 剩余参数
  
    允许将一个不定数量的参数表示为一个数组。arguments对象还有一些附加的属性（如callee属性）。
  
    **剩余参数和arguments对象之间的区别：**
  
    * 剩余参数只包含哪些没有对应形参的实参，而arguments对象包含了传给函数的所有实参。
    * arguments对象不是一个真正的数组，而剩余参数是真正的Array实例。
  
  ​	应该是因为剩余参数是真正的Array实例，故其可以用于箭头函数；而argument作为类数组对象不行。*（是和箭头函数不绑定this有关？还得再研究一下）*
  
  ​	实验结果：
  
  ```javascript
  var sum1 = () => {
  	let res = 0;
  	for(let i = 0; i < arguments.length; i ++) {
  res += arguments[i];
  }
  return res;
  }
  var sum2 = (...arg) => {
  let res = 0;
  for(let i = 0; i < arg.length; i ++) {
  res += arg[i];
  }
  return res;
  }
  console.log(sum1(1, 2, 3, 4)) // Uncaught ReferenceError: arguments is not defined
  console.log(sum2(1, 2, 3, 4)) // 10
  ```
    * 展开运算符（...）
  
      可以在函数调用/数组构造时将数组表达式或者string在语法层面展开；还可以在构造字面量对象时，将对象表达式按key-value的方式展开。（字面量一般指[1, 2, 3]或者{name: "lee"}这种简洁的构造方式，多层嵌套的数组和对象扩展运算符无法扩展。
  
      一些用法：
  
      * 等价于apply的使用
  
        如果想将数组元素迭代为函数参数，一般使用Function.prototype.apply的方式进行调用：
  
        ```javascript
        function myFunction(x, y, z) { }
        var args = [0, 1, 2];
        myFunction.apply(null, args);
        ```
  
        有了展开语法后可以写为：
  
        ```javascript
        function myFunction(x, y, z) { }
        var args = [0, 1, 2];
        myFunction(...args);
        ```
  
      * 数组和对象的复制
  
        ```javascript
        //数组的复制
        var arr1 = ['hello']
        var arr2 =[...arr1]
        arr2 // ['hello']
        //对象的复制
        var obj1 = {name:'chuichui'}
        var obj2 ={...arr}
        obj2 //  {name:'chuichui'}
        ```
  
      * 数组和对象的合并
  
        ```javascript
        //数组的合并
        var arr1 = ['hello']
        var arr2 =['chuichui']
        var mergeArr = [...arr1,...arr2]
        mergeArr  // ['hello','chuichui']
        // 对象分合并
        var obj1 = {name:'chuichui'}
        var obj2 = {height:176}
        var mergeObj = {...obj1,...obj2}
        mergeObj // {name: "chuichui", height: 176}
        ```
  
      * 解构字符串
  
        ```javascript
        var arr1 = [...'hello']
        arr1 // ["h", "e", "l", "l", "o"]
        ```

* **模板字面量**

  允许嵌入表达式的字符串字面量。使用反引号来替代普通字符串中的双引号和单引号。模板字符串可以包含特定语法（`${expression}`）的占位符。占位符中的表达式和周围的文本会一起传递给一个默认函数，该函数负责将所有部分连接起来。

    * 多行字符串

      * 一般使用

      ```javascript
      console.log('string text line 1\n' + 
      'string text line 2');
      // "string text line 1
      // string text line 2"
      ```

      * 模板字面量使用

        ```javascript
        console.log(`string text line 1
        string text line 2`);
        // "string text line 1
        // string text line 2"
        ```

    * 字符串插值

      ```javascript
      // 普通字符串嵌入表达式
      var a = 5;
      var b = 10;
      console.log('Fifteen is ' + (a + b) + ' and\nnot ' + (2 * a + b) + '.');
      
      // 模板字符串
      var a = 5;
      var b = 10;
      console.log(`Fifteen is ${a + b} and
      not ${2 * a + b}.`);
      ```

    * 带标签的模板字面量

      标签实现了用函数解析模板字符串。标签函数的第一个参数包含一个字符串值的数组。其余的参数和表达式相关。最后，函数可以返回处理好的字符串（或也可以返回完全不同的东西）。用于该标签的函数可以被任意命名。

      ```javascript
      var person = 'Mike';
      var age = 28;
      
      function myTag(strings, personExp, ageExp) {
      
      var str0 = strings[0]; // "that "
      var str1 = strings[1]; // " is a "
      
      // There is technically a string after
      // the final expression (in our example),
      // but it is empty (""), so disregard.
      // var str2 = strings[2];
      
      var ageStr;
      if (ageExp > 99){
      ageStr = 'centenarian';
      } else {
      ageStr = 'youngster';
      }
      
      return str0 + personExp + str1 + ageStr;
      
      }
      
      var output = myTag`that ${ person } is a ${ age }`;
      
      console.log(output);
      // that Mike is a youngster
      ```

    * 原始字符串

      在标签函数的第一个参数中，存在一个特殊的属性raw，可以通过它来访问模板字符串的原始字符串，而不经过特殊字符的替换。

      ```javascript
      function tag(strings) {
      console.log(strings.raw[0]);
      }
      
      tag`string text line 1 \n string text line 2`;
      // logs "string text line 1 \n string text line 2" ,
      // including the two characters '\' and 'n'
      ```

      

*参考*：

https://jscode.me/t/topic/109

https://segmentfault.com/a/1190000021975579



### <span id="head4"> 2、Map与普通Object的区别？</span>

* Map继承自Object

* 在Object中，key必须是简单数据类型（整数、字符串或者是symbol）；在Map中可以是JavaScript支持的所有数据类型，即可以用Object来作为Map的key。

* Map元组的顺序遵循插入的顺序，Object没有这一特性。

* 新建实例

  * Object
    * `var obj = { ... }`
    * `var obj = new Object()`
    * `var obj = Object.create(null)`
  * Map
    * `var map = new Map([1, 2], [2, 3])`

* 数据访问

  * Object：`[]`和`.`
  * Map：`map.get(1) // 2`

* 是否有某个元素

  * Object：`obj.id === undefined`或`'id' in obj`

也可以使用`Object.prototype.hasOwnProperty()`判断某个key是否是这个对象本身的属性（不包含从原型链继承的属性）

  * Map：`map.has(1)`

* 新增数据

  * Object：`obj['key'] = value`或`obj.key = value`
  * Map：`map.set(key, value)`

* 删除数据

  * Object：`delete obj.id`或`obj.id = undefined`

第一种是真的将属性从对象中删除，第二种属性仍然在对象上，意味着在使用for...in...去遍历的时候仍然会访问到该属性

  * Map：原生方法`map.delete(1)`，全部删除为`map.clear()`

* 获取size

  * Object：`Object.keys(obj).length`
  * Map：`map.size`

* 迭代

  * Object：自身不支持迭代
  * Map：自身支持迭代

判断方法：

```javascript
console.log(typeof obj[Symbol.iterator]); // undefined
console.log(typeof map[Symbol.iterator]); // function
```

所以Map可以展开为二维数组，但是Object不能，只能展开为对象*（为什么？）*

* 选择方法

一些不完全的总结：

  * 如果key都是简单数据类型的话优先使用Object。因为创建起来比较简单。
  * Map是纯粹hash，Object还会有一些其他内在逻辑，在执行delete时会有性能问题。如果有大量删除和插入的操作，使用Map会更好。
  * Map在存储大量元素的时候性能表现更好，特别是在代码执行不能确定key的类型的情况。



*参考*：

https://blog.csdn.net/ckwang6/article/details/89215396

https://blog.csdn.net/github_38618068/article/details/105785608



### <span id="head5"> 3、Symbol数据类型</span>

Symbol可以具有字符串类型的描述，但是即使描述相同，Symbol也不相等。

带描述符的定义和唯一性验证：

```javascript
let s1 = Symbol("Symbol1");
let s2 = Symbol("Symbol2");
let s3 = Symbol("Symbol1")
s1 == s2;// false
s1 === s2;//false
s1 === s3;//false
```

描述内容不一致，两个变量完全不相等；描述内容一致，两个变量也完全不相等。

Symbol数据的全局使用：

```javascript
const gs1 = Symbol.for('global_symbol_1')  //注册一个全局Symbol
const gs2 = Symbol.for('global_symbol_1')  //获取全局Symbol

gs1 === gs2  // true
```

**使用一：用在对象中来声明某个特殊的key值**

Symbol类型的值，在`Object.keys()`或者`for...in`这种枚举操作的时候，Symbol类型会表现成为不可枚举的状态：

```javascript
const NAME_SYMBOL = Symbol()
let obj = {
	name:"yuz",
	"age":"18",
	[NAME_SYMBOL]:"echo"
}
console.log(Object.keys(obj)) // [ 'name', 'age' ]
for(let attr in obj){
	console.log(attr) //"name","age"
}
```

可以利用这一点特性，来修饰对象内部不可输出的变量，即一种内部私有属性的定义。

如果需要遍历对象中包括Symbol的所有属性，可以通过这样的方法取值：

```javascript
// Object中有几种专门针对Symbol的API
Object.getOwnPropertySymbols(obj);//[ Symbol() ]

// 通过另一个方法能够获取到所有的key值
Reflect.ownKeys(obj);// [ 'name', 'age', Symbol() ]
```

**使用二：一个类中的私有属性**

类定义：

```javascript
const USER_PASSWORD = Symbol()

class Person{
  constructor(username , password){
    this.username = username
    this[USER_PASSWORD] = password
  }
  //定义一个方法
  getPassword(p){
    return (this[USER_PASSWORD] === p )
  }
}
module.exports = Person
```

使用：

```javascript
const Person = require("./b.js")
let person = new Person("11","321")

//由此可知在外部无法获取内部定义的私有状态
console.log(person[USER_PASSWORD]) //报错

let res = person.getPassword("321")
console.log(res) //true
```



*参考*：

https://blog.csdn.net/qq_41583484/article/details/108390882



### <span id="head6"> 4、JS原型链是如何连接的？原型链的产生？</span>

每个JS对象一定对应着一个原型对象，并从原型对象继承属性和方法。原型对象主要是用来实现继承，而原型链就是继承所产生的一个结果。

对象`__proto__`属性的值就是它所对应的原型对象。

```javascript
var one = {x : 1};
var two = new Object();
one.__proto__ === Object.prototype; // true
two.__proto__ === Object.prototype; // true
one.toString === one.__proto__.toString; // true
```

`__proto__`属性都是由一个对象指向一个对象，即指向它们的原型对象（父对象），其作用是当访问一个对象的属性时，如果该对象内部不存在这个属性，那么就会去它的__proto__属性所指向的对象里找，如果该父对象也不存在这个属性，则继续往父对象的__proto__属性所指向的那个对象里找，如此反复，直到原型链顶端null。这种通过__proto__属性来连接对象直到null的一条链即为所谓的原型链。



### <span id="head7"> 5、事件循环？宏任务微任务执行完之后会做什么？</span>

* 事件循环：

（1）JavaScript引擎等到宿主环境分配宏观任务，宏观任务的队列相当于事件循环。

（2）同步和异步任务分别进入不同的执行环境。同步任务进入主线程，即主执行栈，异步任务进入Event Queue。主线程内的任务执行完毕为空，会去Event Queue读取对应的任务，推入主线程执行。上述过程的不断重复就是事件循环。

* 在事件循环中，每一次循环操作称为tick，每一个tick的任务处理模型较为复杂，关键步骤如下：

  * 在此次 tick 中选择最先进入队列的任务( oldest task )，如果有则执行(一次)

  * 检查是否存在 Microtasks ，如果存在则不停地执行，直至清空Microtask Queue

  * 更新 render

  * 主线程重复执行上述步骤



## <span id="head8"> 网络基础</span>

### <span id="head9"> 1、TCP三次握手四次挥手</span>

* **TCP三次握手：**
  * A->B：含有同步序列号标志位的数据段（SYN）请求建立连接。（想要建立连接；哪个序列号是起始数据段？）
  * B->A：确认应答（ACK）+同步序列号（SYN）（收到，可传；哪个序列号是起始数据段？）
  * A->B：确认应答（ACK）（收到回复，开始传了）

* **TCP四次挥手：**

  * A->B：控制位FIN置1（提出停止TCP连接的请求）

  * B->A：ACK置1（这方向上的TCP连接关闭吗）

  * B->A：FIN置1（你那边的也关了吧）

  * A->B：ACK置1（好的我关了）



### <span id="head10"> 2、状态码</span>

- 1xx：临时回应，表示客户端请继续

- 2xx：请求成功

  * 200：请求成功

- 3xx：表示请求的目标有变化，希望客户端进一步处理

  * 301&302：永久性与临时性跳转

  - 304：客户端缓存没有更新
    * 产生前提：客户端本地已有缓存，并且在Request中告诉了服务端，当服务端通过时间或者tag发现没有更新的时候，就会返回一个不含body的304状态。

- 4xx：客户端请求错误

  * 403：无权限

  - 404：表示请求的页面不存在

- 5xx：服务端请求错误

  * 500：服务端错误

  - 503：服务端暂时性错误，可以一会再试




# <span id="head11"> 前端学院</span>

## <span id="head12"> 做一个在线简历（HTML篇）</span>

在Codepen上写的，比较简单，不做过多记录了。

Codepen：https://codepen.io/yuzkio/pen/QWpvoww

参考：https://developer.mozilla.org/zh-CN/docs/conflicting/Web/HTML/Element



## <span id="head13">Some Simple Question</span>s

* **HTML是什么，HTML5是什么？**

HTML指的是超文本标记语言（Hyper Text Markup Language）。

HTML5是最新的HTML标准，拥有更丰富的语义、图形以及多媒体元素等内容。

* **HTML元素标签、属性都是什么概念？**

HTML不是编程语言，是标记语言，所以要使用标记标签来描述网页。

属性是用来提供HTML标签更多的信息。

* **文档类型是什么概念，起什么作用？**

在互联网上有许多不同的文档，只有了解文档的类型，浏览器才能正确的显示文档。

提前声明文档类型可以帮助浏览器正确的显示网页。

* **meta标签都用来做什么的？**

通常所说的META标签，是在HTML网页源代码中一个重要的html标签。

META标签用来描述一个HTML网页文档的属性，例如作者、日期和时间、网页描述、关键词、页面刷新等。

* **Web语义化是什么，是为了解决什么问题？**

HTML的每个标签都有其特定含义(语义)，Web语义化是指使用语义恰当的标签，使页面有良好的结构，页面元素有含义,能够让人和搜索引擎都容易理解。

* **链接是什么概念，对应什么标签？**

HTML中的\<a>元素（或锚元素）可以创建一个到其他网页、文件、同一页面内的位置、电子邮件地址或任何其他URL的超链接。

* **常用标签都有哪些，都适合用在什么场景**

（略）

* 表单标签都有哪些，对应着什么功能，都有哪些属性

* **ol, ul, li, dl, dd, dt等这些标签都适合用在什么地方，举个例子**

ol、ul、li适用**无描述**的列表。例如：本文的这个问题的部分。

dl、dd、dt适用**有描述**的列表。例如：简历页面，介绍自己的信息、年龄、住址等。dt相当于“姓名：”这个部分，dd就是“xxx（一个名字）”。



*参考*：

http://ife.baidu.com/note/detail/id/395