import json
import re
import pandas
from collections import defaultdict
from datetime import datetime
startTime = datetime.now()


good = open("good.txt", 'w')
notfound = open("notfound.txt", 'w')
notparsed = open("notparsed.txt", 'w')
ambig = open("ambig.txt", 'w')


def make_range(text):
    nums = []
    text = re.sub(r"\s+", "", text)
    text = re.sub(r"[а-яa-z]", "", text)
    for i in text.split(','):
        me = i.split('-')
        if len(me) > 1:
            nums.extend(list(range(int(me[0]), int(me[1]), 2)))
            nums.append(int(me[1]))
        else:
            nums.append(i)
    return nums


def is_in_range(text, building):
    nns = make_range(text)
    # print(nns)
    return True if building in nns else False


ds = pandas.read_csv('districts.csv', sep=',', )

# print(ds.query('a > b'))

# res = ds.loc[ds['street'] == "Аполинарьевская ул."]
res = ds.loc[ds['street'].str.contains(r'Аполинарьевская')]
# print(res)
# exit()
# dtype={"user_id": int, "username": object}
[n, m] = [0, 70000]
# [n, m] =  [0, 100]

# Ванеева ул
# Ваупшасова ул
# Гурского ул
# Кирова ул
# Козлова ул
# Комсомольская ул
# Куйбышева ул
# Ленина ул
# Машерова просп
# Московская ул
# Независимости просп
# Немига ул
# Партизанский просп
# Первомайская ул
# Платонова ул
# Солтыса ул
# Старовиленская ул
# Сурганова ул
# Тимирязева ул
# Филимонова ул
# Харьковская ул

# 290 address points, 1079 addresses

distrib = defaultdict(int)


