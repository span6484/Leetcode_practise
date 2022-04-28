### HTTP/1.1 和 HTTP/1.0 的区别

主要区别如下：

**缓存处理**：在 HTTP/1.0 中主要使用 header 里的 if-modified-Since, Expries 来做缓存判断的标准。而 HTTP/1.1 请求头中添加了更多与缓存相关的字段，从而支持更为灵活的缓存策略，例如 Entity-tag, If-Unmodified-Since, If-Match, If-None-Match 等可供选择的缓存头来控制缓存策略。
**节约带宽**： 当客户端请求某个资源时，HTTP/1.0 默认将该资源相关的整个对象传送给请求方，但很多时候可能客户端并不需要对象的所有信息。而在 HTTP/1.1 的请求头中引入了 **range** 头域，它允许只请求部分资源，其使得开发者可以多线程请求某一资源，从而充分的利用带宽资源，实现高效并发。
**错误通知的管理**：HTTP/1.1 在 1.0 的基础上新增了 24 个错误状态响应码，例如 414 表示客户端请求中所包含的 URL 地址太长，以至于服务器无法处理；410 表示所请求的资源已经被永久删除。
**Host 请求头：**早期 HTTP/1.0 中认为每台服务器都绑定一个唯一的 IP 地址并提供单一的服务，请求消息中的 URL 并没有传递主机名。而随着虚拟主机的出现，一台物理服务器上可以存在多个虚拟主机，并且它们共享同一个 IP 地址。为了支持虚拟主机，HTTP/1.1 中添加了 host 请求头，请求消息和响应消息中应声明这个字段，若请求消息中缺少该字段时服务端会响应一个 404 错误状态码。
**长连接**：HTTP/1.0 默认浏览器和服务器之间保持短暂连接，浏览器的每次请求都需要与服务器建立一个 TCP 连接，服务器完成后立即断开 TCP 连接。HTTP/1.1 **默认使用的是持久连接**，其支持在同一个 TCP 请求中传送多个 HTTP 请求和响应。此之前的 HTTP 版本的默认连接都是使用非持久连接，如果想要在旧版本的 HTTP 协议上维持持久连接，则需要指定 Connection 的首部字段的值为 Keep-Alive。















### 补充

#### Expires、Cache-Control、Last-Modified和If-Modified—Since、Etag和If-None-Match



##### 1.Expires

页面的初次访问者会进行很多HTTP请求，但是通过使用一个长久的Expires头，可以使这些组件被缓存，下次访问的时候，就可以减少不必要的HTPP请求，从而提高加载速度。

Web服务器通过Expires头告诉客户端可以使用一个组件的当前副本，直到指定的时间为止。例如：

`Expires: Fri, 18 Mar 2016 07:41:53 GMT`

Expires缺点： 它要求服务器和客户端时钟严格同步；过期日期需要经常检查

HTTP1.1中引入Cache-Control来克服Expires头的限制，使用max-age指定组件被缓存多久。

`Cache-Control： max-age=12345600`

若同时制定Cache-Control和Expires，则max-age将覆盖Expires头.





##### 2.Cache-Control

Cache-Control 是指缓存指令，这个指令**控制谁在什么条件下可以缓存响应**，以及可以缓存多久。这个协定取代了以前的 Expires 指令，在 **HTTP/1.1** 开始支持，在这么长时间后，我们可以认为 Cache-Control 在正常环境下都是支持的。Cache-Control的格式如下：



```
Cache-control: must-revalidate
Cache-control: no-cache
Cache-control: no-store
Cache-control: no-transform
Cache-control: public
Cache-control: private
Cache-control: proxy-revalidate
Cache-Control: max-age=<seconds> //Cathe-Control：max-age=315360000
Cache-control: s-maxage=<seconds>

```

