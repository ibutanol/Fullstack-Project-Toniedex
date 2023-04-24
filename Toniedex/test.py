import re 

a = 'https://res.cloudinary.com/tonies/image/fetch/f_auto,q_auto,c_fill,b_rgb:ffffff,w_166,h_125/https://278163f382d2bab4b036-4f5ec62496a160f3570d3b6e48fc4516.ssl.cf3.rackcdn.com/10001473-50004892-b-CH2wvqo-.png'
x = re.findall(r"w_\d*,h_\d*",a)
print(a.replace(x[0],"w_2500,h_3000"))
