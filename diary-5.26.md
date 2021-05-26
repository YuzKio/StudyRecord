# 面经

## JavaScript

### 1、浏览器的事件代理？



## 网络





# 前端学院

## 做一个在线简历（CSS篇1）

Codepen：https://codepen.io/yuzkio/pen/QWpvoww

* CSS font的简写规则

  字体属性主要包括下面几个：font-family，font-style（normal、italic、oblique），font-variant（normal、small-caps），font-weight，font-size，font

  **顺序**：font-style | font-variant | font-weight | font-size/line-height | font-family



## CSS如何工作

不同浏览器处理文件时候的步骤：

* 浏览器载入HTML文件（比如从网络上获取）

* 将HTML文件转化成一个DOM（Document Object Model），DOM是文件在计算机内存中的表现形式

* 接下来，浏览器会拉取该HTML相关的大部分资源，比如嵌入到页面的图片、视频和CSS样式。JavaScript则会稍后进行处理

* 浏览器拉取到CSS之后会进行解析，根据选择器的不同类型（比如element、class、id等等）把他们分到不同的“桶”中。浏览器基于它找到的不同的选择器，将不同的规则（基于选择器的规则，如元素选择器、类选择器、id选择器等）应用在对应的DOM的节点中，并添加节点依赖的样式（这个中间步骤称为渲染树）

* 上述的规则应用于渲染树之后，渲染树会依照应该出现的结构进行布局

* 网页展示在屏幕上（这一步被称为着色）

  ![img](https://mdn.mozillademos.org/files/11781/rendering.svg)



## CSS选择符

* **元素选择符**：HTML预定义的某个元素（html，div，p，...）

* **通用选择符**：*

* **类选择符**：可以赋予任意个元素

- - （.）：包含所指示类的所有元素（相当于省略了通配符）
  - （其他选择符).(类)：匹配包含(类)的(其他选择符)元素。比如p.warning只匹配包含了warning类的p元素。
  - 两个类选择符串在一起，选择的是同时具有两个类名的元素，而且对类名的顺序没有要求。例如HTML源码中写class="urgent warning"，而CSS选择符写的是.warning.urgent。并且串写选择符只会影响同时具有这两个类名的元素，单独有某一类名的选择器不会被串写选择符的属性影响。

* **ID选择符**：

- - 散列字元（#）
  - HTML文档中一个ID能且仅能使用一次
  - 不能串在一起使用，其值不是能以空格分隔的列表

* **属性选择符**：

- - 简单属性选择符：选择具有某个属性的元素，不管属性的值。

  - - h1[class] { color: silver;}		选择具有class属性的h1元素，将字体颜色设置为silver
    - a[href][title]				基于多个元素的选择，这两个选择是&&而不是||

  - 精准属性值选择符：只选择属性为特定值的元素。

  - - 要求属性的值与指定的值完全一致。 
    - ID选择符与引用id属性的属性选择符不完全等效。

  - 部分匹配属性值选择符

  - - [foo|="bar"]：以bar和一个英文破折号或bar本身开头
    - [foo~="bar"]：选择的元素有foo属性，且有包含bar这个词的一组词。p.warning和p[class~="warning"]等效
    - [foo^="bar"]：选择的元素有foo属性，以bar开头
    - [foo$="bar"]：选择的元素有foo属性，以bar结尾

  - 起始值属性选择符

* **文档结构选择符**

- - 后代选择符：空格
  - 子代选择符：>
  - 紧邻同胞连接符：+
  - 一般同胞连接符：~

* **伪类选择符**

- - 伪类始终指代所依附的元素

  - 选择根元素：:root

  - 选择空元素：:empty	没有任何子代的元素，甚至连文本节点都没有（包括文本和空白），唯一一个在匹配时考虑文本节点的CSS选择符

  - 选择唯一子代：:only-child

  - 选择唯一元素类型：:only-of-type

  - 选择第一个子代：:first-child

  - 选择最后一个子代：:last-child

  - 选择第一个某种元素：:first-of-type

  - 选择最后一个某种元素：:last-of-type

  - 选择每第n个子元素：:nth-child(n)/nth-last-child(n)

  - 动态伪类：

  - - 链接伪类：:link :visited

    - 用户操作伪类：

    - - :focus：当前获得输入焦点的元素
      - :hover：鼠标指针放置其上的元素
      - :active：由用户输入激活的元素

  - UI状态伪类：

  - - :enabled：启用的用户界面元素
    - :disabled
    - :checked
    - :indeterminate：只能由DOM设定，不能由用户设定
    - :default：默认选中的单选按钮、复选框或选项
    - :valid：用户输入的值满足全部数据验证条件
    - :invalid：不满足全部
    - :in-range
    - :out-of-range
    - :required
    - :optional
    - :read-write
    - :read-only

  - :target伪类

  - - 如果对应的页面中有ID为target-pseudo（片段标识符）的元素，那个元素就是片段标识符的目标

  - :lang伪类

  - 否定伪类:not()：

  - - 括号中是简单的选择符（一个类型选择符、通用选择符、属性选择符、类选择符、ID选择符或伪类）（没有祖辈-后代关系的选择符）

* **伪元素选择符**
  伪类使用一个冒号，伪元素使用两个；所有伪元素只能出现在选择符的最后。

  * ::first-letter：任何非行内元素的首字母

  * ::first-line

  以上两个伪元素选择符只能应用到块级元素上（例如标题和段落），而不能应用到行内元素上（如超链接）

  * ::before：创建/装饰前置元素
  * ::after：创建/装饰后置元素