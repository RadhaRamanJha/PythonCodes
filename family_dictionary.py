import collections
# importing collections to convert thess dictionary into a list of dictonaries
kameshwar_jha = {'age':65, 'Qualification':'Msc'}
manjula_jha = {'age' : 55, 'Qualification':"Uttaaar Madhyama"}
bandana_mishra = {'age': 40, 'Qualifion':"Btech CSE"}
keshav_jha = {'age' : 35, 'Qualification':"Btech CSE"}
radha_jha = {'age' : 33, 'Qualification':"Python learner"}
family_members = collections.ChainMap(kameshwar_jha,manjula_jha,bandana_mishra,keshav_jha) 
# collections.ChainMap(a,b,c) converts a,b,c dictionaries into a list of dictionaries
print(family_members.maps)
print(family_members.keys())
print(family_members.keys)
print(list(family_members.keys()))
print(list(family_members.values()))
print(family_members.values())
family_members.new_child(radha_jha) # new_child() works only when assigned 
print(family_members.maps)
print(family_members.maps)
print(family_members.keys())
print(family_members.values())
updated_family_members = family_members.new_child(radha_jha)
print(updated_family_members.maps)
print(list(updated_family_members.keys()))
print(list(updated_family_members.values()))