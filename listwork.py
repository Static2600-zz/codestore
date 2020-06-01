list1 = [1,3,3,5,7,9,13,15] 
print('1.',list1)

list1.append(17)
print('2.',list1)

list1.insert(6,11)
print('3.',list1)

list1.insert(0,-1)
print('4.',list1)

list1.remove(3)
print('5.',list1)

del list1[0] 
print('6.',list1)

list1.pop(0)
print('7.',list1)
print('8.',list1[0],'and ',list1[3])

list1.insert(0,1)
print('9.',list1)
print('10.',list1[0], 'and ',list1[3])

print ('11.',list1[2:5])

print ('12.',list1 * 2)

list2 = [5,4,3,2,1,0]

print('13.',list1+list2)

list3=list1+list2
print('14.',list3)

print('15.',list3[0:])
print('16.',list3[0:])
print('17.',list3[7:])
print('18.',list3[:10])
print('19.',list3[6:9])
print('20.',list3)
print('21.',list3[8:11])
print('21.',list3[-11:-5])
print('22.',list3[:7])
print('23.',list3[:-7])
print('23.',list3[-7:])

print('24.',list3.index(3))
print('25.',list3.count(3))

list4 = list3
list4.sort()
print('25.',list4)