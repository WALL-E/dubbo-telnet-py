Dubbo Telnet Client of python
=====================================  
通过telnet调用Dubbo接口

### 兼容性测试

*  Python 2.6.6
*  Python 2.7.10
*  Python 3.4.3

### 安装

*  easyinstall安装 

```shell
easy_install dubbo_telnet
```

*  pip安装 

```shell
pip install --upgrade dubbo_telnet
```

*  git安装  

```shell
pip install --upgrade git+https://github.com/WALL-E/dubbo-telnet-py.git
```

### Example

```python
    import dubbo_telnet

    Host = '192.168.1.203'  # Doubble服务器IP
    Port = 28008  # Doubble服务端口

    # 初始化dubbo对象
    conn = dubbo_telnet.connect(Host, Port)

    # 设置telnet连接超时时间
    conn.set_connect_timeout(10)

    # 设置dubbo服务返回响应的编码
    conn.set_encoding('gbk')

    interface = 'com.zrj.pay.trade.api.QueryTradeService'
    method = 'tradeDetailQuery'
    param = '{"id": "nimeide"}'
    print conn.invoke(interface, method, param)

    command = 'invoke com.zrj.pay.trade.api.QueryTradeService.tradeDetailQuery({"message":"hello,world"})'
    print conn.do(command)
```

### Dubbo Telnet命令

Dubbo2.0.5以上版本服务提供端口支持telnet命令，使用如下

```shell
telnet localhost 20880
```

或者

```shell
echo status | nc -i 1 localhost 20880
```

详见[Dubbo官方文档](http://dubbo.io/)
