## Created list

first_list = ['Monday', 'Tuesday', 4, 66, 'Wednesday', 120, 180, 'Thursday']; 
first_list[1]; #slice 2nd element
first_list[:3]; #slice 0-2nd element
first_list[::-2]; 
first_list[-1]; 
first_list[-2]; 

## Insert element and  append

first_list.append(333); 
first_list.insert(2, 444); 
first_list[4] = 'WED-replace'; 

#join elements 

join_text = ['morning', 'afternoon', 'evening']; 
",".join(join_text); 
"__aaaa___".join(join_text); 

##remove & pop

first_list.remove(120); 
first_list.pop(-2); 
first_list.pop(2); 

## concatenate lists

name_list = ['Nar', 'Sar', 'Od']; 
number_list = [111, 222, 333, 4444]; 

name_list + number_list; 

name_list.extend(number_list); 

## set list

set_list = {'Photo', 'Frame', 'Color', 10, 30, 10, 4, 'Color', 'Color', 5, 8, 9, 5, 9}; 
set_list.add('Price'); 
set_list.add(1000); 
set_list.update('xxx'); 
set_list.update([-3, 'add', 888]); 



myset1 = { 11, 22, 33, 44, 55}; 
myset2 = { 11, 33, 44, 66, 77}; 

myset1 | myset2; 
myset1 & myset2; 


import datetime

dt_today = '2024/01/04'; 
convert_date = datetime.datetime.strptime(dt_today, "%y/%m/%d"); 


#dictionary 

first_dic = {"name": "Anu", "age": 20, "height": 170, "weight": 50}; 
second_dic = {"name": "Tsolmon", "age": 25}; 
combined_dic = {"fist": first_dic, "second": second_dic}; 

first_dic["age"]; 