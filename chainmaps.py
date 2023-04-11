from collections import ChainMap

defaults = {'theme':'Default','language':'eng', 'showIndex':True, 'showFooter':True}
cm = ChainMap(defaults)
cm2 = cm.new_child({'theme':'Blue-Sky'})
# print(cm)
# print(cm2)
# print(cm2['theme'])
# print(cm2.maps[1])
cm2.maps[0] = {'theme':'Desert','showIndex':False}
print(cm2['showIndex'])
print(cm2.parents)