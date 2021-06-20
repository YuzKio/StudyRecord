**【写在前面】**

前一阵子刚开始整了几天日记之后就折腾期末去了，连前端学习也荒废了好久。现在期末ddl紧迫的硬骨头算是啃完了，开始重拾前端学习！

老实说，没有学前端的这段时间也翻了翻知乎的前端学习路径、前端入门必备的知识什么的，感觉自己差得好多；期末虽然是有整了前端的项目，但是用了字节大佬的简单模板，其他地方也是囫囵吞枣，也没做优化，就这样还耗费了挺长的时间。我用了半个月的时间再一次深刻地意识到自己知识储备和实践经验都很缺乏，身边的人一个一个都说要去大厂实习了，而我八字都还没一撇呢。时不时感觉好焦虑。但还能怎么办，只能硬着头皮塔塔开啦！不能被社会达尔文主义打败！每天进步一点点就好啦！

然后就简单总结一下自己到七月份之前要做的事：

* 围绕开题准备组会论文（下周三）
* 做好开题PPT
* 优化一下数据库大作业的项目，可能还得重构一下代码
* 每天看看面经，写写算法
* 改改简历，投一下实习，面试
* 数据仓库大作业和考试



# 面经

今天看的面经：百度前端实习

地址：https://www.nowcoder.com/discuss/643727?type=post&order=time&pos=&page=1&ncTraceId=&channel=-1&source_id=search_post_nctrack

## 1、浏览器的缓存机制，强缓存和协商缓存的过程

<a herf="https://github.com/YuzKio/StudyRecord/blob/main/diary-5.26-27.md#head8">5.26-27的日记中有写</a>

强缓存就是一种在服务器端进行的缓存配置。当浏览器第一次请求某个资源，服务器端就在response header中配置cache-control，如果它配置的不是no-cache或者no-store，都是在进行强缓存的配置。

常见的配置有max-age（有效期）、public（客户端和代理服务器都可以缓存）、private（代理服务器不缓存）和immutable（在有效期内，做刷新操作也不向服务器发起http请求，而是直接读取缓存）

如果配置的值no-cache，表示不设置强缓存，但是不影响协商缓存的设置；配置no-store，表示客户端和服务器端都不缓存。

我理解的强缓存（没过期的时候）与协商缓存的区别就是，当有本地缓存的时候，需不需要再与服务器进行通信。

当浏览器向服务器发送请求时，如果命中协商缓存，则服务器就向浏览器返回e-tag、last-modified（其实强缓存过程中也会有这两个值，只不过在缓存没过期的时候其实都用不到）。下一次浏览器还需要用到这个资源的时候，浏览器就要带着e-tag和last-modified，去询问服务器这个资源有没有发生改变。如果没改变，服务器返回304，浏览器继续使用原来的缓存；如果发生改变了，服务器返回200和改变后的资源，浏览器用这个改变后的资源。

<a herf="https://juejin.cn/post/6844903763665240072">这篇</a>总结得挺好。

## 2、HTTP状态码

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

## 3、BFC

我竟然好像是今天第一次看到这个概念？

**一、常见定位方案**

* 普通流（normal flow）

  在普通流中，元素按照其在 HTML  中的先后位置至上而下布局，在这个过程中，行内元素水平排列，直到当行被占满然后换行，块级元素则会被渲染为完整的一个新行，除非另外指定，否则所有元素默认都是普通流定位，也可以说，普通流中元素的位置由该元素在 HTML 文档中的位置决定。

* 浮动（float）

  在浮动布局中，元素首先按照普通流的位置出现，然后根据浮动的方向尽可能的向左边或右边偏移，其效果与印刷排版中的文本环绕相似。

* 绝对定位（absolute position）

  在绝对定位布局中，元素会整体脱离普通流，因此绝对定位元素不会对其兄弟元素造成影响，而元素具体的位置由绝对定位的坐标决定。

**二、BFC概念**

* Formatting context：它是页面中的一块渲染区域，并且有一套渲染规则，它决定了其子元素将如何定位，以及和其他元素的关系和相互作用。

* BFC（Block Formatting context）：块级格式化上下文，属于定位方案的普通流

  具有BFC特性的元素可以看做是隔离了的独立容器，容器里面的元素不会在布局上影响到外面的元素，并且BFC具有普通容器所没有的一些特性。

**三、触发BFC**

只要元素满足下面任一条件即可触发BFC特性：

* body 根元素
* 浮动元素：float除none以外的值
* 绝对定位元素：position(absolute、fixed)
* display为inline-block、table-cells、flex
* overflow除了visible以外的值（hidden、auto、scroll）

**四、BFC特性及应用**

