# <span id="head1">面经</span>

## <span id="head2">网络/浏览器</span>

### <span id="head3">1、浏览器是什么？</span>

浏览器是一个软件。主要功能是向服务器发出请求，在浏览器窗口中展示用户选择的网络资源。这里说的资源一般是指HTML文档，也可以是PDF、图片或其他的类型。

浏览器解释并显示HTML文件的方式是在HTML和CSS规范中指定的。这些规范由网络标准化组织W3C进行维护。

* **浏览器的主流内核**

  * Trident内核：IE
  * Gecko内核：Firefox
  * WebKit内核：Chrome、Safari
  * Presto内核：Opera

* **浏览器的多进程架构**

  * 进程（process）和线程（thread）

    进程是系统进行资源分配和调度的基本单位。程序是指令、数据及其组织形式的描述，进程是程序的实体。

    线程是操作系统进行运算调度的最小单位。

  * 浏览器架构

    以Chrome为例，它采用多进程架构，其顶层存在一个Browser process用以协调浏览器的其他进程。其架构如下：

    ![img](https://pic3.zhimg.com/80/v2-6b4e841c652a7a15554e98abce726222_720w.jpg)

    * Browser Process：浏览器的主进程（负责协调、主控），只有一个。

      负责浏览器的页面显示，包括地址栏、书签栏、前进后退按钮等部分的工作；

      负责各个页面的管理，创建和销毁其他进程；

      将Renderer进程得到的内存中的Bitmap绘制到用户界面上；

      负责处理浏览器的一些不可见的底层操作，比如网络请求和文件访问。

    * Renderer Process（浏览器渲染进程）

      该进程内部是多线程的。默认每个Tab页面一个进程，互不影响。主要负责一个tab内关于网页呈现的所有事情，页面渲染、脚本执行、事件处理等。

    * Plugin Process（第三方插件进程）

      负责控制一个网页里用到的所有插件，每种类型的插件对应一个进程，仅当使用该插件时才创建，如flash
    
    * GPU Process
    
      负责处理GPU相关业务，最多一个，用于3D绘制等

* **浏览器多进程的优势**

  * 避免单个page crash影响整个浏览器
  * 避免第三方插件crash影响整个浏览器
  * 多进程充分利用多核优势
  * 方便使用沙盒模型隔离插件等进程，提高浏览器稳定性

* **浏览器渲染进程**

  * GUI渲染进程
    * 负责渲染浏览器界面，解析HTML、CSS，构建DOM树和RenderObject树，布局和绘制等；
    * 当界面需要重绘（Repaint）或由于某种操作引发回流（reflow）时，该线程就会执行；
    * GUI渲染线程和JS引擎线程是互斥的，当JS引擎执行时GUI线程会被挂起，GUI更新会被保存在一个队列中等到JS引擎空闲时立即被执行
  * JS引擎线程
    * 也称为JS内核，负责处理JavaScript脚本程序
    * JS引擎线程负责解析JavaScript脚本，运行代码
    * JS引擎一直等待着任务队列中任务的到来，然后加以处理，浏览器无论什么时候都只有一个JS线程在运行JS程序
    * GUI渲染线程与JS引擎线程是互斥的，所以如果JS执行时间过长，就会造成页面的渲染不连贯，导致页面渲染加载阻塞
  * 事件触发线程
    * 归属于浏览器而不是JS引擎，用来控制事件循环
    * 当JS引擎执行代码块如setTimeOut时（也可来自浏览器内核的其他线程，如鼠标点击、AJAX异步请求等），会将对应任务添加到事件线程中
    * 当对应的事件符合触发条件被触发时，该线程会把事件添加到待处理队列的队尾，等待JS引擎的处理
    * 由于JS的单线程关系，所以这些待处理队列中的事件都得排队等待JS引擎处理（当JS引擎空闲才会去执行）
  * 定时触发器线程
    * setInterval和setTimeout所在线程
    * 浏览器定时计数器并不是由JavaScript引擎计数的（因为JS引擎是单线程的，如果处于阻塞线程状态会影响计时的准确）
    * 通过单独线程来计时并触发定时（计时完毕后，添加到事件队列中，等待JS引擎空闲后执行）
  * 异步http请求线程
    * 在XMLHttpRequest连接后是通过浏览器新开一个线程请求
    * 当检测到状态变更时，如果设置有回调函数，异步线程就产生状态变更事件，将这个回调再放入事件队列中。再由JavaScript执行。

* **WebWorker**

  HTML5中支持了Web Worker。 Web Worker为Web内容在后台线程中运行脚本提供了一种简单的方法：

  * 创建Worker时，JS引擎向浏览器申请开一个子线程（子线程是浏览器开的，完全受主线程控制，而且不能操作DOM）
  * JS引擎线程与worker线程间通过特定的方式通信（postMessage API，需要通过序列化对象来与线程交互特定的数据）

  如果有耗时的工作，单独开一个Worker线程，等待计算出结果之后通信给主线程即可。

  WebWorker只属于某个页面，不会和其他页面的Render进程（浏览器内核进程）共享；SharedWorker是浏览器所有页面共享的，不能采用与Woker同样的方式实现，因为其不隶属于某个Render进程，可以为多个Render进程共享使用。

*参考*：

https://www.html5rocks.com/zh/tutorials/internals/howbrowserswork/

https://zhuanlan.zhihu.com/p/47407398

https://blog.csdn.net/sh435367384/article/details/79647326



### <span id="head4"> **2、HTTP和HTTPS的区别？**</span>

* **HTTP协议**：传输的数据都是未加密的（明文的），因此使用HTTP传输隐私信息非常不安全。

  * ***协议特点：***

    * 是一种请求/响应模式的协议
    * 简单快速：客户向服务器请求服务时，只需传送请求方法和路径。请求方法常用的有GET、HEAD、POST等。
    * 灵活：HTTP允许传输任意类型的数据对象，传输的类型由Content-Type加以标记。
    * 无连接：限制每次连接只处理一个请求。服务器处理完请求，并收到客户的应答后，即断开连接，但是却不利于客户端与服务器保持会话连接，为了弥补这种不足，产生了两项记录http状态的技术，一个叫做Cookie，一个叫做Session。
    * 无状态：无状态是指协议对于事务处理没有记忆，后续处理需要前面的信息，则必须重传。
    * 存在问题：请求信息明文传输，容易被窃听截取；数据的完整性未校验，容易被篡改；没有验证对方身份，存在冒充危险。

  * ***URI和URL***

    HTTP使用统一资源标识符（Uniform Resource Identifiers, URI）来传输数据和建立连接。

    * URI：统一资源标识符。标识一个具体资源，可以通过URI知道一个资源是什么。
    * URL（Location）：统一资源定位符。定位具体资源，标识具体的资源位置。

  * ***HTTP报文***

    * 请求报文：请求行（请求方法、URL、协议/版本），请求头，请求正文
    * 响应报文：状态行，响应头

  * ***常见请求方法***

    * GET：请求指定的页面信息，并返回实体主体
    * POST：向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
    * HEAD：类似于GET请求，只不过返回的响应中没有具体的内容，用于获取报头。
    * PUT：从客户端向服务器传送的数据取代指定的文档的内容。
    * DELETE：请求服务器删除指定的页面。

  * ***POST和GET***

    * 都包含请求头请求行，POST多了请求body
    * GET多用来查询，请求参数放在URL中，不会对服务器上的内容产生作用；POST用来提交，如把账号密码放入body中
    * GET是直接添加到URL后面的，直接就可以在URL中看到内容，而POST是放在报文内部，用户无法直接看到；
    * GET提交的数据长度有限制，因为URL长度有限制，具体的长度限制视浏览器而定。而POST没有。

  * ***状态码***

    * 1xx：信息型，服务器收到请求，需要请求者继续操作；
    * 2xx：成功型，请求成功收到，理解并处理；
      * 200：OK，客户端请求成功
    * 3xx：重定向，需要进一步操作以完成请求；
      * 301：资源（网页等）被永久转移到其他URL
      * 302：临时跳转
    * 4xx：客户端错误，请求包含语法错误或者无法完成的请求；
      * 400：客户端请求有语法错误，不能被服务器所理解
      * 401：请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
      * 404：请求资源不存在
    * 5xx：服务器错误，服务器在处理请求的过程中发生了错误。
      * 500：服务器内部发生了不可预期的错误
      * 503：服务器当前不能处理客户的请求，一段时间后可能恢复正常

* **HTTPS协议**：是由SSL（Secure Socket Layer，安全套接字层）/TLS（Transport Layer Security，传输层安全）+HTTP协议构建的可进行加密传输、身份认证的网络协议，比HTTP安全。

  * ***使用HTTPS传输数据的流程***

    ![img](https://pic4.zhimg.com/80/v2-a994fbf3094d737814fe01c2b919477b_720w.jpg)

    * 客户端通过URL访问服务器建立SSL连接
    * 服务端收到客户端请求后，会将网站支持的证书信息（证书中包含公钥）传送一份给客户端
    * 客户端的服务器开始协商SSL连接的安全等级，也就是信息加密的等级
    * 客户端的浏览器根据双方同意的安全等级，建立会话密钥，然后利用网站的公钥将会话秘钥加密，并传送给网站
    * 服务器利用自己的私钥解密出会话密钥
    * 服务器利用会话密钥加密与客户端之间的通信

  * ***HTTPS的缺点***

    * HTTPS协议多次握手，导致页面的加载时间延长
    * HTTPS连接缓存不如HTTP高效，会增加数据开销和功耗
    * 申请SSL整数需要钱，功能越强大的证书费用越高
    * SSL设计到的安全算法会消耗CPU资源，对服务器资源消耗较大

* **HTTPS和HTTP协议的区别**：

  * https协议需要到ca申请证书，一般免费证书较少，需要一定费用；
  * http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议；
  * http页面相应速度比https快，主要是因为HTTP使用TCP三次握手建立连接，客户端和服务器需要交换3个包，而HTTPS除了TCP的三个包，还要加上SSL握手需要的9个包，所以一共是12个包；
  * http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443；
  * http连接很简单，是无状态的；https协议是由ssl+http协议构建的可进行加密传输、身份认证的网络协议，比http协议安全



*参考*：

https://zhuanlan.zhihu.com/p/72616216

https://www.runoob.com/w3cnote/http-vs-https.html



### <span id="head5"> **3、公钥和私钥**</span>

* **私钥加密**

  对称密钥加密，又称私钥加密，即信息的发送方和接收方用一个密钥去加密和解密数据。优势是加密和解密速度快，适合对大数据量进行加密，但密钥管理困难。

* **公钥加密**

  公钥加密也叫非对称加密，非对称加密算法需要两个密钥：公开密钥（public key）和私有密钥（private key）。公开密钥和私有密钥是一对，如果用公开密钥对数据进行加密，只有用对应的私有秘钥才能解密；如果用私有密钥对数据进行加密，那么只有用对应的公开密钥才能解密。因为加密和解密使用的是两个不同的密钥，所以这种算法叫做非对称加密算法。

  * 公钥和私钥成对出现

  * 公开的密钥叫公钥，只有自己知道的叫私钥

  * 用公钥加密的数据只有对应的私钥可以解密

  * 用私钥加密的数据只有对应的公钥可以解密

  * 如果可以用公钥解密，则必然是对应的私钥加的密

  * 如果可以用私钥解密，则必然是对应的公钥加的密

    

*参考*：

http://songlee24.github.io/2015/05/03/public-key-and-private-key/

https://blog.csdn.net/tabactivity/article/details/49685319



### <span id="head6"> **4、Cookie、Session、webStorage**</span>

**会话（Session）**跟踪是Web程序中常用的技术，用来**跟踪用户的整个会话**。常用的会话跟踪技术是Cookie与Session。**Cookie通过在客户端记录信息确定用户身份**，**Session通过在服务器端记录信息确定用户身份**。

**Cookie**

由于HTTP是一种无状态的协议，服务器单从网络上无从知道客户身份。于是服务器就给客户端颁发一个凭证，每个客户端一个，无论谁访问都需要携带这个凭证，这样就可以从这个凭证上确认客户端（也就是客户）的信息了。这就是Cookie的工作原理

Cookie实际上是一小段文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie；客户端浏览器会把Cookie保存起来，当浏览器再请求该网站时，浏览器把请求的网址连同该Cookie一同提交给服务器，服务器检查该Cookie，以此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。

Cookie的内容主要包括：名字、值、过期时间、路径和域。路径与域一起构成Cookie的作用范围。

Cookie的属性maxAge为正数时，表示该Cookie在maxAge秒后失效；如果为负数，该Cookie为临时Cookie，关闭浏览器即失效；如果为0，表示删除Cookie。默认为-1。

* ***Cookie的不可跨域名性***

  浏览器判断一个网站是否能操作一个网站的Cookie的依据是域名，如果域名不一样，则不能操作该Cookie。

* ***Cookie的修改删除***

  Cookie并不提供修改、删除操作。如果要修改某个Cookie，只需要新建一个同名的Cookie，添加到response中覆盖原来的Cookie。

  如果要删除某个Cookie，只需要新建一个同名的Cookie，并将maxAge设置为0，并添加到response中覆盖原来的Cookie。

**Session**

Session是服务器端使用的一种记录客户端状态的机制，使用上比Cookie简单一些，相应的也增加了服务器的存储压力。也就是说，Cookie是保存在客户端浏览器中，而Session是保存在服务器上的。

使用Session时，当客户端浏览器访问服务器时，服务器把客户端信息以某种形式记录在服务器上；当客户端浏览器再次访问时，只需要从该Session中查找该客户的状态就可以了。

如果说Cookie机制是通过检查客户身上的“通行证”来确定客户身份的话，那么Session机制就是通过检查服务器上的“客户明细表”来确认客户身份。

* ***Session的生命周期***

  服务器一般把Session放在内存里，每个用户都会有一个独立的Session，如果Session内容过于复杂，当大量客户访问服务器时可能会导致内存溢出。因此，Session里的信息应尽量精简。

  Session在用户第一次访问服务器的时候自动创建。并且只有访问JSP、Servlet等程序时才会创建Session，只访问HTML、IMAGE等静态资源并不会创建Session。如果尚未生成Session，也可以使用request.getSession(true)强制生成Session。

  Session生成后，只要用户继续访问，服务器就会更新Session的最后访问时间，并维护该Session。用户每访问服务器一次，无论是否读写Session，服务器都认为该用户的Session“活跃（active）”了一次。

* ***Session对浏览器的要求***

  HTTP协议是无状态的，Session不能依据HTTP连接来判断是否为同一客户，因此服务器向客户端浏览器发送一个名为JSESSIONID的Cookie，它的值为该Session的ID。Session根据该Cookie来识别是否为同一用户。

  如果浏览器禁用了Cookie则采用URL重写的方式实现Session，即在URL后添加sid=xxxx等信息。

**Cookie和Session的区别**

* Cookie数据存放在客户端的浏览器上，Session数据放在服务器上

  Session是由应用服务器维持的一个服务器端的存储空间，用户在连接服务器时，会由服务器生成一个唯一的SessionID，用该SessionID为标识符来存取服务器端的Session存储空间。而SessionID这一数据则是用Cookie保存在客户端。

* Cookie不是很安全，别人可以分析存放在本地的Cookie并进行Cookie欺骗，考虑到安全应当使用Session
* 设置Cookie时间可以使Cookie过期，但是使用session-detroy()我们将会销毁会话
* Session会在一定时间内保存在服务器上，当访问增多，会比较占用服务器的性能
* 单个Cookie保存的数据不能超过4k，Session对象没有对存储数据量的限制，可以保存更复杂的数据类型。
* Cookie中保存的是字符串，Session中保存的是对象
* Session不能区分路径，同一个用户在访问一个网站期间，所有的Session在任何一个地方都可以访问到；而Cookie中如果设置了路径参数，那么同一个网站中不同路径下的Cookie是访问不到的

**web Storage**

HTML5中与本地存储相关的两个重要内容：Web Storage与本地数据库。其中，Web  Storage存储机制是对HTML4中cookie存储机制的一个改善。由于cookie存储机制有很多缺点，HTML5不再使用它，转而使用改良后的Web  Storage存储机制。本地数据库是HTML5中新增的一个功能，使用它可以在客户端本地建立一个数据库，原本必须保存在服务器端数据库中的内容现在可以直接保存在客户端本地了，这大大减轻了服务器端的负担，同时也加快了访问数据的速度。

Web Storage的概念和cookie相似，区别是它是为了更大容量存储设计的。cookie的大小是受限的，并且每次请求一个新的页面的时候cookie都会被发送过去，这样无形中浪费了带宽，另外cookie还需要指定作用域，不可跨域调用，要正确的操纵Cookie是很困难的。

HTML5重新提供了一种在客户端本地保存数据的功能：Web Storage。Web Storage的两个主要目标为：（1）提供一种在cookie之外存储会话数据的路径；（2）提供一种存储大量可以跨会话存在的数据的机制。Web Storage又分为两种：

* sessionStorage（会话存储）：将数据保存在Session对象中。所谓Session，是指用户在浏览某个网站时，从进入网站到浏览器关闭所经过的这段时间，也就是用户浏览这个网站所花费的时间。Session对象可以用来保存在这段时间内所要求保存的任何数据。sessionStorage引入了一个“浏览器窗口”的概念，sessionStorage是在同源的窗口中始终存在的数据。只要这个浏览器窗口没有关闭，即使刷新页面或者进入同源另一个页面，数据依然存在。但是sessionStorage在关闭了浏览器窗口后就会被销毁。同时独立的打开同一个窗口同一个页面，sessionStorage也是不一样的。（临时保存）
* localStorage（本地存储）：将数据保存在客户端本地的硬件设备（通常指硬盘，也可以是其他硬件设备）中，即使浏览器被关闭了，该数据仍然存在，下次打开浏览器访问网站时仍然可以继续使用。（永久保存）

两种Web Storage的说明：

* 存储大小：二者存储大小一般都是5MB
* 存储位置：二者都保存在客户端，不与服务器进行交互通信
* 存储内容类型：二者只能存储字符串类型，对于复杂对象可以使用JSON对象的stringify和parse来处理
* 获取方式：
  * localStorage：window.localStorage；
  * sessionStorage：window.sessionStorage
* 应用场景：
  * localStorage：常用于长期登录（+判断用户是否已登录），适合长期保存在本地的数据
  * sessionStorage：敏感账号一次性登录
* 保存数据
  * sessionStorage：
    * sessionStorage.setItem("key", "value");
    * sessionStorage.key = value;
  * localStorage:
    * localStorage.setItem("key", "value");
    * localStorage.key = value;
* 读取数据
  * sessionStorage：
    * value = sessionStorage.getItem("key");
    * value = sessionStorage.key;
  * localStorage：
    * value = localStorage.getItem("key");
    * value = localStorage.key;

Web Storage的优点：

* 存储空间更大：cookie为4kb，WebStorage是5MB
* 节省网络流量：WebStorage不会传送到服务器，存储到本地的数据可以直接获取，也不会像cookie一样每次请求都会传送到服务器，所以减少了客户端和服务器端的交互，节省了网络流量。
* 对于那种只需要在用户浏览一组页面期间保存而关闭浏览器后就可以丢弃的数据，sessionStorage会非常方便；
* 快速显示：有的数据存储在WebStorage上，再加上浏览器本身的缓存。获取数据时可以从本地获取会比从服务器端获取快得多，所以速度更快
* 安全性：WebStorage不会随着HTTP header发送到服务器端，所以安全性相对于cookie来说比较高一些，不会担心截获，但是仍然存在伪造问题

**Cookie、sessionStorage与localStorage的区别**

<table style="text-align:center; ">
    <tr>
    	<td style="text-align:center; font-weight:bold;">特性</td>
        <td style="text-align: center; font-weight:bold;">cookie</td>
        <td style="text-align:center; font-weight:bold;">sessionStorage</td>
        <td style="text-align:center; font-weight:bold;">localStorage</td>
    </tr>
	<tr>
    	<td style="text-align:center; font-weight:bold;">数据生命期</td>
        <td>生成时就会被指定一个maxAge值，这就是cookie的生存周期，在这个周期内cookie有效，默认关闭浏览器失效</td>
        <td>页面会话期间可用</td>
        <td>除非数据被清除，否则一直存在</td>
    </tr>
    <tr>
    	<td style="text-align:center; font-weight:bold;">存放数据大小</td>
        <td>4K左右（因为每次http请求都会携带cookie）</td>
        <td colspan="2">一般5M或更大</td>
    </tr>
    <tr>
    	<td style="text-align:center; font-weight:bold;">与服务器通信</td>
        <td>由对服务器的请求来传递，每次都会携带在HTTP头中，如果使用cookie保存过多的数据会带来性能问题</td>
        <td colspan="2">数据不是由每个服务器请求传递的，而是只有在请求时使用数据，不参与和服务器的通信</td>
    </tr>
    <tr>
    	<td style="text-align:center; font-weight:bold;">易用性</td>
        <td>cookie需要自己封装setCookie，getCookie</td>
        <td colspan="2">可以用原生接口，也可以再次封装来对Object和Array有更好的支持</td>
    </tr>
    <tr>
        <td style="text-align:center; font-weight:bold;">共同点</td>
    	<td colspan="3">都是保存在浏览器端，和服务器端的session机制不同</td>
    </tr>
</table>



*参考*：

https://www.cnblogs.com/l199616j/p/11195667.html#_label0_8

https://www.cnblogs.com/jing-tian/p/10991431.html

https://blog.csdn.net/jiangnanqbey/article/details/81709322



### <span id="head7"> **5、TCP和UDP**</span>

* **TCP（Transmission Control Protocol）传输控制协议**

  面向连接的、可靠的、基于字节流的传输层协议。

  * 面向连接：TCP三次握手、四次挥手
  * 可靠传输：序列号、超时重传、拥塞控制
  * 面向字节流：
    * 创建一个TCP的socket，同时在内核中创建一个发送缓冲区和一个接收缓冲区；
    * TCP的一个连接，既有发送缓冲区也有接收缓冲区；
    * 传输的两端既可以作为发送方又可以作为接收方，全双工传输。、
  * 协议：HTTP（超文本传输协议）、HTTPS（加密超文件传输协议）、SSH（安全外壳协议；远程登录会话）、Telnet（远程终端协议；远程终端）、FTP（文件传输协议）、SMTP（简单邮件传输协议）

* **UDP（User Datagram Protocl）用户数据报协议**

  * 无连接：只要知道对端的IP和端口号就可以直接进行传输
  * 不可靠：没有确认机制，没有重传机制
  * 面向数据报：应用层交给UDP多长的报文，UDP原样发送，超过长度需要在应用层分包，因为无法保证包序，需要在应用层编号
  * 协议：NFS（网络文件系统；远程服务器）、TFTP（简单文件传输协议；文件传送）、DHCP（动态主机配置协议；IP地址配置）、BOOTP（启动协议；无盘设备启动）、DNS（域名解析协议；域名转换）、SNMP（简单网络管理协议；网络管理）、RIP（路由信息协议；路由器选择协议）、IGMP（网际组管理协议；多播）



### <span id="head8"> **6、Web前端性能优化常见方法**</span>



### <span id="head9"> **7、跨域**</span>



## <span id="head10"> **JavaScript**</span>

### <span id="head11"> **1、垃圾回收机制**</span>

