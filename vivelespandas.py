
# coding: utf-8

# ## Le titre de mon carnet

# In[1]:

get_ipython().magic('matplotlib inline')


# In[2]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib as mp


# In[3]:

md = pd.read_csv("cmq.csv")


# In[49]:

pd.set_option("display.float_format", lambda x : "%.2f" % x)


# In[4]:

md


# In[5]:

md.shape


# In[6]:

md.head()


# In[7]:

md.tail()


# In[8]:

md[1000:1010]


# In[9]:

md.loc[7000:7010,["nom", "prenom", "num"]]


# In[10]:

md.iloc[10000:10011, 0;4]


# In[11]:

md.iloc[10000:10011,0:4]


# In[12]:

md.columns


# In[13]:

md.columns = ['num', 'annee', 'prenom', 'nom', 'genre', 'specialite1', 'specialite2',
       'specialite3', 'statut', 'date', 'typePermis', 'ville',
       'prov', 'pays']


# In[14]:

md


# In[15]:

md.dtypes


# In[16]:

md.count()


# In[17]:

md.loc["Labrèche"]


# In[18]:

md.loc[5]


# In[19]:

md.loc(5)


# In[20]:

md.loc["Blais"]


# In[21]:

md.iloc[5]


# In[22]:

md.loc[0:35109, [5, "Labrèche"]]


# In[23]:

md.loc[0:35109, [5]]


# In[24]:

mil = pd.read_csv("militaires.csv")


# In[25]:

mil


# In[26]:

mil.montant.max()


# In[27]:

mil.montant.min()


# In[28]:

mil.montant.sum()


# In[29]:

mil.montant.mean()


# In[30]:

mil.montant.median()


# In[31]:

mil.montant.average()


# In[32]:

md.genre.value_counts()


# In[33]:

md.genre.value_counts() / len(md.genre)*100


# In[34]:

md.nom.value_counts()


# In[35]:

md.prenom.value_counts()


# In[36]:

md.nom.value_find("Labrèche")


# In[37]:

md.nom_find("Labrèche")


# In[38]:

md.nom.value_get("Labrèche")


# In[39]:

md.nom()


# In[40]:

mil.fournisseurs


# In[41]:

mil.fournisseur.value_counts()


# In[44]:

mil.groupby("fournisseur").montant.sum()


# In[50]:

mil.groupby("fournisseur").montant.sum().sort_values(ascending=False)


# In[51]:

mil.groupby("fournisseur").montant.sum().sort_values(ascending=False)


# In[54]:

md.statut.value_counts()


# In[55]:

rad = md.statut == "Radié"


# In[57]:

md[rad]


# In[58]:

md[rad].genre.value_counts()


# In[59]:

lab = md.prenom == "Labrèche"
md[lab]


# In[60]:

lab = md.nom == "Labrèche"
md[lab]


# In[62]:

mimi = md.prenom == "Myriam"
md[mimi]


# In[67]:

md[actifs].pays.value_counts()


# In[66]:

actifs = md.statut.str.contains("Actif")


# In[75]:

famille = md[actifs].specialite1 == "Médecine de famille"
md[actifs][famille]


# In[79]:

md[actifs][famille].genre.value_counts().plot(kind="pie",title="Le genre des médecins de famille actifs au Québec")


# In[82]:

md.annee.hist(bins=87)


# In[85]:

md.groupby("genre").annee.hist(bins=87,alpha=0.5)


# In[98]:

mil.groupby("annee").montant.sum().plot(kind="barh",color="pink")


# In[ ]:



