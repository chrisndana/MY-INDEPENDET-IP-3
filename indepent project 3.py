#!/usr/bin/env python
# coding: utf-8

# In[1]:


minutes=int(input("enter minutes here"))
messeges=int(input("enter messeges here"))
base_charge=50
minutes_additional_charge=3*(minutes-20)
messeges_additional_charge=2*(messeges-20)
tax_1=0.16*(base_charge+minutes_additional_charge+messeges_additional_charge)
total_cost_1=tax_1+base_charge+minutes_additional_charge+messeges_additional_charge
if minutes<=20 and messeges<=20:
    print(base_charge+(0.16*50))
elif (minutes<20 and messeges>20):
    tax_2=.16*(base_charge+messeges_additional_charge)
    total_cost_2=(base_charge+messeges_additional_charge+tax_2)
    print(total_cost_2)
elif (minutes>20 and messeges<20):
    tax_3=.16*(base_charge+minutes_additional_charge)
    total_cost_3=(base_charge+minutes_additional_charge+tax_3)
    print(total_cost_3)
else:
    print(total_cost_1)


# In[ ]:




