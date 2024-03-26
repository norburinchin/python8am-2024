# data={}
# key value
# data={
#     'name':"kunsang",
#     "age":27
# }
# print(data['address']['city'])
# students=[
#     {
#         'name':"ram",
#       "country":[
#          {
#         'name':"nepal",
#         'capital':"ktm"
#     }
#       ]
#     },
  
   



# {
#     'name':"sita",
#     "country":[
#         {
#             'cname':"nepal",
#             'capital':"pokhara"
#         }
#     ]
# },
# {
#     'name':"kunsang",
#     "country1":[
#         {
#             'cname':"china",
#             'capital':"beijing"
#         }
#     ]
# }
# ]
# students=[
#     {
#         'name':"ram",
#         "country":[
#             {
#                 'cname':"nepal",
#                 'capital':"ktm"
#             },
#             {
#                 'name':"india",
#                 'capital':"delhi"
#             }
#         ]
        
#     },
#     {
#         'cname':"sita",
#         "country":[
#             {
#                 'name':"nepal",
#                 'capital':"ktm"
#             },
#             {
#                 'name':"china",
#                 'capital':"beijing"
#             }
#         ]
#     }
# ]
# print(students[0]['name'])
# print(students[0]['country'][0]['cname'])
# print(students[0]['country'][1]['cname'])

# data=[
#     ['ram','sita','gita'],
#     ['nepal',['india'],'china'],

# {'name':"hari"}
# ]
# print(data['name'])
# ========================================#
# product={
#     'quantity':5,
#     'price':350
# }
# print(product.keys())
# print(product.values())
# print(product['name'])
# print(product.get("price","key not found"))
# print('hello')
#  print(product.keys())
# users={
#     'name':'ram',
#     'address':{
#         'city':'ktm',
#         'state':'bagmati'
#     }
# }
# print(users['address']['city'])
students=[
    {
        'name':"my name is ram",
        "country":[
            {
                'name':"I am from nepal",
                'capital':"ktm"
            },
            {
                'cname':"india",
                'capital':"delhi"
            }
        ]
        
    },
    {
        'name':"my name is sita",
        "country":[
            {
                'name':"nepal ",
                'capital':"pokhara"
            },
            {
                'name':"i am from china",
                'capital':"my is sister is from beijing"
            }
        ]
    }
]
print(students[0]['name'])
print(students[0]['country'][0]['name'])
print(students[1]['name'])
print(students[1]['country'][1]['name']['capital'])


# data=[
#     ['ram','sita','gita'],
#     ['nepal',['india'],'china'],
#     {'name':"hari"}

# ]
# print(data[0][0])
# print(data[1][1])
# print(data[2]['name'])