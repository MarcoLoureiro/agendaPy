#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Schedule:
    
    def __init__(self):
        self.__contacts = []
    
    def read_contacts(self):
        with open('contacts.txt','r',encoding='UTF-8') as file:
            for l in file:
                print(f"{l.rstrip()}")
        
    def add_contact(self,data):
        with open('contacts.txt','w',encoding='UTF-8') as file:
            self.__contacts.append(data)
#             file.write(self.__contacts)
            for i in self.__contacts:
                file.write(f"{i}\n")
            
    def remove_contact(self,name):

        for i in self.__contacts:
            infos = i.split(',')
            name_temp = infos[0]
            if(name==name_temp):
                self.__contacts.remove(i)
                print(f"{name} removed!")
                with open('contacts.txt','w',encoding='UTF-8') as file:
                    for i in self.__contacts:
                        file.write(f"{i}\n")
                return
            
        print("Not found")
            



