#list&tuple

s3_bucket_lists = ["rahul_demo_bucket","ram_demo_bucket","tim_demo_bucket","john_demo_bucket"]
print(type(s3_bucket_lists))
# s3_bucket_lists.remove("ram_demo_bucket")
print(s3_bucket_lists)
print(s3_bucket_lists[2])
print(len(s3_bucket_lists))


# ['rahul_demo_bucket', 'ram_demo_bucket', 'tim_demo_bucket', 'john_demo_bucket', 'new_demo_bucket']
# PS C:\Users\> & C:/Python/python.exe "c:/Users/rahul/OneDrive/Desktop/DevOps/Python/DevOps_1_Python/Day 8/list_tuples_diff.py"
# <class 'tuple'>
# Traceback (most recent call last):
#   File "c:\Users\rahul\OneDrive\Desktop\DevOps\Python\DevOps_1_Python\Day 8\list_tuples_diff.py", line 5, in <module>
#     s3_bucket_lists.append("new_demo_bucket")
#     ^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'tuple' object has no attribute 'append

new_list  = s3_bucket_lists[1:3]
print(new_list)