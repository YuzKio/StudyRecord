- [ 今天的学习</span>](#head1)
  - [<span id="1">基础</span>](#head2)
  	- [<span id="1.1">访问一个网站的过程</span>](#head3)
  - [ 面经](#head4)
  	- [ HTML](#head5)
  		- [ 1、HTML页面常见的结构是怎么样的？](#head6)
  		- [ 2、HTML标签有哪几类？](#head7)
  		- [ 3、head标签内包含什么？](#head8)
  		- [ 4、HTML5新增的语义化标签](#head9)
  	- [ CSS](#head10)
  		- [ 1、CSS盒模型](#head11)
  		- [ 2、长度单位（em、rem等）](#head12)
  		- [ 3、CSS3怎么做动画？](#head13)
  		- [ 4、不定宽高的元素居中](#head14)

# <span id="head1"> 今天的学习</span>

*flag*：

	注册了个Codepen。感觉是个好东西，之前也有相应的资料有过，希望以后自己可以主动多去看一看。
	
	这周内把数据库的登录注册做好！
	
	写算法呀！



## <span id="head2"><span id="1">基础</span></span>

### <span id="head3"><span id="1.1">访问一个网站的过程</span></span>

总的来说，是浏览器和服务器交流、服务器和数据库交流的过程。
具体来说，从输入URL到显示页面，经历了以下过程：

- **域名解析（DNS解析）**：浏览器按照【浏览器缓存—系统缓存—路由器缓存—ISP缓存】的过程进行域名解析，获取相应的IP地址
- 浏览器向服务器发起**TCP连接**，与浏览器经历**三次握手**
- 握手成功后，浏览器向服务器**发送http请求**，请求数据包
- 服务器处理收到的请求，将数据返回至浏览器
1. Web Server进行相应的初步处理，使用服务器脚本生成页面
2. WebServer将生成的页面作为HTTP相应的body，根据不同的处理结果生成HTTP header发回给客户端
- 浏览器收到HTTP响应
- 读取页面内容、浏览器渲染、解析HTML源码
1. 解析过程中遇到引动的服务器上的资源再向Web Server发送请求，Web Server找到对应的文件发送回来。
- 生成DOM树，解析CSS样式，JS交互
- 客户端和服务器交互
1. 交互过程中客户端向服务器索取或提交额外的数据（局部刷新等），一般是跳转、或通过JS代码（相应某个动作或者定时）向Web Server发送请求，Web Server再用服务器脚本进行处理（生成资源或写入数据），把资源返回给客户端
- ajax查询等

*参考：*
https://blog.csdn.net/shan1991fei/article/details/81118734
https://www.zhihu.com/question/22689579




## <span id="head4"> 面经</span>

### <span id="head5"> HTML</span>

#### <span id="head6"> 1、HTML页面常见的结构是怎么样的？</span>

完整的HTML包括html DOCTYPE声明、tiltle、head、网页编码声明等。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body></body>
</html>
```

- DOCTYPE：文档声明，位于页面的首行，告知浏览器使用哪种HTML版本规范方式解析网页
- html：包裹着head和body
1. head：描述HTML文件各种属性和信息，比如网页标题、字符编码、是否启用缓存，引用的外部脚本和样式等等。
     * title：网页的标题
     * meta：提供有关页面的元信息，比如针对搜索引擎的关键字、缓存时间、启用浏览器内核等。有两个主要属性：name和http-equiv。
       1. name属性：用于描述网页，比如定义网页的关键词，关键内容、标注作者、版权等。

```
<meta name="属性值" content="描述内容" />
```

​				 2. http-equiv属性：用于设置网页的字符集，缓存机制等

```
<meta http-equiv="属性值" content="参数" />
```

2. body：HTML的主体，网页的文本、超链接、图像、表格、视频等所有在网页上显示的内容。



- **常用name属性值：**
**keywords**——告诉搜索引擎网页的关键字
**description**——告诉搜索引擎网站的主要内容
**robots**——告诉爬虫哪些页面需要索引，哪些页面不需要索引
**author**——标注网页的作者信息
**generator**——标注网页用什么IDE做的
**copyright**——标注版权信息
**renderer**——用于指定双核浏览器默认以什么方式进行页面渲染content="webkit"为webkit内核，content="ie-comp"为IE兼容模式，content="ie-stand"为IE标准模式。	

- **常用http-equiv属性值：**
**content-type**——设定网页字符集
**X-UA-Compatible**——告知浏览器以什么版本来渲染页面
**cache-control**——设置浏览器如何缓存某个响应以及缓存多长时间
**Set-Cookie**——设置cookie设定



*参考*：
https://blog.csdn.net/cyjbdqn/article/details/102643927



#### <span id="head7"> 2、HTML标签有哪几类？</span>

HTML标签分为块级标签、行内标签、内联块状标签。

* 块级标签：

  * 标签可独占一行，可指定宽高
  * `magrin`和`padding`的上下左右均对其有效
  * 可以自动换行
  * 多个块状元素标签写在一起，默认排列方式从上至下
  * 可以使用`margin: 0 auto`自动对齐
  * 常见的有：<div>、<p>、<h1>...<h6>、<ol>、<ul>、<dl>、<table>、<address>、<blockquote>、<form>

* 内联标签：

  * 标签在一行内，宽度和高度由内容决定，只有在内容超过HTML的宽度时才会换行（不能自动换行）
  * `margin`上下无效果，只有左右有效果，`padding`都有效果，会撑大空间；`box-sizing: border-box`无效，因为该属性针对盒模型。
  * 常见的有：<a>、<span>、<i>、<em>、<strong>、<label>、<q>、<var>、<cite>、<code>

* 内联块状标签（inline-block）

  * 同时具备内联元素、块状元素的特点（`display:inline-block`）

  * 不会自动换行

  * 能够设置宽高

  * 默认排列方式为从左到右

  * 可以使用`text-align:center`使内容相对于父盒子水平居中对齐。例如img标签，可以使用其相对于父盒子居中对齐，而`margin:0 auto`无效。

  * 水平排列，但所有元素默认会有一个空格的间隙，因为元素之间在html中书写有回车换行，浏览器解析会将其解析为一个空格。

  * 常见的有：<img>、<input>



*参考：*

https://www.html.cn/qa/html5/13389.html



#### <span id="head8"> 3、head标签内包含什么？</span>

* **title**：唯一必需元素

* **base**：为页面上的所有链接规定默认地址或默认目标。通常情况下，浏览器会从当前文档的URL中提取相应的元素来填写相对URL中的空白。
使用<base>标签可以改变这一点。浏览器随后将不再使用当前文档的URL，而使用指定的基本URL来解析所有的相对URL。这其中包括 <a>、<img>、<link>、<form>标签中的 URL。

可选属性：target。值：\_blank、\_parent、\_self、\_top、framename。表明在何处打开页面中所有的链接。

* **link**：链接一个外部样式表。主要属性：href、rel（指示被链接的文档是样式表，stylesheet）、type（MIME类型，“text/css”）、charset（被链接文档的字符集）

* **script**

* **style**

* **meta**：提供有关页面的元信息。

*参考*：

https://www.cnblogs.com/--cainiao/p/10266567.html



#### <span id="head9"> 4、HTML5新增的语义化标签</span>

article、aside、audio、bdi、canvas、command、datalist、details、embed、figcaption、figure、footer、header、hgroup、keygen、mark、meter、nav、output、progress、rp、rt、ruby、section、source、summary、time、track、video

![img](https://img-blog.csdn.net/20180609233744464)

除了图中的标签外还有：

* \<figure>：一组媒体对象及文字
* \<figcaption>：定义figure的标题
* \<hgroup>：定义对网页标题的组合
* \<dialog>：定义一个对话框
* \<datalist>：选项列表
* \<time>
* \<ruby>：两个子元素，rt为注释的内容，rp是该标签不显示时显示的文件。

```html
<ruby>
    柚子<rt>Yuzu</rt>
    <rp>can't display</rp>
</ruby>
```

* \<details>：描述文档或文档某一部分的细节

```html
<details>
    <summary>点击查看更多</summary>
    <p>
        点击后的内容
    </p>
</details>
```

* \<mark>：给想要突出显示的文本加个背景色
* \<progress>：显示数据的进度，属性value指定当前值，max最大值。

```html
<progress value="30" max="100"></progress>
```

* \<video>：src引入资源，controls视频的控制控件。以防用户浏览的视频不支持某些格式的视频，为用户多准备一些格式的视频

```html
<video controls="controls">
  <source src="" type="video/ogg">
  <source src="" type="video/mp4">
  <source src="" type="video/webm">
  你的浏览器不支持video标签
</video>
```

* \<audio>：不加controls不显示音频的控制界面

* \<datalist>：提示可能的值，datalist及其选项不会被显示出来，它仅仅是合法输入值的列表使用input元素的list属性来邦定datalist，下面选项使用option定义。标签被用来在为 <input> 元素提供"自动完成"的特性。用户能看到一个下拉列表，里边的选项是预先定义好的，将作为用户的输入数据。

```html
<input type="text" list="cars">
<datalist id="cars">
	<option value="宝马"></option>
	<option value="奔驰"></option>
	<option value="奥迪"></option>
</datalist>
```

* \<embed>：定义插入的内容，如插件、flash

```html
<embed src="swf/flash5924.swf" tyep="application/x-shockwave-flash">
</embed>
```

* \<canvas>：容器。可以通过控制坐标在canvas上绘制图形。

*参考*：

https://blog.csdn.net/sunming709424/article/details/79086240

https://www.cnblogs.com/xxqd/p/12179738.html



### <span id="head10"> CSS</span>

#### <span id="head11"> 1、CSS盒模型</span>

CSS基础和模型将所有元素表示为一个个矩形的盒子。CSS决定这些盒子的大小、位置以及属性。

每个盒子由四个部分组成，效用由各自的边界定义：Content、Padding、Border、Margin

* content area
  * 尺寸为内容宽度和内容高度
  * `box-sizing:content-box` 时，内容区域的大小可明确通过`width`, `min-width`, `max-width`, `height`, `min-height`和`max-height`控制

![img](C:\Users\40724\AppData\Local\YNote\data\407249117@qq.com\dd2b0208793d4d95a3965ebbcd74601a\clipboard.png)

*参考*：

https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model



#### <span id="head12"> 2、长度单位（em、rem等）</span>

* **em**： 1em等于元素的font-size。理论上1em等于所用字体中小写字母m的宽度。
* **ex**： 所用字体中小写字母m的宽度。
* **rem**： em相对当前元素的字号计算，rem始终相对根元素计算。
* **ch**： 等于渲染时所用字体中“0”字形的进矩。
* **视区相关单位vw、vh、vmin、vmax**

*参考*：《CSS权威指南》



#### <span id="head13"> 3、CSS3怎么做动画？</span>

使用animation属性和@keyframes。anamation用于给动画设置CSS样式。通过@keyframes定义，再在animation中调用。

* animation-name：声明@keyframes要操作的at-rule的名称。
* animation-duration：动画完成一个循环所需的时间长度。
* animation-timing-function：建立预设的加速度曲线，如ease或linear
* animation-delay：正在加载的元素和动画序列的开始之间的时间
* animation-direction：设置循环后动画的方向。它的默认值在每个周期重置。
* animation-iteration-count：动画应执行的次数。
* animation-fill-mode：设置在动画之前/之后应用的值。
* animation-play-state：暂停/播放动画



#### <span id="head14"> 4、不定宽高的元素居中</span>

* 水平居中

  * inline-block+text-align

```CSS
.parent{
	width: 400px;
	height: 100px;
	background: #bbb;
	text-align: center;
}
.child{
	display: inline-block;
	width: 100px;
	height: 100px;
	background: #333;
}
```

  * table+margin

```css
.parent{
	width: 400px;
	height: 100px;
	background: #bbb;
}
.child{
	display: table;
	margin: 0 auto;
	width: 100px;
	height: 100px;
	background: #333;
}
```

  * absolute+transform

```css
.parent{
	position: relative;
	width: 400px;
	height: 100px;
	background: #bbb;
}
.child{
	position: absolute;
	left: 50%;
	transform: translateX(-50%);
	width: 100px;
	height: 100px;
	background: #333;
}
```

  * flex+justify-content

```css
.parent{
	display: flex;
	justify-content: center;
	width: 400px;
	height: 100px;
	background: #bbb;
}
.child{
	width: 100px;
	height: 100px;
	background: #333;
}
```

*p.s. 单纯垂直居中有table-cell+vertical-align、absolute+transform和flex+align-items方法。*

* 垂直+水平居中

  * 方法一：父元素为table，子元素为cell-table，就可以使用`vertical-align:center`实现垂直居中。优点在于父元素可以动态地改变高度。

```css
.parent1{
	display: table;
	height:300px;
	width: 300px;
	background-color: #FD0C70;
}
.parent1 .child{
	display: table-cell;
	vertical-align: middle;
	text-align: center;
	color: #fff;
	font-size: 16px;
}
```

  * 方法二：子元素绝对定位，距顶部50%，左边50%，然后使用CSS3 `transform: translate(-50%, -50%)`

```CSS
.parent3{
	position: relative;
	height:300px;
	width: 300px;
	background: #FD0C70;
}
.parent3 .child{
	position: absolute;
	top: 50%;
	left: 50%;
	color: #fff;
	transform: translate(-50%, -50%);
}
```

  * 方法三：使用CSS3 flex布局

```css
.parent4{
	display: flex;
	justify-content: center;
	align-items: center;
	width: 300px;
	height:300px;
	background: #FD0C70;
}
.parent4 .child{
	color:#fff;
}
```



*参考*：

https://www.cnblogs.com/jogen/p/5213566.html

https://blog.csdn.net/qq_41960337/article/details/88668753
