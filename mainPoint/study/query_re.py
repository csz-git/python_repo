#coding=utf-8
import re

a = re.findall("匹配规则", "这个字符串是否有匹配规则的字符")   #第二步，调用模块函数
a = re.findall("^匹配规则", "匹配规则这个字符串是否匹配")   #字符串开始位置与匹配规则符合就匹配，否则不匹配
a = re.findall("匹配规则$", "这个字符串是否匹配规则")   #字符串结束位置与匹配规则符合就匹配，否则不匹配
a = re.findall("匹配规则*", "这个字符串是否匹配规则则则则则")   #需要字符串里完全符合，匹配规则，就匹配，（规则里的*元字符）前面的一个字符可以是0或多个原本字符
a = re.findall("匹配+", "匹配配配配配规则这个字符串是否匹配规则则则则则")   #需要字符串里完全符合，匹配规则，就匹配，（规则里的+元字符）前面的一个字符可以是1个或多个原本字符
a = re.findall("匹配规则?", "匹配规这个字符串是否匹配规则则则则则")   #需要字符串里完全符合，匹配规则，就匹配，（规则里的?元字符）前面的一个字符可以是0个或1个原本字符
a = re.findall("匹配规则{3}", "匹配规这个字符串是否匹配规则则则则则")   #{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次
a = re.findall("匹配[a,b,c]规则", "匹配a规则这个字符串是否匹配b规则则则则则")   #需要字符串里完全符合，匹配规则，就匹配，（规则里的 [] 元字符）对应位置是[]里的任意一个字符就匹配
a = re.findall("[^a-z]", "匹配s规则这s个字符串是否s匹配f规则则re则则则")   #反取，匹配出除字母外的字符

a = re.findall("\d", "匹配规则这2个字符串3是否匹配规则5则则则7则")   #\d匹配任何十进制数，它相当于类[0-9]
a = re.findall("\d+", "匹配规则这2个字符串134444是否匹配规则5则则则7则")   #\d+如果需要匹配一位或者多位数的数字时用
a = re.findall("\D", "匹配规则这2个字符串3是否匹配规则5则则则7则")   #\D匹配任何非数字字符，它相当于类[^0-9]
a = re.findall("\s", "匹配规则   这2个字符串3是否匹\n配规则5则则则7则")   #\s匹配任何空白字符，它相当于类[\t\n\r\f\v]
a = re.findall("\S", "匹配规则   这2个字符串3是否匹\n配规则5则则则7则")   #\S匹配任何非空白字符，它相当于类[^\t\n\r\f\v]
a = re.findall('\w',"https://www.cnblogs.com/")  #\w匹配包括下划线在内任何字母数字字符，它相当于类[a-zA-Z0-9_]
a = re.findall('\W',"https://www.cnblogs.com/")  #\w匹配包括下划线在内任何字母数字字符，它相当于类[a-zA-Z0-9_]
a = re.search("(a4)+", "a4a4a4a4a4dg4g654gb")   #匹配一个或多个a4
a = re.search("a(\d+)", "a466666664a4a4a4dg4g654gb")    #匹配 (a) (\d0-9的数字) (+可以是1个到多个0-9的数字)
a = re.findall(r"你|好", "a4a4a你4aabc4a4dgg好dg4g654g")   #|或，或就是前后其中一个符合就匹配
print(a)

origin = "hello egon bcd egon lge egon acd 19"
r = re.match("h\w+", origin)    #match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
r = re.match("h(\w+)", origin)   #match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
r = re.match("(?P<n1>h)(?P<n2>\w+)", origin)   #?P<>定义组里匹配内容的key(键)，<>里面写key名称，值就是匹配到的内容
r = re.search("a\w+", origin)    #search浏览全部字符串，匹配第一符合规则的字符串，浏览整个字符串去匹配第一个，未匹配成功返回None
r = re.search("a(\w+).*(\d)", origin)
r = re.search("a(?P<n1>\w+).*(?P<n2>\d)", origin)   #?P<>定义组里匹配内容的key(键)，<>里面写key名称，值就是匹配到的内容
print(r.group())     # 获取匹配到的所有结果，不管有没有分组将匹配到的全部拿出来
print(r.groups())    # 获取模型中匹配到的分组结果，只拿出匹配到的字符串中分组部分的结果
print(r.groupdict()) # 获取模型中匹配到的分组结果，只拿出匹配到的字符串中分组部分定义了key的组结果

r = re.split("a", origin) #根据正则匹配分割字符串
r = re.split("a\w+", origin) #根据正则匹配分割字符串
r = re.sub("a","替换",origin) #替换匹配成功的指定位置字符串
a,b = re.subn("a","替换",origin) #替换匹配成功的指定位置字符串,并且返回替换次数，可以用两个变量分别接受
print(r)
print(a, b)