**1、同一个BFC下外边距会发生折叠**

​	想要避免外边距的重叠，可以放在不同的BFC容器中。

**2、BFC可以包含浮动的元素（清除浮动）**

​	浮动的元素会脱离普通文档流：

```html
<div style="border: 1px solid #000;">
    <div style="width: 100px; height: 100px; background: #eee; float: left;"></div>
</div>
```

<div style="border: 1px solid #000;">
	<div style="width: 100px; height: 100px; background: #eee; float: left;"></div>
</div>



​	

​	由于容器内元素浮动，脱离了文档流，所以上述代码的容器只剩下2px的边距高度。如果触发容器的BFC，那么容器将会包裹着元素浮动。

```html
<div style="border: 1px solid #000; overflow: hidden;">
    <div style="width: 100px; height: 100px; background: #eee; float: left;"></div>
</div>
```

<div style="border: 1px solid #000; overflow: hidden;">
    <div style="width: 100px; height: 100px; background: #eee; float: left;"></div>
</div>

**3、BFC可以阻止元素被浮动元素覆盖**

文字环绕效果：

```html
<div style="height: 100px;width: 100px;float: left;background: lightblue">
    我是一个左浮动的元素
</div>
<div style="width: 200px; height: 200px;background: #eee">
    我是一个没有设置浮动, 
也没有触发 BFC 元素, width: 200px; height:200px; background: #eee;
</div>
```

<div style="height: 100px;width: 100px;float: left;background: lightblue">
    我是一个左浮动的元素
</div>
<div style="width: 200px; height: 200px;background: #eee">
    我是一个没有设置浮动, 
也没有触发 BFC 元素, width: 200px; height:200px; background: #eee;
</div>

此时第二个元素有部分被浮动元素覆盖（但文本信息不会），想要避免这种情况，在第二个元素中加入`overflow: hidden`

<div style="height: 100px;width: 100px;float: left;background: lightblue">
    我是一个左浮动的元素
</div>
<div style="width: 200px; height: 200px;background: #eee; overflow: hidden;">
    我是一个没有设置浮动, 
也没有触发 BFC 元素, width: 200px; height:200px; background: #eee;
</div>

**五、与盒模型的对比**

**1、什么是盒模型？**

在HTML中，每一个元素都可以被看作一个盒子，这个盒子由：内容区（content）、填充区（padding）、边框区（border）、外边界区（margin）四部分组成。

盒模型是CSS布局的基本单位。

标准盒模型：width和height仅仅指内容区域的宽度和高度，增加内边距、边框和外边距不会影响内容区域的尺寸，但会增加元素框的总尺寸。

IE盒模型：width和height指的是内容区域+border+padding的宽度和高度

**2、BFC与盒模型**

我的理解是，BFC是一个容器，一个BFC也是一个盒子，它用来解决一些盒模型在应用时出现的布局上的问题，比如说边距折叠和清除浮动等。因为被BFC所包裹的元素不会影响到外部的元素，也不会受外部元素的影响。



*参考：*

https://zhuanlan.zhihu.com/p/25321647

https://blog.csdn.net/sinat_36422236/article/details/88763187

https://www.cnblogs.com/qianguyihao/p/8512617.html



## 4、垂直居中

之前在<a href="https://github.com/YuzKio/StudyRecord/blob/main/diary-5.24.md#head14">这里</a>也写过水平居中和垂直+水平居中的方法。

单纯的垂直居中有：table-cell+vertical-align、absolute+transform和flex+align-items

```html
<div style="width: 200px; height: 200px; background: pink; display: table;">
    <div style="color: #fff; display: table-cell; vertical-align: middle;">	
        test
    </div>
</div>
```

```html
<div style="width: 200px; height: 200px; background: pink;">
    <div style="position: relative; top: 50%; transform: translateY(-50%)";>	
        test
    </div>
</div>
```

```html
<div style="width: 200px; height: 200px; background: pink; position:relative;">
    <div style="position: absolute; top: 50%; transform: translateY(-50%)";>	
        test
    </div>
</div>
```

```html
<div style="width: 200px; height: 200px; background: pink; display: flex; align-items: center;">
    <div style="width: 20px; height: 20px; background: yellow;">	
    </div>
</div>
```

*参考*：

https://blog.csdn.net/qq_43677117/article/details/109475579



## 5、ES6新特性

之前在<a href="https://github.com/YuzKio/StudyRecord/blob/main/diary-5.25.md#head3">这里</a>有写过块级作用域、箭头函数、参数处理和模板字面量。

* **类**



## 6、ES7、ES8一些新特性



## 7、Webpack



## 8、跨域



## 9、手写代码：找出出现次数最多的元素

