Dubbo Telnet Client of python
=====================================  
通过telnet调用Dubbo接口


### 安装

*  源码安装 

```shell
python setup.py install
```

*  pip安装 

```shell
pip install dubbo-client
```

*  git安装  

```shell
pip install git+https://github.com/WALL-E/dubbo-telnet-py.git
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

