"""
列表用[]表示，是python中最常用的数据类型。列表类似于传统语言中的数组，但它更灵活、强大。
列表支持字符、数字、字符串，也可以包含列表（即列表嵌套）。
列表中的每个元素都分配一个数字，这个数字即元素的位置或索引，第一个元素的索引为0，第二个元素的索引为1。
上下标可以为空，表示取到头（上标为空）或尾（下标为空）。
"""

#
#输出列表
#
print("#1:输出列表")

list1 = [ '元素_1', '元素_2', '元素_3' ] #定义列表
list2 = [ '元素_4', '元素_5', '元素_6' ]
for x in list1: #将每个元素单独输出  
  print(x)

print( list1 )  #输出整个列表
print( list1[:] )  #输出整个列表
print( list1[1:] ) #输出索引为1~尾（含尾）的元素
print( list1[1:2] ) #输出索引为1~2（不含2）的元素
print( list1[:2] ) #输出索引为头~2（不含2）的元素
print( "list1+list2=", list1 + list2 ) #用“+”号合并输出两个列表
print( "list1*2=", list1*2 ) #用“*”号重复输出列表

list2.insert( 0, list1 )
print( "list2=", list2 )
print( "tuple(list2)=", tuple(list2) )

#
#range
#
for y in range( len(list1) ):
  print( y, list1[y] )
