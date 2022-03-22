

import cobra
from cobra import *

# In[2]:


model=Model('model_1')


# In[3]:


v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1

v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000

v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000

v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=.9
v3.upper_bound=.9

v4=Reaction('v4')
v4.name='v4'
v4.lower_bound=0
v4.upper_bound=1000

M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[4]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[5]:


v1.add_metabolites({A:-1,B:1})

v2.add_metabolites({B:-1,C:1})

v0.add_metabolites({A:1})

M.add_metabolites({C:-1})

v3.add_metabolites({A:-1,ATP:1})

v4.add_metabolites({ATP:-1})

model.add_reactions([v0,v1,v2,v3,v4,M])
model.objective='M'
model.optimize()


# In[6]:


model.summary()


# In[7]:


cobra.io.save_json_model(model,"task2.json")


# In[8]:


cobra.io.load_json_model("task2.json")


# In[9]:

import escher
from escher import Builder

builder = Builder()


# In[10]:


builder


# In[ ]:




