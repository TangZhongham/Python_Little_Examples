"""
知乎上有人搞了个防剧透，于是无聊自己实现一下

"""
import itchat

FORBIDDEN_WORDS = [
    "钢铁侠",
    "铁人",
    "iron",
    "man",
    "小蜘蛛",
    "绿巨人",
    "鹰眼",
    "美队",
    "tony",
    "stack",
    "复仇者",
    "联盟",
    "妇联",
    "黑寡妇",
    "灭霸",
    "死",
    "灰",
    "幻视",
    "挂",
]

reply_text = '\n' * 40 + '防剧透保护启动！！！'


class AntiSpoiler:
    """防剧透"""
    @itchat.msg_register(itchat.content.TEXT, isGroupChat=True, isFriendChat=True)
    def text_reply(msg):
        for i in FORBIDDEN_WORDS:
            if i in msg.text:
                return reply_text

    def run(self):
        """跑！"""
        itchat.auto_login()
        itchat.run()


if __name__ == '__main__':
    AntiSpoiler().run()
