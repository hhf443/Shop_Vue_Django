
import requests
import json
from random import choice

class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def generate_code(self):
        """
        生成四位数字验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return ''.join(random_str)

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "{code}".format(code)
        }
        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)