df = pandas.read_csv('all.csv', sep=',', dtype=object )
for index, row in df.iterrows():
    if index >= n:
        id = str(row['id'])
        addr = row['address']
        addr_str = row['address']
        is_got = False
        if type(addr) is str:
            addr = re.sub(r"^Минск", "", addr)
            # addr = re.sub(r"^г\.", "", addr, flags=re.IGNORECASE)

            addr = re.sub(r"\b[А-Яа-я]\b.[\.]?", "", addr, flags=re.IGNORECASE)


            addr = re.sub(r"Минск$", "", addr)
            addr = re.sub(r"улица", "ул.", addr, flags=re.IGNORECASE)
            addr = re.sub(r"^[\s\.\,]+", "", addr)


            addr = re.sub(r"Героев\s+120[\-ой]*\s+Дивизии", "Гсдд", addr, flags=re.IGNORECASE)
            addr = re.sub(r"50 лет Победы", "Плпбд", addr, flags=re.IGNORECASE)
            addr = re.sub(r"40 лет Победы", "Слпбд", addr, flags=re.IGNORECASE)
            addr = re.sub(r"8 Марта", "Вмрт", addr, flags=re.IGNORECASE)
            addr = re.sub(r"3[\-eго]{0,4}\s+сентября", "Тсент", addr, flags=re.IGNORECASE)

            addr = re.sub(r"ё", "е", addr)

            addr = re.sub(r"м[иі]нск", "", addr, flags=re.IGNORECASE)
            addr = re.sub(r"\bнапротив\b", "", addr, flags=re.IGNORECASE)
            addr = re.sub(r"беларусь", "", addr, flags=re.IGNORECASE)
            addr = re.sub(r"\bрядом\b", "", addr, flags=re.IGNORECASE)
            addr = re.sub(r"\s+дом\s+", " ", addr)
            # addr = re.sub(r"\s+д[\s\.]\s*", " ", addr, flags=re.IGNORECASE)

            addr = re.sub(r"(?<=[\.\,])(?=[0-9а-я])", " ", addr, flags=re.IGNORECASE)

            addr = re.sub(r"\bдом(?=[^а-я])", " ", addr, flags=re.IGNORECASE)

            addr = re.sub(r"газеты", "", addr, flags=re.IGNORECASE)

            addr = re.sub(r"\s+д(?=\d)", " ", addr, flags=re.IGNORECASE)

            addr = re.sub(r"\s+слобода\b", "ЪСлобода", addr, flags=re.IGNORECASE)

            addr = re.sub(r"\s+бор\b", "ЪБор", addr, flags=re.IGNORECASE)
            addr = re.sub(r"\s+вал\b", "ЪВал", addr, flags=re.IGNORECASE)

            addr = re.sub(r"\,\s+", " ", addr)
            addr = re.sub(r"^рядом\s+с", "", addr)
            addr = re.sub(r"^\s+", "", addr)

            # addr = re.sub(r"\s+[А-Я]\.\s+", " ", addr)



            addr = re.sub(r"\bул\b\.?", "ул.", addr, flags=re.IGNORECASE)
            addr = re.sub(r"\bпер\b\.?", "пер.", addr, flags=re.IGNORECASE)
            addr = re.sub(r"\bпр\b\.?", "просп.", addr, flags=re.IGNORECASE)
            addr = re.sub(r"переулок", "пер.", addr)
            addr = re.sub(r"площадь", "пл.", addr)
            addr = re.sub(r"проспект", "просп.", addr)
            addr = re.sub(r"бульвар", "бул.", addr)
            addr = re.sub(r"\bтракт\b", "трт.", addr, flags=re.IGNORECASE)


            addr = addr.strip()
            # print(addr)

            # match = re.search(r'(ул\.)\s+([А-Яа-я ])\s+(\d[\dа-я\s]+)$|([А-Яа-я ])\s+(ул\.)\s+(\d[\dа-я\s]+)$', addr)
            #
            stype = ''
            sname = ''
            snum = ''
            bigmatch = re.search(r'(бул|ул|просп|пер|пл|трт)\.\s+([А-Яа-яЁёІіЎў ]+)(\d*)', addr)
            if bigmatch:
                # print(1, bigmatch.groups())
                stype = bigmatch.group(1) + '.'
                sname = bigmatch.group(2)
                if bigmatch.group(3): snum = bigmatch.group(3)
                is_got = True

            if not is_got:
                # print(2)
                bigmatch = re.search(r'([А-Яа-яЁёІіЎў]+)\s+(бул|ул|просп|пер|пл|трт)\.\s*(\d*)', addr)
                if bigmatch:
                    stype = bigmatch.group(2) + '.'
                    sname = bigmatch.group(1)
                    if bigmatch.group(3): snum = bigmatch.group(3)
                    is_got = True

            if not is_got:
                # print(3)
                bigmatch = re.search(r'^([А-Яа-яЁёІіЎў]+)\s*(\d*)\b', addr)
                if bigmatch:
                    sname = bigmatch.group(1)
                    if bigmatch.group(2): snum = bigmatch.group(2)
                    is_got = True
            sname = sname.strip()
            if is_got and len(sname):
                if stype == 'трт.':
                    stype = 'тракт'
                # print(":" + sname + "|" + addr)
                # print(sname)
                snames = sname.split(' ')
                if len(snames) > 1 and snames[1]:
                    sname = snames[1]

                sname = re.sub(r"\s+$", "", sname)
                sname = sname[0].title() + sname[1:]

                sname = re.sub(r"Ъ", " ", sname)

                sname = re.sub(r"Плпбд", "50 Лет Победы", sname)
                sname = re.sub(r"Слпбд", "40 Лет Победы", sname)
                sname = re.sub(r"Тсент", "3 Сентября", sname)
                sname = re.sub(r"Вмрт", "8 Марта", sname)
                sname = sname.title()
                sname = re.sub(r"Гсдд", "Героев 120-й Дивизии", sname)

                match = re.search(r'^(\d)(?=\D)', addr)
                ending = 'я' if stype == 'ул.' else 'й'
                sord = ' '+match.group(1) + '-' + ending + ' ' if match else ''

                # "Багратиона 2-й пер.", "Партизанский",
                query = sname + '\D*?' + sord + stype

                query = re.sub(r"\s+", " ", query)

                res = ds.loc[ds['street'].str.contains(query)]

                dst = ''
                replySize = len(res.index)
                if replySize == 1:
                    for val in res['district']:
                        this_dist = str(val)
                        good.write(id + "\t" + this_dist + "\n")
                        distrib[this_dist] += 1

                elif replySize == 0:
                    # print('================================================')
                    # print(sname +": "+ query)
                    suffix = ' '+ stype if stype else ''
                    # notfound.write(id+"\t"+sname + sord + suffix +"\t"+ addr +"\n")
                    # notfound.write(id+"\t"+addr+"|" +addr_str+"\n")
                    notfound.write(id+"\t"+addr_str+"\n")
                else:
                    rels = []

                    if not len(stype):
                        for ix, itrow in res.iterrows():
                            if itrow['district'] not in rels:
                                rels.append(itrow['district'])
                    else:
                        for ix, itrow in res.iterrows():
                            # print("!!!",row['buildings'])
                            numtxt = str(itrow['buildings'])
                            # if len(numtxt ) == 0:
                            # ambig.write(res.to_string(index=True, header=False) + "\n")
                            # ambig.write(sname + " "+ snum + " : " + str(make_range(numtxt))+"\n" )
                            #     exit()
                            # print(snum)
                            if snum and is_in_range(numtxt, int(snum)):
                                if itrow['district'] not in rels:
                                    rels.append(itrow['district'])
                    if len(rels) != 1:
                        # print(sord + sname + " " + stype + ' [' + snum + ']' +' :: '+addr)
                        # print(sord + sname + " " + stype)

                        # ambig.write(id+"\t"+sord + sname + " " + stype +' [' + str(snum) + '] | ' + addr_str + "\n")
                        # ambig.write(sord + sname + " " + stype + ' [' + str(snum) + ']' + ': ' + addr + '|' + addr_str + "\n")
                        ambig.write(id+"\t"+sord + sname + " " + stype + ' [' + str(snum) + ']' + ': ' + addr + "\n")
                        pass
                    else:
                        good.write(id + "\t" + str(rels[0]) + "\n")
                        # print(addr + "\n" + res.to_string(index=True, header=False))
                        pass
            else:
                notparsed.write(id+"\t"+addr + "\n")
                pass
        if index == m:
            break

good.close()
notfound.close()
notparsed.close()
ambig.close()
print (datetime.now() - startTime)
print(distrib)