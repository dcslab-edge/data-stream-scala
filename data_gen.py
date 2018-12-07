#usr/bin/python3.7
#coding: UTF-8

import argparse
import os
import random
import string
import json
from pathlib import Path


class saveable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            with open(prospective_dir, 'w'): pass
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace,self.dest,prospective_dir)
        else:
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))

class dataType:
    def __init__(self,data_name:string,data_type:string,data_count:int,data_length:int=100):
        self._data_name=data_name
        self._data_type=data_type
        self._data_count=data_count
        self._data_length=data_length
    def __str__(self):
        return '{'+self._data_name+'}['+self._data_type+']('+str(self._data_length)+')'



class dataGenerator:
    def __init__(self,data_count:int,data_types=[]):
        self._data_count = data_count
        self._data_types = data_types
    def __init__(self,data_cfg={}):
        self._data_types=[]
        self._data_count = data_cfg["maximum_data_count"]
        major_length = data_cfg["major_data_type"]
        major_type = data_cfg["major_data_length"]
        specific_len=len(data_cfg["specific_data_types"])
        for d in data_cfg["specific_data_types"] :
            self._data_types.append(dataType(d["type"],d["count"],d["length"]))
        self._data_types.append(dataType(major_type,specific_len,major_length))

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
        seen = set()

        # An optimization for tightly-bound loops:
        # Bind these methods outside of a loop
        join = ''.join
        add = seen.add

        while len(seen) < ntokens:
            token = join(random.choices(pool, k=k))
            add(token)
        return seen


    def generateData(self):

        data_ret = {}
        
        for dt in self._data_types :
            print(dt)
            if dt._data_type == "int"  :
                data_ret[dt._data_name]=random.randrange(1,dt._data_length)
            elif dt._data_type == "string" :
                data_ret[dt._data_name]=self.unique_strings(dt._data_length,1)
            elif dt._data_type == "long" :
                data_ret[dt._data_name]=random.randrange((dt._data_length/10000)+1,dt._data_length)
        print(data_ret)
        return data_ret
            






def main() :
    parser = argparse.ArgumentParser(description='Create Random datastrean written in data.config.json file format')
    parser.add_argument('config_dir', metavar='PARENT_DIR_OF_CONFIG_FILE', type=str, nargs='+',
                    help='Directory path where the config file (data.config.json) exist. (support wildcard *)')
    #parser.add_argument('-s','--save',action=saveable_dir,help='save data in specified path')
    args = parser.parse_args()
    #save_path =args.save

    data_cfg:Path = Path(args.config_dir[0]) / "data.config.json"
    data_sav:Path = Path(args.config_dir[0]) / "data.json"
    with open(data_cfg) as f:
        cfg = json.load(f)
        generator = dataGenerator(cfg)
        generator.generateData()
        #{'maximum_data_count': 10, 'major_data_type': 'int', 'specific_data_types': [{'type': 'long', 'count': 1}, {'type': 'string', 'length': 25, 'count': 1}]}



    sav=open(data_sav,'w')



if __name__=='__main__' :
    main()
