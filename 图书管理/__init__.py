comment_list= [
   {'id':1,'content':'xxx','parent_id':None},
   {'id':2,'content':'xxx','parent_id':None},
   {'id':3,'content':'xxx','parent_id':None},
   {'id':4,'content':'xxx','parent_id':1},
   {'id':5,'content':'xxx','parent_id':4},
   {'id':6,'content':'xxx','parent_id':2},
   {'id':7,'content':'xxx','parent_id':5},
   {'id':8,'content':'xxx','parent_id':3},
    ]


comment_dict={}
for row in comment_list:
   comment_dict[row['id']]=row


for row in  comment_list:
    row['child']=[]
    if row['parent_id']:
        comment_dict[row['parent_id']]['child'].append(row)


for item in comment_list:
    print(item)
