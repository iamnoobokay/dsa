class Hashtable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        
        # table = ['p','r','a','n','a','v']
        # hash_value = 3
        # for i,item in enumerate(table[hash_value]):
        #     print (table[hash_value])
        #     print('hash value is '+str(hash_value))
        #     print('value of i is '+str(i))
        #     print('value of item is '+str(item))
    
    def _hash_function(self,key):
        # print(hash(key))
        # print(hash(key) % self.size)
        return hash(key) % self.size
    
    def insert(self,key,value):
        hash_value = self._hash_function(key)
        print(hash_value)
        print(key)
        print(value)
        for i,item in enumerate(self.table[hash_value]):
            if item[0] == key:
                # print('i was here too')
                self.table[hash_value][i] = (key,value)
        self.table[hash_value].append((key,value))
        
    def delete(self,key):
        hash_value = self._hash_function(key)
        print(hash_value)
        for i,item in enumerate(self.table[hash_value]):
            if item[0] == key:
                del self.table[hash_value][i]
                return
        
htable = Hashtable()
arr = ['p','r','a','n','a','v']

for i,a in enumerate(arr):
    # print('the value of i is '+str(i))
    # print('the value of a is '+str(a))
    htable.insert('0',a)


print(htable.table)
htable.delete('1')
print(htable.table)
# htable._hash_function('1')
# htable.insert("1k","prnav")