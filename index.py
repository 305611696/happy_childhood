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
            {'des': '小狗', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/gou.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2Fbcdb7178025288cb89ed463a9816b41b732e72a02311bd61f440e197845e8eed'},
            {'des': '小浣熊', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/chouyou.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F60b301f2588a21555cf23ced57309bf9c2064f6e014d7d6193d5908e68b5a24a'},
            {'des': '小飞机', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/feiji.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F8d9e91d2bd70d78e6469cd1896575c88fcd7f48e32ea7aa82b789c543231cf0a'},
            {'des': '小猴子', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/houzi.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2Fdd4c2913f838a7917f6f5a4d964d0a69b22405b3a7c0983170fbc3c20e99b681'},
            {'des': '小金鱼', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/jinyu.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F2bcae622a12fa680f8d0f5dc58e741a339250a964a381671c5f6d7f46e609d37'},
            {'des': '小猫咪', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/mao.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F5ff1b80a13f0dd9ade9d0aeb98a1cbfddc4b18caab5b3ca6093b6688c9f36fa2'},
            {'des': '猫头鹰', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/maotouying.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F2f901f83649019a61d96e7757ed2ec60c5d1165a1fe1f4657cff3f53dad19ee5'},
            {'des': '小青蛙', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/qingwa%27.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F323211fff790feccb8831b12ba6df5eb175d5795b266c079a0961ecf14cfbc87'},
            {'des': '小兔子', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/tuzi.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F86dd636c2b87bf8689e18259fe64136c084adb98df0587a547b80e78e1a85731'},
            {'des': '小鱼儿', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/yu.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F9d56963b0cd710d506c4c56e252376f6ee3eebcc8a06f2b615fb79584a8e3082'},
            {'des': '小章鱼', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/zhangyu.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2F228c93080f253336cbc5f9864e3a3798dd671ae7572fae679c37b2b6d048b8a3'},
            {'des': '大猫咪', 'pic': 'http://dbp-resource.gz.bcebos.com/217dd919-cd4f-3942-3594-11d05b9f5d1e/maomi.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2019-01-10T03%3A02%3A15Z%2F-1%2F%2Fb58777285005d3f3208584bab3c31e8c309545e9db2b880f44d57c0594ef95c6'},
        ]

        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('start', self.get_guide)
        self.add_intent_handler('next', self.get_next)
        self.add_intent_handler('previous', self.get_previous)
        self.add_intent_handler('ai.dueros.common.default_intent', self.get_default)

    def launch_request(self):
        """
        打开调用名
        """
        self.wait_answer()
        template = BodyTemplate1()
        template.set_title('快乐童年')
        template.set_plain_text_content('欢迎进入快乐童年')
        template.set_background_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532350870263&di=c93edb2fb9a3cfe7a632acc46cceba62&imgtype=0&src=http%3A%2F%2Ffile25.mafengwo.net%2FM00%2F0A%2FAC%2FwKgB4lMC26CAWsKoAALb5778DWg60.rbook_comment.w1024.jpeg')
        template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        render_template = RenderTemplate(template)
        return {
            'directives': [render_template],
            'outputSpeech': r'欢迎进入快乐童年，可以尝试对我说开始画图。'
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
            index = random.random()*len(self.pics)
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
            index = random.random() * len(self.pics)
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
        template.set_title('快乐童年')
        template.set_plain_text_content(content)
        template.set_background_image(bg)
        template.set_token(content)
        render_template = RenderTemplate(template)
        return render_template


def handler(event, context):

    bot = HChildHood(event)
    result = bot.run()
    return result
