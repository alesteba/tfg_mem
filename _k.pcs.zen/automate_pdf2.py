#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from weasyprint import HTML

HTML('https://alesteba.github.io/tfg/').write_pdf('test_out.pdf') 

