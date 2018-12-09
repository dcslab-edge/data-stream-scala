import os
import random
import string

class dataType:
    def __init__(self,data_type:string,data_count:int,data_length:int=100):
        self._data_type=data_type
        self._data_count=data_count
        self._data_length=data_length
        # def __str__(self):
        #     return "{"+self._data_name+"}["+self._data_type+"]("+str(self._data_length)+")"



class dataGenerator:
    def __init__(self,data_count:int,data_types=[]):
        self._data_count = data_count
        self._data_types = data_types
    def __init__(self,data_cfg={}):
        self._data_types=[]
        self._data_count = data_cfg["maximum_data_count"]
        major_length = data_cfg["major_data_length"]
        major_type = data_cfg["major_data_type"]
        specific_len=0
        for d in data_cfg["specific_data_types"] :
            self._data_types.append(dataType(d["type"],d["count"],d["length"]))
            specific_len+=d["count"]
        print("major")
        print(major_type)
        print(specific_len)
        print(major_length)
        self._data_types.append(dataType(major_type,self._data_count-specific_len,major_length))
        print(self._data_types)

    def add_data_types(self,data_type:dataType):
        self._data_types.append(data_type)

    def unique_strings(self,k: int, ntokens: int,
                       pool: str=string.ascii_letters) -> set:
        """Generate a set of unique string tokens.

        k: Length of each token
        ntokens: Number of tokens
        pool: Iterable of characters to choose from

        For a highly optimized version:
        https://stackoverflow.com/a/48421303/7954504
        """
        seen = list()

        # An optimization for tightly-bound loops:
        # Bind these methods outside of a loop
        join = ''.join
        add = seen.append

        while len(seen) < ntokens:
            token = join(random.choices(pool, k=k))
            add(token)
        return seen[0]

    def data_stringify(self,data):
        ret=""
        for i in data:
            for k,v in i.items():
                ret+=k+":"+str(v)+" "
        return ret

    def generateData(self):

        data_ret = []
        print(self._data_types)
        print(len(self._data_types))
        for dt in self._data_types :
            print(dt._data_type)
            if dt._data_type == "int" :
                for i in range(0,dt._data_count) :
                    data_ret.append({dt._data_type+str(i):random.randrange(1,dt._data_length)})
            elif dt._data_type == "string" :
                for i in range(0,dt._data_count) :
                    data_ret.append({dt._data_type+str(i):self.unique_strings(dt._data_length,1)})
            elif dt._data_type == "long" :
                for i in range(0,dt._data_count) :
                    data_ret.append({dt._data_type+str(i):random.randrange((dt._data_length/10000)+1,dt._data_length)})
        return self.data_stringify(data_ret)
