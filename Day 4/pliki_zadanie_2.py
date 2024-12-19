import chardet

with open("test2.log", "r", encoding='utf-8') as f:
    raw_data = f.read()

print(raw_data)

with open("test2.log", 'rb') as f:
    raw_data = f.read()

print(raw_data)

result = chardet.detect(raw_data)
print(result)
encoding = result['encoding']

print(raw_data.decode(encoding=encoding))
# decoded_data = raw_data.decode(result['encoding'])
# print(decoded_data)
