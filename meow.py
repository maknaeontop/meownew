f = open('zamok.txt','r',encoding='utf-8')
import re
zamok = f.read()

ifam = re.compile('[А-ЯЁ][а-яё]?\.\s?[А-ЯЁ][а-яё]+')
iifam = re.compile('(([А-ЯЁ][а-яё]?\.\s?-?)+[А-ЯЁ][а-яё]+)')
imyafam = re.compile ('[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+')

result1 = ifam.findall(zamok)
print(result1)

result2 = imyafam.findall(zamok)
result3 = iifam.findall(zamok)
print(result2)
print(result3)


f.close
