#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

import sys
import random
from dueros.Bot import Bot
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1

reload(sys)
sys.setdefaultencoding('utf8')


class HChildHood(Bot):

    def __init__(self, request_data):
        super(HChildHood, self).__init__(request_data)
        self.pics = [
            {'des': '小狗', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/gou.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2Fa2830cb8f4d2e71a5c7b9b6f86b68cb8206ec82a34c49f76e965d7201da0d61e'},
            {'des': '小臭鼬', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/chouyou.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F3ba24af94d380035d7c7ad2aa9cd6246702eac53944695c765383aba03ee63d5'},
            {'des': '小飞机', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/feiji.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F7e8b57490568a688ac3ff372cbe2ce2d3ae26398de68a5587d019dfe5c15ed64'},
            {'des': '小猴子', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/houzi.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2Fbb6571b5a863dcbad1f5ee4d058bf503ec6e4b102fa9c2d7416100f5fac8a646'},
            {'des': '小金鱼', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/jinyu.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F51ec2f6465c5579476f5bb51edee92f89ec16f84f0224da0dca2a08908758548'},
            {'des': '小猫咪', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/mao.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F746c01ab873439ba78e2b67a61cc58b96537c1ef94bcb5b1ec7e1214b82e16da'},
            {'des': '猫头鹰', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/maotouying.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2Fab546cb7f04a57b83664da26e70bf75b5efc094ef7da07a7ff81ac3ebee37ec0'},
            {'des': '小青蛙', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/qingwa%27.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2Fe4e49e25611c11219473103a6244c414a8e45ff259e72f2fc2bc1815479544a1'},
            {'des': '小兔子', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/tuzi.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F4252b8422110445d354d530e894333c01352aecfeb7ff785a027c3060abc6b6e'},
            {'des': '小鱼儿', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/yu.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F9427c86d055832c88b7aa32576383a095172d21a91891e0fe941844a131f2a55'},
            {'des': '小章鱼', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/zhangyu.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-14T03%3A30%3A38Z%2F-1%2F%2F07f21dabf5b3b37b27b6e8af13a41de3dcd5f6b4d69cdfca4f404c7eec22dbd7'},
        ]

        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('start', self.get_guide)
        self.add_intent_handler('next', self.get_next)
        self.add_intent_handler('previous', self.get_previous)
        self.add_intent_handler('ai.dueros.common.default_intent', self.get_default)
        self.add_session_ended_handler(self.ended_request)

    def launch_request(self):
        """
        打开调用名
        """
        self.wait_answer()
        template = BodyTemplate1()
        template.set_title('简笔画')
        template.set_plain_text_content('欢迎进入简笔画，可以尝试对我说开始画图。')
        template.set_background_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532350870263&di=c93edb2fb9a3cfe7a632acc46cceba62&imgtype=0&src=http%3A%2F%2Ffile25.mafengwo.net%2FM00%2F0A%2FAC%2FwKgB4lMC26CAWsKoAALb5778DWg60.rbook_comment.w1024.jpeg')
        template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        render_template = RenderTemplate(template)
        return {
            'directives': [render_template],
            'outputSpeech': r'欢迎进入简笔画，可以尝试对我说开始画图。'
        }

    def ended_request(self):
            """
            关闭技能
            """
            return {
                'outputSpeech': r'感谢您的使用'
            }

    def get_default(self):
        self.wait_answer()
        return {
            'outputSpeech': r'不太明白您的表达。'
        }

    def get_guide(self):
        self.wait_answer()
        index = int(random.random()*len(self.pics))
        self.set_session_attribute('index', index, -1)
        pic = self.pics[index]
        template = self.get_template(pic['des'], pic['pic'])
        return {
            'directives': [template],
            'outputSpeech': pic['des']
        }

    def get_next(self):
        self.wait_answer()
        index_str = self.get_session_attribute('index', -1)
        if index_str == '-1' or int(index_str) + 1 >= len(self.pics):
            index = int(random.random()*len(self.pics))
        else:
            index = int(index_str) + 1

        self.set_session_attribute('index', index, -1)
        pic = self.pics[index]
        template = self.get_template(pic['des'], pic['pic'])
        return {
            'directives': [template],
            'outputSpeech': pic['des']
        }

    def get_previous(self):
        self.wait_answer()
        index_str = self.get_session_attribute('index', -1)
        if index_str == '-1' or int(index_str) - 1 < 0:
            index = int(random.random() * len(self.pics))
        else:
            index = int(index_str) - 1

        self.set_session_attribute('index', index, -1)
        pic = self.pics[index]
        template = self.get_template(pic['des'], pic['pic'])
        return {
            'directives': [template],
            'outputSpeech': pic['des']
        }

    def get_template(self, content, bg='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532350870263&di=c93edb2fb9a3cfe7a632acc46cceba62&imgtype=0&src=http%3A%2F%2Ffile25.mafengwo.net%2FM00%2F0A%2FAC%2FwKgB4lMC26CAWsKoAALb5778DWg60.rbook_comment.w1024.jpeg'):
        template = BodyTemplate1()
        template.set_title('简笔画')
        template.set_plain_text_content(content)
        template.set_background_image(bg)
        template.set_token(content)
        render_template = RenderTemplate(template)
        return render_template


def handler(event, context):

    bot = HChildHood(event)
    result = bot.run()
    return result
