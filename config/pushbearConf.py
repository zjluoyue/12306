# -*- coding: utf8 -*-
import time

import requests
from config.ticketConf import _get_yaml
from config.urlConf import urls
from myUrllib.httpUtils import HTTPClient

PUSH_BEAR_API_PATH = "https://pushbear.ftqq.com/sub"


def sendPushBear(msg):
    """
    pushBear微信通知
    :param str: 通知内容 content
    :return:
    """
    conf = _get_yaml()
    if conf["pushbear_conf"]["is_pushbear"] and conf["pushbear_conf"]["send_key"].strip() != "":
        try:
            sendPushBearUrls = urls.get("Pushbear")
            data = {
                "sendkey": conf["pushbear_conf"]["send_key"].strip(),
                "text": "易行购票成功通知，{}".format(time.strftime("%Y-%m-%d %H:%M:%S")),
                "desp": msg
            }
            httpClint = HTTPClient(0)
            sendPushBeaRsp = httpClint.send(sendPushBearUrls, data=data)
            if sendPushBeaRsp.get("code") is 0:
                print(u"已下发 pushbear 微信通知, 请查收")
            else:
                print(sendPushBeaRsp)
        except Exception as e:
            print(u"pushbear 配置有误 {}".format(e))
    else:
        pass


if __name__ == '__main__':
    sendPushBear(1)
