# # ## my first program of PYTHON
# # list1 = [1,2,3,'p',"prajwal",8.34,4.78,2345];
# # print(len(list1));
# # list1.append(45);
# # print(list1);
# # list1.remove(1);
# # count = list1.count(3);
# # print(count);
# # list1.pop(1);
# # list1.insert(3,"shrutika");
# # print(list1)
# # #list1.sort();
# # print(list1)
# # a = 'prajwal'
# # b = 'kumbhar'
# # if(a!=b):
# #   print("Not equal");
# # elif(a==b):
# #   print("equal not")
# # else : print("Yes Present");
# # print(dict)



# # dict1 = {
# #   "name": "prajwal",
# #   "cgpa":8.7,
# #   "rollno":22413,
# #   "marks":[20,30,40],
# #   "info":{
# #     "a":1,
# #     "b":2,
# #     "c":3,
# #   }
# # };
# # print(dict1["cgpa"]);
# # print(dict1["marks"][2]);
# # print(dict1["rollno"]);
# # print(dict1["info"]["a"]);
# # print(dict1.keys());
# # print(dict1.values());
# # print(dict1.items());
# # print(dict1.get("name"));
# # dict1.update({"dep":"entc"});
# # print(dict1);



# # listi = [1,2,'p',"prajwal",'shruti','madhura'];
# # for i in listi : 
# #   print(i);
  
  
# # for i in range(1,5+1,2):
# #   print(i)

# def sum(a,b):
#   return a + b ;

# # print(sum(3,5));

# def factorial(n):
#   if(n<=1): return 1 ;
#   return n * factorial(n-1);

# # print(factorial(1));

# def sum_natural(n,sum):
#   if(n==0): return sum ;
#   sum += n ;
#   return sum_natural(n-1,sum);
  
# print(sum_natural(100,0));

# f = open("demo.txt","r");
# # data = f.read();

# print(f.readline(),end=" ");
# print(f.readline());
# f.close();

f = open("demo.txt",'a');
f.write("\nmhi i am prajwal+++++");
print("done");


