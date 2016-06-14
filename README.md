Dubbo Telnet Client of python
=====================================  
通过telnet调用Dubbo接口
-------------------------------------



### 安装
*  源码安装  
python setup.py install
*  pip安装  
pip install dubbo-client==0.9b5
*  git安装  
pip install git+https://github.com/WALL-E/dubbo-telnet-py.git@0.9b5

### Example

```python

    conn = dubbo.init(host="192.168.1.203", port=28008)
    interface = 'com.zrj.pay.trade.api.QueryTradeService'
    method = 'tradeDetailQuery'
    request = {"id": "nimeide"}
    # response is a JSON Object
    response = conn.invoke(service, request)
    print response 
```

### TODO
todo

### Licenses
LICENSE   