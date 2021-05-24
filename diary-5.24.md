# 今天的学习

*flag*：注册了个CodeOpen。感觉是个好东西，之前也有相应的资料有过，希望以后自己可以主动多去看一看。

## 基础

### 访问一个网站的过程

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




## 面经
### HTML

**1、HTML页面常见的结构是怎么样的？**

完整的HTML包括html DOCTYPE声明、tiltle、head、网页编码声明等。

```
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
>**常用name属性值：**
>**keywords**——告诉搜索引擎网页的关键字
>**description**——告诉搜索引擎网站的主要内容
>**robots**——告诉爬虫哪些页面需要索引，哪些页面不需要索引
>**author**——标注网页的作者信息
>**generator**——标注网页用什么IDE做的
>**copyright**——标注版权信息
>**renderer**——用于指定双核浏览器默认以什么方式进行页面渲染content="webkit"为webkit内核，content="ie-comp"为IE兼容模式，content="ie-stand"为IE标准模式。	

​						2. http-equiv属性：用于设置网页的字符集，缓存机制等

```
<meta http-equiv="属性值" content="参数" />
```
>**常用http-equiv属性值：**
>**content-type**——设定网页字符集
>**X-UA-Compatible**——告知浏览器以什么版本来渲染页面
>**cache-control**——设置浏览器如何缓存某个响应以及缓存多长时间
>**Set-Cookie**——设置cookie设定
> 2. body：HTML的主体，网页的文本、超链接、图像、表格、视频等所有在网页上显示的内容。

*参考*：
https://blog.csdn.net/cyjbdqn/article/details/102643927

