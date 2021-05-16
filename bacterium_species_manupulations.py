# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np

# %% [markdown]
# ## **Read TSV File**
# 

# %%
df = pd.read_csv('C:/Users/Sagar Singh/Desktop/chrons_taxanomic_profile (1).tsv', sep='\t')


# %%
df.head()

# %% [markdown]
# > ## **Step_1-> Row filtering based on taxonomic_profile**

# %%
contains_t = df[df['#SampleID'].str.contains("t__")]


# %%
contains_t.head()

# %% [markdown]
# > ## **Step_2-> Replacing first column with species names**

# %%
# name_extraction
import re 
def name_finder(name_col):
    r = name_col.split('|')
    for v in r:
        if v.startswith('s'):
            return v[3:]
    return None

# %% [markdown]
# >> ***making an array of names***

# %%
name_list = [name_finder(name) for name in contains_t['#SampleID']]

# %% [markdown]
# >> ***adding the arrey as a column "Name" in dataframe***

# %%
contains_t['Name'] = np.array(name_list)

# %% [markdown]
# >> ***replacing the first row with the name column***

# %%
contains_t.drop('#SampleID', inplace=True, axis=1)


# %%
contains_t.set_index('Name',inplace = True)
    


# %%
contains_t.head()


# %%
contains_t.reset_index(drop=False, inplace=True)


# %%
contains_t.head()

# %% [markdown]
# > ## **Step_3-> Grouping and sum of the rows based on common name**

# %%
t_sum = contains_t.groupby(['Name']).sum().reset_index()


# %%
t_sum.head()

# %% [markdown]
# > ## **Step_4-> Saving to csv file**
# 

# %%
# t_sum.to_csv('C:/Users/Sagar Singh/Desktop/Final_Table.csv')


