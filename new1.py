# 正则表达式
# re模块
# \d匹配一个数字,\s匹配一个空格，\w匹配一个数字或者字符，()分组
s = r'ABC\-001' # 使用r前缀不用考虑转义
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())