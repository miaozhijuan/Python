## 1.什么是字符串
'''
a. 使用单引号或者双引号括起来的字符集就是字符串
b. 引号中单独的符号，数字，字母等叫字符


c. 转义字符：可以用来表示一些有特殊功能或者是特殊意义的字符（通过在固定的字符前加\）
\' -> '
\\ -> \
\n -> 换行
\t -> 制表符
\" -> "
在计算字符串的长度的时候，转义字符代表一个字符

'''
'123'  #数字字符串
'asdf'
'asd@@#!!'
'中文汉字'
'   '
'\\'
str1 = '床前明月光,\n疑是地上霜。\n举头望明月,\n低头思故乡。'
print(str1)


str2 = '\\\''
print(str2)



#2.阻止转义
'''
可以通过在字符串前面加r或者R，来阻止转义字符转义
'''
str1 = R'\\1\n2'
print(str1)


#3.python中字符串中的字符是Unicode编码

'''
Unicode编码:shiyong 16位对一个字符进行编码。编码的目的是让字符可一存储到计算机中。
Unicode码中包含了ASSCII码，可以表示世界上所有的语言和符号
'''

#a.获取一个字符的Unicode码
#ord(编码值)
print(hex(ord('故')))

#b.将Unicode码转换成字符
#chr(编码值)
print(chr(0x4Efd))

#字符串比较大小的时候,从字符开始一次往后比较每个字符的大小，直到遇到字符不一样为止。
#比较字符大小的时候，实质比的是他们的编码的大小

print('abc' > 'a')