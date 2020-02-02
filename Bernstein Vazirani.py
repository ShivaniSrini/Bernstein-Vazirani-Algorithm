#!/usr/bin/env python
# coding: utf-8

# In[6]:


from qiskit import *
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.visualization import plot_histogram


# In[11]:


secretnumber = '11001'


# In[17]:


circuit = QuantumCircuit(len(secretnumber)+1, len(secretnumber))

#circuit.h([0,1,2,3,4,5])
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))

circuit.barrier()

circuit.draw(output = 'mpl')

for ii, yesno in enumerate(reversed(secretnumber)):
    if yesno== '1':
        circuit.cx(ii, len(secretnumber))

circuit.barrier()

circuit.h(range(len(secretnumber)))

circuit.barrier()
circuit.measure(range(len(secretnumber)),range(len(secretnumber)))


# In[13]:


circuit.draw(output = 'mpl')


# In[14]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1).result()
counts = result.get_counts()
print(counts)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




