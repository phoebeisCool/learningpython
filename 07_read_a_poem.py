# f = open(r'.\一首诗.text','r',encoding = 'utf-8')
# content = f.read()
# print(content)
# f.close()

with open(r'.\一首诗.text','r',encoding = 'utf-8') as f:
    content = f.read()
    print(content)
