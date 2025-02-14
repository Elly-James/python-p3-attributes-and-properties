#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
     def __init__(self, name="SmokingMirror", job="Sales"):
          if isinstance(name, str) and 1 <= len(name) <= 25:
              self._name = name.title()
          else:
              print("Name must be string between 1 and 25 characters.")
              self._name = "Sir Elly".title()

          if job in APPROVED_JOBS:
              self._job = job
          else:
              print("Job must be in list of approved jobs.")
              self._job = "Freelancer"

     def get_name(self):
         return self._name
     
     def set_name(self, name):
         if isinstance(name, str) and 1 <= len(name) <= 25:
             self._name = name.title()
         else:
             print("Name must be string between 1 and 25 characters.")

     def get_job(self):
         return self._job
     
     def set_job(self, job):
         if job in APPROVED_JOBS:
             self._job = job
         else:
             print("Job must be in list of approved jobs.")
        
     name = property(get_name, set_name)
     job = property(get_job, set_job)

    
person = Person()
print(person.name)  
print(person.job)  

person.name = "Ja Koyundi"
person.job = "Ja Nam"
print(person.name)
print(person.job)

person.name = "Koyundi.254"
person.job = "Ja Omena"


    

    
