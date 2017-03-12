
# coding: utf-8

# #### Introduccion a la teoria de la computacion
# 
# ##### Taller #1 - Automatas finitos
# 
# 1.Considere el problema de determinar si un código corresponde a un ISBN de 13 dígitos. Construya un autómata finito determinístico para identificar si un código es válido o no. Especifique formalmente el autómata, dibuje el diagrama y la tabla de transiciones. Implemente el autómata correspondiente utilizado una clase autómata.
# 
# 
# 2.Construya un autómata finito determinístico sobre el alfabeto $\{a,b\}$ la cual acepte todas las cadenas que contengan NO más de dos ocurrencias consecutivas de la misma entrada (Por ejemplo, abba es aceptada y abbba no es aceptada). Especifique formalmente el autómata, dibuje el diagrama y la tabla de transiciones. 
# 
# <script>console.log("hola")</script>

# In[22]:

import networkx as nx
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


# In[49]:

G = nx.DiGraph()
G.graph['rankdir'] = 'LR' #Left to Right
G.graph['dpi'] = 250 #(dots per inch) 
G.add_cycle(range(4))
G.add_node(0, color='red')
G.add_node(1, shape='doublecircle')
G.add_node(3, shape='circle')
G.add_edge(3,3,label='a')
draw(G)



# In[62]:

H=nx.path_graph(10)
G = nx.DiGraph()
G.add_nodes_from(H)
G.add_edges_from([(4,8),(1,3),(1,0),(5,3),(6,3),(7,0),(1,4),(9,8),(8,2),(9,7),(3,9)])
G.graph['dpi'] = 300 
G.graph['rankdir'] = 'LR'
draw(G, show='ipynb')


# $$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$$

# ##### Jesus Felipe Chavarro Muñoz
