import string

txt = "Hi’ Sam!"
x = "mSa"
y = "eJo"
z = string.punctuation + '’'
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
