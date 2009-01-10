# -*- coding: utf-8 -*-
import e32
import os
import e32dbm
from wmglobals import DEFDIR

class Persist(dict):
    __highlander = None
    DBNAME = os.path.join(DEFDIR,"wordmobi")
    DEFVALS = {"user":u"username",
               "pass":u"password",
               "blog":u"http://blogname.wordpress.com",
               "email":u"",
               "realname":u"",
               "num_posts":u"10",
               "num_comments":u"20",
               "categories":u"",
               "proxy_user":u"",
               "proxy_pass":u"",
               "proxy_addr":u"",
               "proxy_port":u"8080",
               "proxy_enabled":u"False"}
    
    def __init__(self):
        if Persist.__highlander:
            raise Persist.__highlander
        Persist.__highlander = self
        
        dict.__init__(self)
        
        self.load()
            
    def save(self):
        db = e32dbm.open(Persist.DBNAME,"c")
        for k in Persist.DEFVALS.iterkeys():
            db[k] = self.__getitem__(k)
        db.close()

    def load(self):
        try:
            db = e32dbm.open(Persist.DBNAME,"w")
        except:
            db = e32dbm.open(Persist.DBNAME,"n")
            
        for k in Persist.DEFVALS.iterkeys():
            try:
                self.__setitem__(k,utf8_to_unicode( db[k] ))
            except:
                self.__setitem__(k,Persist.DEFVALS[k])
        db.close()
