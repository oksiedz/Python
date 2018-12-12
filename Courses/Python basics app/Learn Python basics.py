#printing string
print("Hello world!");
print('Hello world 2');

#id function
x = 42;
print(id(x));

#data types
myint = 1;
print(myint);

myfloat = 7.0;
myfloat2 = float(8);
print(myfloat);
print(myfloat2);
hello = 'Hello';
world = "world";
Helloworld = hello + " " + world;
print(Helloworld);

#multiple assignments
a, b, c = 2, 3, 4;
print(a,b,c);

#lists
list = [ 'abcd', 786, 2.23, "john", 70.2];
tinylist = [123, 'john'];

#print complete list
print(list);
#print first element
print(list[0]);
#print elements from 2 to 3
print(list[1:3]);
#print list starting from 3rd element
print(list[2:]);
#print list two times
print(tinylist*2);
#print concatenated list
print(list + tinylist);

#tuples
#tuples are read only lists which cannot be updated.
tuple = ("tuple", "abcd", 786, 2.23, "john");
print(tuple);