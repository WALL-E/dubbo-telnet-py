Dubbo Telnet Client of python
=====================================  
通过telnet调用Dubbo接口


### 安装
*  手动安装

```shell
dist=`python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"`
cp dubbo.py $dist
```

*  源码安装(Todo) 

```shell
python setup.py install
```

*  pip安装(Todo)  

```shell
pip install dubbo-client==0.9b5
```

*  git安装(Todo)  

```shell
pip install git+https://github.com/WALL-E/dubbo-telnet-py.git@0.9b5
```

### Example

```python

    Host = '192.168.1.203'  # Doubble服务器IP
    Port = 28008  # Doubble服务端口

    # 初始化dubbo对象
    conn = dubbo(Host, Port)

    # 设置telnet连接超时时间
    conn.set_connect_timeout(10)

    # 设置dubbo服务返回响应的编码
    conn.set_encoding('gbk')

    interface = 'com.zrj.pay.trade.api.QueryTradeService'
    method = 'tradeDetailQuery'
    param = '{"id": "nimeide"}'
    print conn.invoke(interface, method, param)

    command = 'invoke com.zrj.pay.trade.api.QueryTradeService.tradeDetailQuery({"id":"nimeide"})'
    print conn.do(command)
```

### TODO
安装

### Licenses
LICENSE   
