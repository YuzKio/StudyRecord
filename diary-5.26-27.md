- [ 面经](#head1)
  - [ JavaScript](#head2)
    - [ 1、浏览器的事件代理和事件传递步骤？](#head3)
    - [ 2、浏览器的渲染机制？](#head4)
    - [ 3、this在函数里的具体含义？](#head5)
    - [4、箭头函数进行apply调用，this会是什么？即声明了一个箭头函数，再调用这个箭头函数，传入一个object，此时的this是什么？可以用apply改掉箭头函数的this吗？ ](#head6)
  - [ 网络](#head7)
    - [ 1、协商缓存？强缓存？](#head8)
    - [ 2、http2.0新特性](#head9)
    - [4、XSS CSRF？](#head10)
- [ 算法](#head11)
  - [哈希表的存储](#head12)
  - [ 快速排序](#head13)
- [ 前端学院](#head14)
  - [ 做一个在线简历（CSS篇1）](#head15)
  - [ CSS如何工作](#head16)
  - [ CSS选择符](#head17)

# <span id="head1"> 面经</span>

## <span id="head2">JavaScript</span>

### <span id="head3">1、浏览器的事件代理和事件传递步骤？</span>

* **事件**

  JavaScript与HTML的交互式通过事件实现的，事件代表文档或浏览器窗口中某个有意义的时刻。即在DOM中，操作对应的HTML元素时，会触发相应事件（包含事件源、事件名以及对应的事件回调函数）。

* **事件流**

  事件流描述了页面接收事件的顺序。用红宝书里面的例子就是，当点击页面中的一个按钮时，点击的不光是这个按钮，还有这个按钮的容器以及整个页面。

  另一个解释（其实是一个意思，详细一点说而已）：DOM结构是一个树型结构，当一个HTML元素产生一个事件时，该事件会在元素结点与根结点之间的路径传播，路径所经过的结点都会收到该事件，这个传播过程可称为DOM事件流。

  事件流的实现方式：冒泡事件（event bubbling）、事件捕获（event capturing）。

* **事件传递**

  DOM2级事件把事件流分为三个阶段：捕获阶段、目标阶段、冒泡阶段。

  * 事件捕获阶段。即由最顶层元素，逐次进入dom内部，最后到达目标元素，依次执行绑定在其上的事件。（由外向内依次执行事件）
  * 目标阶段。检测机制到达目标元素，按事件注册顺序执行绑定在目标元素上的事件。
  * 事件冒泡阶段。从目标元素出发，向外层元素冒泡，最后到达顶层（window或document），依次执行绑定再其上的事件。（由内向外依次执行事件）

  DOM事件流中，实际的目标在捕获阶段不会接收到事件。这是因为捕获阶段从document开始到目标元素的上一个元素时就结束了。下一阶段，即会在目标元素上触发事件的到达目标阶段，通常在事件处理时被认为是冒泡阶段的一部分。

  addEventListener时默认false是冒泡，true是捕获。

* **事件代理**

  现在的网站有大量互动，如果通过事件监听一个一个去写，除了效果差，写起来也麻烦。事件代理就是给祖先元素绑定事件，操作后代元素时，会利用事件流的原理触发祖先元素的事件。事件代理是基于事件冒泡。作用是避免给过多的子元素添加同一事件，影响性能；后期新添加的子元素也能触发事件。

  简单来说，由于事件传递的机制，子元素的事件在传递过程中势必会经过它的父元素。事件代理就是将子元素事件监听器交由父元素代理。

  优点：

  ​	1、大量节省内存占用，减少事件注册。

  ​	2、可以实现当新增子对象时，无需再对其进行事件绑定，对于动态内容部分尤为合适。

  缺点：

  ​	所有事件都用事件代理，可能会出现事件误判。

  一个例子：

  ```html
  <button id="push">push</button>
  <button id="pop">pop</button>
  <ul id="list"></ul>
  ```

  没有事件代理的情况：每个`li`上都注册了事件监听器。

  ```javascript
  (function() {
    document.querySelector('#push').addEventListener('click', pushHandler)
    document.querySelector('#pop').addEventListener('click', popHandler)
  
    const list = document.querySelector('#list')
  
    function pushHandler() {
      list.appendChild(getNewElem(list.childNodes.length))
    }
  
    function popHandler() {
      document.querySelectorAll('#list>li')[list.childNodes.length - 1].remove()
    }
  
    function getNewElem(text) {
      const elem = document.createElement('li')
      elem.innerText = text
      elem.addEventListener('click', eventHandler)
      return elem
    }
    
    function eventHandler(e) {
      alert(e.target.innerText)
    }
  })()
  ```

  有事件代理的情况：事件监听器注册在了外层的`ul`上，无论内容又多少，浏览器都只需要承担一组事件监听器的消耗。

  ```javascript
  (function() {
    document.querySelector('#push').addEventListener('click', pushHandler)
    document.querySelector('#pop').addEventListener('click', popHandler)
  
    const list = document.querySelector('#list')
    
    list.addEventListener('click', listClickHandler)
    
    function pushHandler() {
      list.appendChild(getNewElem(list.childNodes.length))
    }
  
    function popHandler() {
      document.querySelectorAll('#list>li')[list.childNodes.length - 1].remove()
    }
  
    function getNewElem(text) {
      const elem = document.createElement('li')
      elem.innerText = text
      return elem
    }
    
    function listClickHandler(e){
      if (e.target.tagName === 'LI') alert(e.target.innerText)
    }
  })()
  ```



*Vue中的事件监听是怎么样的？*



*参考*：

https://blog.csdn.net/qq_43004614/article/details/91040173

https://cloud.tencent.com/developer/article/1739042

https://github.com/YvetteLau/Step-By-Step/issues/20



### <span id="head4">2、浏览器的渲染机制？</span>

* **基本概念**

  * DOM：浏览器将HTML解析成树型的数据结构

  * CSSOM：浏览器将CSS解析成树型的数据结构

  * Render Tree：DOM和CSSOM合并后生成Render Tree

    ![img](https://upload-images.jianshu.io/upload_images/13387321-e29326c79d4fba4c.png?imageMogr2/auto-orient/strip|imageView2/2/w/600)

  * Layout：计算出Render Tree每个节点的具体位置

  * Painting：通过显卡，将Layout后的节点内容分别呈现到屏幕上。

* **注意事项**

  ***！前两点看到了不一样的说法，准备花时间去阅读资料求证一下，先留存记录问题！***

  * ~~当浏览器获得HTML文件后，会自上而下加载，并在加载过程中进行解析和渲染。~~
  * ~~加载说的是获取文件的过程，如果在加载过程中遇到外部CSS文件和图片，浏览器会另外发送一个请求，去获取CSS文件和相应的图片，这个请求是异步的，并不会影响HTML文件的加载。~~
  * 但是如果遇到JavaScript，HTML文件会挂起渲染的进程，等待JavaScript文件加载完毕后再继续进行渲染。因为JavaScript可能会修改DOM，导致后续HTML资源白白加载，所以HTML必须等待JavaScript文件加载完毕后再继续渲染。

* **浏览器渲染流程**

  ![img](https://upload-images.jianshu.io/upload_images/13387321-d87d75e05f6ac01f.png?imageMogr2/auto-orient/strip|imageView2/2/w/409)

  * 当用户输入URL后，浏览器就会向服务器发出请求，请求URL所对应的资源
  * 接收到服务器的相应内容后，浏览器的HTML解析器会将HTML文件解析成一刻DOM树。（深度遍历）
  * 将CSS解析为CSSOM树
  * 根据DOM树和CSSOM树构建Render Tree。渲染树并不等于DOM树，`display:none`没必要放在渲染树中
  * 渲染树告知了浏览器网页中有哪些节点、每个节点的CSS定义以及它们之间的从属关系。此后进行Layout，即计算每个节点在屏幕中哪个位置。
  * Layout后，进行painting，按照计算出来的规则，通过显卡把内容显示到屏幕上。

* **Reflow和Repaint**

  * Repaint：改变某个元素的背景色、文字颜色、边框颜色等不影响它周围或是内部布局的属性时，屏幕的一部分要重画，但是元素的几何尺寸没有改变。
  * Reflow：元素的几何尺寸变了，需要重新验证并计算Render Tree。
  * reflow 几乎是无法避免的。现在界面上流行的一些效果，比如树状目录的折叠、展开（实质上是元素的显 示与隐藏）等，都将引起浏览器的 reflow。鼠标滑过、点击……只要这些行为引起了页面上某些元素的占位面积、定位方式、边距等属性的变化，都会引起它内部、周围甚至整个页面的重新渲染。通常我们都无法预估浏览器到底会 reflow 哪一部分的代码，它们都彼此相互影响着。
    *注*：display:none会触发reflow，而visibility:hidden只会触发repaint，因为没有发生位置变化。

*参考*：

https://www.jianshu.com/p/05eb1b17b298

https://www.jianshu.com/p/c9049adff5ec



### <span id="head5">3、this在函数里的具体含义？</span>

普通函数this值由“调用它所使用的引用”决定，即同一个函数调用方式不同，得到的this值也不同（获取函数的表达式时实际上返回的并非函数本身，而是一个*Reference类型*）

一句话说明：谁调用它，this就指向谁。

* **普通函数**（this指向window）默认绑定；严格模式下会抛出错误undefined

* **对象函数**：this指向该方法所属对象

* **构造函数**：如果没有return，则this指向这个对象实例；如果存在return返回一个对象，则this指向返回的这个对象。

* **绑定事件函数**：this指向的是函数的调用者，指向了接收事件的HTML元素

  ```javascript
  var btn = document.querySelector('button');
  btn.onclick = function () {
      console.log(this); // btn <button>点击</button>
  }
  ```

* **定时器函数**：this指向window

* **立即执行函数**：this指向window

* **箭头函数**：不绑定this关键字，指向的是函数定义位置的上下文this

* **显式绑定**：函数通过call()、apply()调用，bind()方法绑定，this指向的就是指定的对象

  ```javascript
  function fun() {
  	console.log(this.age);
  }
  var person = {
  	age: 20,
  	fun
  }
  var age = 28;
  var fun = person.fun;
  fun.call(person);   //20
  fun.apply(person);  //20
  fun.bind(person)(); //20
  ```

  如果这些方法传入的第一个参数是undefined或者null，严格模式下this指向为传入的值undefined/null；非严格模式下指向window：

  ```JavaScript
  function fun() {
  	console.log(this.age);
  }
  var person = {
  	age: 20,
  	fun
  }
  var age = 28;
  var fun = person.fun;
  fun.call(null);   //28
  ```

* **隐式绑定**：函数的调用是在某个对象上触发的，即调用位置上存在上下文对象（相当于对象函数中的this指向）。典型的隐式调用为：xxx.fn()

  ```javascript
  function fun() {
  	console.log(this.age);
  }
  var person = {
  	age: 20,
  	fun
  }
  var age = 28;
  person.fun(); //20 隐式绑定
  ```

  

### <span id="head6">4、箭头函数进行apply调用，this会是什么？即声明了一个箭头函数，再调用这个箭头函数，传入一个object，此时的this是什么？可以用apply改掉箭头函数的this吗？ </span>



## <span id="head7">网络</span>

### <span id="head8">1、协商缓存？强缓存？</span>

* **浏览器缓存**

  浏览器将用户请求过的静态资源（html、css、js）存储到电脑本地磁盘中，当浏览器再次访问时，就可以直接从本地加载而无需到服务端请求。

  优点：

  - 减少了不必要的数据传输，节省带宽
  - 减少服务器的负担，提升网站性能
  - 加快了客户端加载网页的速度
  - 用户体验友好

* **强缓存**

  强是强制的意思。当浏览器去请求某个文件的时候，服务端就在respone header里面对该文件做了缓存配置。缓存的时间、缓存类型都由服务端控制，具体表现为respone header的cache-control，常见的设置是max-age public private no-cache no-store等。

  * max-age表示缓存的时间
* public表示可用被浏览器和代理服务器缓存
  * immutable表示该资源永远不变，这么设置的意思是为了让用户在刷新页面的时候不要去请求服务器。就是说，public+immutable的话，用户就算刷新页面，浏览器也不会向服务器发起请求，而是直接从本地磁盘或者内存中读取缓存并返回200状态。
* 总结：
  
  * cache-control: max-age=xxxx，public
       客户端和代理服务器都可以缓存该资源；
     客户端在xxx秒的有效期内，如果有请求该资源的需求的话就直接读取缓存，statu code:200 ，如果用户做了刷新操作，就向服务器发起http请求
    * cache-control: max-age=xxxx，private
       只让客户端可以缓存该资源；代理服务器不缓存
       客户端在xxx秒内直接读取缓存,statu code:200
  * cache-control: max-age=xxxx，immutable
       客户端在xxx秒的有效期内，如果有请求该资源的需求的话就直接读取缓存，statu code:200 ，即使用户做了刷新操作，也不向服务器发起http请求
    * cache-control: no-cache
       跳过设置强缓存，但是不妨碍设置协商缓存；一般如果你做了强缓存，只有在强缓存失效了才走协商缓存的，设置了no-cache就不会走强缓存了，每次请求都回询问服务端。
  * cache-control: no-store
       不缓存，这个会让客户端、服务器都不缓存，也就没有所谓的强缓存、协商缓存了。
  * 强缓存步骤：
   * 第一次请求a.js，缓存表中没有该信息，直接请求后端服务器；
     * 后端服务器返回了a.js，且http response header中cache-control为max-age=xxx，所以是强缓存规则，存入缓存表中；
     * 第二次请求a.js，缓存表中时max-age，那么命中强缓存，然后判断是否过期。如果没过期直接读缓存的a.js；如果过期了，则执行协商缓存的步骤。

* **协商缓存**

  强缓存就是给资源设置一个过期时间，客户端每次请求资源时都会看是否过期；只有过期才会去询问服务器。response header中设置：etag，last-modified。协商缓存的触发条件：Cache-Control的值为no-cache（不强缓存）或者max-age过期了（强缓存，但总有过期的时候）。
  
  * etag：每个文件有一个，改动文件了就变了，是个文件hash，每个文件唯一。类似于用webpack打包时，每个资源都会有一个文件hash，如：app.js打包后变为app.c20abbde.js，即多了一个唯一hash，是为了解决缓存问题。
  * last-modified：文件修改的时间，精确到秒。
  
  简单来说，每次请求都返回etag和last-modified，在下次请求时带上，服务器端根据其进行对比，判断资源是否更改。如果更改直接返回新资源，更新对应的response header的标识etat和last-modified。如果资源不变，那就不改变两个标识。
  
  协商缓存的过程（资源没过期）：发请求——看资源是否过期——过期——请求服务器——服务器对比资源是否真的过期——没过期——返回304状态码——客户端用缓存的老资源
  
  协商缓存的过程（资源过期）：发请求——看资源是否过期——过期——请求服务器——服务器对比资源是否真的过期——过期——返回200状态码——客户端如第一次接收该资源一样，记下cache-control中的max-age、etag、last-modified

* **为什么需要Etag？**

  * 一些文件也许会周期性修改，但内容可能并不改变，只有修改时间发生改变，这时候Etag可以避免客户端重新GET资源。
  * 某些文件修改非常频繁，如果修改的频率小于浏览器（If-Modified-Since）能检查到的粒度，比如说文件在秒以下的时间内进行了修改，但是浏览器能记录的修改时间只能精确到秒。
  * 某些服务器不能精确的得到文件最后修改时间。

* **用户行为对缓存的影响**

  ![img](https://images2015.cnblogs.com/blog/408483/201605/408483-20160525202949975-1541314356.png)

  F5会跳过强缓存规则，直接走协商缓存。Ctrl+F5跳过所有缓存规则，和第一次请求一样，重新获取资源。

* **强缓存如何重新加载缓存缓存过的资源**

  使用强缓存时，浏览器不会发送请求到服务端，根据设置的缓存时间浏览器一直从缓存中获取资源，如果在这期间资源发生了变化，为了防止浏览器在缓存期内一直得不到最新的资源，可以通过更新页面中引用的资源路径，让浏览器主动放弃缓存，重新加载资源。

* **总结**

  <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/244a7d5cf07f421ba9d4e3dbb4a27bf4~tplv-k3u1fbpfcp-zoom-1.image" alt="img" style="zoom:67%;" />

*参考*：

https://www.cnblogs.com/wonyun/p/5524617.html

https://juejin.cn/post/6844903763665240072

https://www.cnblogs.com/ziyunfei/p/5642796.html

### <span id="head9">2、http2.0新特性</span>

* **http**

  一种超文本传输协议，是客户端与服务端之间请求和应答的标准，通常会使用TCP协议。

* **http2.0**

  解决HTTP1.0+协议存在的问题，并且提高网络传输性能、优化网络传输过程。

  * ***二进制分帧***

    二进制分帧可以保证HTTP的各种动词、方法、首部都不受影响，又能突破上一代标准的性能限制，改进传输性能，实现低延迟和高吞吐量。做法是在应用层和传输层之间增加一个二进制分帧层。

    在二进制分帧层上，HTTP2.0会将所有传输的信息分割为更小的消息和帧，并对它们采用二进制格式的编码，其中HTTP1.x的首部信息会被封装到Headers帧，而request body则封装到Data帧里。

    这样在建立连接的时候，就可以承载任意数量的双向数据流，每一个数据流都以消息的形式发送；消息由一个或多个帧组成，可乱序发送。每个帧首部都会有一个标识位，接收到之后就可以重装。这样就解决了HTTP1.0中一应一答的低效率模式，能够有效提高传输效率，连接吞吐量更大且内存占用更少。

  * ***多路复用***

    HTTP 1.0的模式是，建立连接请求数据完毕之后就立即关闭连接；后来采用了keep-alive保活模式使得可以复用连接不断开，可以利用这次连接继续请求数据。但是始终会有一个缺点，就是你必须等待服务器返回上一次的请求数据你才可以进行下一次的请求。

    HTTP 2.0提出了多路复用的技术，就是你可以连续发送多个请求，可以不用收到回复就继续发送请求。

    优点：

    * 并行交错发送请求，请求之间互不影响
    * TCP连接一旦建立可以并行发送请求
    * 消除不必要延迟，减少页面加载时间
    * 可以最大程度利用HTTP1.x

  * ***首部压缩***

    首部压缩可以使得头部帧可以最大程度复用，减少头部的大小，有利于减少内存和流量。比如我们第一次发送请求，里面包含头部的各种信息；但是后来我们又发送另外的请求，发现大部分的字段是可以复用的，我们只要发送一个当前请求特有的头部帧即可。由于首部表在HTTP 2.0 的连接存续期内始终是有效的，客户端和服务端共同更新。

  * ***流量控制***

    HTTP2.0“流”的流量控制最终的目标是在不改变协议的情况之下允许采用多种流量控制算法。

    流量控制特点：

    * 流量基于HTTP连接的每一跳进行，非端到端控制
    * 流量基于窗口更新帧进行，接收方可广播准备接收字节数甚至对整个连接要接收的字节数
    * 流量控制有方向性，接收方可以根据自身情况进行控制窗口大小
    * 流量控制可以由接收方禁用，包括个别流和整个连接
    * 只有DATA帧服从流量控制，其他类型帧不会消耗控制窗口的空间

  * ***请求优先级***

  * ***服务器推送***

    一般HTTP请求都是由客户端发起，服务器收到请求进行返回。但是HTTP 2.0 可以使服务器主动返回资源给客户端用户。比如前端请求 /index.html 资源，但服务器把 /index.css ， index.png 都返回了。这样就可以提高性能。

    服务器推送工作过程：

    * PUSH_PROMISE帧是服务端有意向客户端推送资源
    * PUSH_PROMISE帧只包含预推送资源的首部。如果客户端对此帧没有意见，服务端就会发送DATA帧响应。假如客户端缓存了可以拒绝推送。
    * 服务器遵守同源策略，不会随意推送第三方资源。

  *参考*：

  https://zhuanlan.zhihu.com/p/110993022



### <span id="head10">3、XSS CSRF？</span>

* **XSS(Cross Site Scripting)跨站脚本攻击**

  恶意攻击者往Web页面里嵌入恶意的客户端脚本（Script代码），当用户浏览此网页时，脚本就会在用户的浏览器上执行，从而达到攻击者的目的，比如：获取用户的Cookie、导航到恶意网站、携带木马等。

  XSS是用户过分信任网站，放任来自浏览器地址栏代表的那个网站代码在自己本地任意执行。如果没有浏览器的安全机制限制，XSS代码可以在用户浏览器为所欲为。

  XSS有以下三种分类：

  * Reflected XSS（基于反射的XSS攻击）：是指XSS代码在请求的URL中，而后提交到服务器，服务器解析后，XSS代码随着响应内容一起传给客户端进行解析执行。（直接反射显示在页面）
  * Stored XSS（基于存储的XSS攻击）：Stored XSS和Reflected XSS的差别在于，具有攻击性的脚本被保存到了服务器端（数据库、内存、文件系统）并且可以被普通用户完整的从服务取得并执行，从而获得了在网上传播的能力。
  * DOM-based or local XSS（基于DOM或本地的XSS攻击）：DOM型XSS是一种特殊类型的反射型XSS，它是基于DOM文档对象模型的一种漏洞。可以通过DOM来动态修改页面内容，从客户端获取DOM中的数据并在本地执行。

* **CSRF（Cross-site Request Forgery）跨站请求伪造**

  与XSS相同，它们都是不攻击服务器端而攻击正常访问网站的用户，但它们的攻击类型是不同维度上的分类。CSRF是伪造请求，冒充用户在站内的正常操作。我们知道绝大多数网站是通过cookie等方式识别用户身份（包括使用服务器端Session的网站，因为Session ID也是大多保存在cookie里面的），再予以授权的。所以要伪造用户的正常操作，最好的方法是通过XSS或链接欺骗等途径，让用户在本机（即拥有身份cookie的浏览器端）发起用户所不知道的请求。

  CSRF是网站过分新人用户，放任来自所谓通过访问控制机制的代码合法用户的请求执行网站的某个特定功能。

***这部分还是不是很懂qwq之后再看看吧***

*参考*：

https://blog.csdn.net/zl834205311/article/details/81773511

https://www.jianshu.com/p/64a413ada155

https://www.zhihu.com/question/34445731



# <span id="head11">算法</span>/数据结构

## <span id="head12">哈希表的存储</span>

哈希表是一种用空间换时间的存储结构，它能够通过给定的关键字直接访问到具体对应的值的一个数据结构。也就是说，把挂件自映射到一个表中的位置来直接访问记录，以加快访问速度。

通常把关键字称为Key，对应的记录称作Value，通过Key访问一个映射表来得到Value的地址，这个映射表就叫做哈希函数，存放记录的数组叫做哈希表。

* **几种哈希函数：**
  * 直接寻址法
  * 数字分析法
  * 平方取中法
  * 取随机数法
  * 除留取余法
* **哈希函数产生冲突的解决办法：**
  * 开放地址法
  * 再哈希法：用关键字的其他部分继续计算地址
  * 链地址法：对Key通过哈希之后落在同一个地址上的值做一个链表。
  * 建立一个公共溢出区：这种方式是建立一个公共溢出区，当地址存在冲突时，把新的地址放在公共溢出区里。
* **哈希表的特点**：
  * 访问速度很快
  * 需要额外的空间
  * 无序
  * 可能会产生碰撞
* **哈希表的应用场景**：
  * 缓存
  * 快速排序：不是排序，而是在集合中找出是否存在指定的元素。



*参考*

http://data.biancheng.net/view/107.html



## <span id="head13">快速排序</span>

**基本思路**：

1、先从数列中取出一个数作为基准数

2、分区过程，将比这个数大的数全放到它的右边，小于或等于它的数劝放到它的左边

3、再对左右区间重复第二步，直到各区间只有一个数

***（一）***

```javascript
function quickSortTemplate (array) {
    var tmp_array = array.slice(0), result;
    var quickSort = function (arr) {
        if (arr.length <= 1) { return arr; }
        var pivotIndex = Math.floor(arr.length / 2);
        var pivot = arr.splice(pivotIndex, 1)[0]; // splice把pivot删掉了，arr的长度有变化
        var left = [];
        var right = [];
        for (var i = 0; i < arr.length; i ++) {
            if(arr[i] < pivot) left.push(arr[i]);
            else right.push(arr[i]);
        }
        return quickSort(left).concat([pivot], quickSort(right));
    }
    result = quickSort(tmp_array);
    return result
}
```

**（二）**

```javascript
function advanceQuickSortTemplate(array) {
    var tmp_array = array.slice(0);
    var result;
    var low = 0;
    var high = array.length - 1;
    var quickSort = function (arr, low, high) {
        if (high <= low) { return arr; }
        var mid = Math.floor((low + high) / 2);
        var i = low, j = high;
        while (i <= j) {
            while (arr[i] < arr[mid]) {
                i ++;
            }
            while (arr[j] > arr[mid]) {
                j --;
            }
            if (i <= j) {
                var tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i ++;
                j --;
            }
        }
        return i;
    } 
    var quickSortExecute = function (arr, low, high) {
        if (arr.length <= 1) { return arr; }
        var pivotIndex = quickSort(arr, low, high);
        if (low < pivotIndex) {
            quickSortExecute(arr, low, pivotIndex - 1);
        }
        if (high > pivotIndex) {
            quickSortExecute(arr, pivotIndex, high);
        }
        return arr;
    }
    result = quickSortExecute(tmp_array, low, high);
    return result;
}
```



# <span id="head14">前端学院</span>





Codepen：https://codepen.io/yuzkio/pen/QWpvoww

* CSS font的简写规则

  字体属性主要包括下面几个：font-family，font-style（normal、italic、oblique），font-variant（normal、small-caps），font-weight，font-size，font

  **顺序**：font-style | font-variant | font-weight | font-size/line-height | font-family



## <span id="head16">CSS如何工作</span>

不同浏览器处理文件时候的步骤：

* 浏览器载入HTML文件（比如从网络上获取）

* 将HTML文件转化成一个DOM（Document Object Model），DOM是文件在计算机内存中的表现形式

* 接下来，浏览器会拉取该HTML相关的大部分资源，比如嵌入到页面的图片、视频和CSS样式。JavaScript则会稍后进行处理

* 浏览器拉取到CSS之后会进行解析，根据选择器的不同类型（比如element、class、id等等）把他们分到不同的“桶”中。浏览器基于它找到的不同的选择器，将不同的规则（基于选择器的规则，如元素选择器、类选择器、id选择器等）应用在对应的DOM的节点中，并添加节点依赖的样式（这个中间步骤称为渲染树）

* 上述的规则应用于渲染树之后，渲染树会依照应该出现的结构进行布局

* 网页展示在屏幕上（这一步被称为着色）

  ![img](https://mdn.mozillademos.org/files/11781/rendering.svg)



## <span id="head17">CSS选择符</span>

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