# JavaScript红宝书（八）对象、类与面向对象编程

## 理解对象

* **属性的类型**

  属性分为两种：数据属性和访问器属性。

  **数据属性**有四个特性描述它们的行为：[[Configurable]]、[[Enumerable]]、[[Writable]]、[[Value]]

  修改属性的默认特性，使用`Object.defineProperty()`方法（使用此方法定义时configurable、enumerable和writable的值都默认为false）：

  ```javascript
  let person = {};
  Object.defineProperty(person, "name", {
      writable: false;
      value: "Nicholas"
  })
  ```

  **访问器属性**不能直接定义，必须使用`Object.defineProperty()`方法。四个特性[[Configurable]]、[[Enumerable]]、[[get]]、[[set]]

  **读取属性的特性**有方法`Object.getOwnPropertyDescriptor`和`Object.getOwnPropertyDescriptors`

  **合并对象**就是把源对象所有的本地属性一起复制到目标对象上，有时候这种操作也被成为混入（mixin）。ES6中为合并对象提供了`Object.assign()`方法。这个方法接收一个目标对象和一个或多个源对象作为参数，然后将每个源对象中可枚举（`Object.propertyIsEnumerable`）和自有（`Object.hasOwnProperty`）属性复制到目标对象。对每个符合条件的属性，这个方法会使用源对象上的[[Get]]取得属性的值，然后使用目标对象上的[[Set]]设置属性的值。不能在两个对象间转移获取函数和设置函数。

  **对象解构**就是使用与对象匹配的结构来实现对象属性赋值。

