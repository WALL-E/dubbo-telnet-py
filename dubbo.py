#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import telnetlib


def do_telnet(host, port, finish, command):
    # 连接Telnet服务器
    tn = telnetlib.Telnet(host=host, port=port, timeout=10)
    tn.set_debuglevel(0)

    # 触发doubble提示符
    tn.write('\n')

    # 执行命令
    tn.read_until(finish)
    tn.write('%s\n' % command)

    # 执行完毕后，终止Telnet连接（或输入exit退出）

    # tn.read_until(finish)

    data = ''
    while data.find('>') == -1:
        data = tn.read_very_eager()
    data = data.split("\n")
    # print data[0]
    data = json.loads(data[0], encoding="gbk")
    # print data["responseDesc"]

    tn.close()  # tn.write('exit\n')

    return data


if __name__ == '__main__':
    # 配置选项
    Host = '192.168.1.203'  # Doubble服务器IP
    Port = 28008  # Doubble服务端口
    finish = 'dubbo>'      # 命令提示符
    command = 'invoke com.zrj.pay.trade.api.QueryTradeService.tradeDetailQuery({"id":"nimeide"})'
    print do_telnet(Host, Port, finish, command)
