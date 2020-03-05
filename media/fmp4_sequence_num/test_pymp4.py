from pymp4.parser import Box

data = None

with open('frag1.m4s', 'rb') as f:
    data = f.read()

ftyp = Box.parse(data)

print(dir(ftyp))

print(ftyp)
print('haha', ftyp.end)

t = Box.parse(data[36:])
#print(t)

boxes = []
processed_byte = 0
data_lenth = len(data)
while True:
    if processed_byte >= data_lenth:
        break

    b = Box.parse(data[processed_byte:])
    boxes.append(b)

    processed = b.end
    processed_byte += processed

print(len(boxes))

for b in boxes:
    print(b.type)

#print(boxes[2])
#print(dir(boxes[2]))
print(boxes[2].search_all('sequence_number'))
print(boxes[4].search_all('sequence_number'))

print(list(boxes[2].keys()))

for c in boxes[4].children:
    if c.type == b'mfhd':
        print('sequence_number', c.sequence_number)
        c.sequence_number = 33
        break

print(boxes[4].search_all('sequence_number'))

with open('frag1-changed.m4s', 'wb') as f:
    for b in boxes:
        data = Box.build(b)
        f.write(data)
