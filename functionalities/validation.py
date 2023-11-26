import pandas as pd
# import pprint

def make_plot_arrays(nodes_dict):
  lst_nodes=[]
  for i in nodes_dict:
    for ele in nodes_dict[i]:
      lst_nodes.append(ele)
  nodes =[]
  parents = []
  for i in lst_nodes:
    if(i.parent==None):
      nodes.append(i.text)
      parents.append('')
  for i in lst_nodes:
    if(i.parent!=None):
      nodes.append(i.text)
      parents.append(i.parent.text)
  
  return nodes,parents
def get_original_arrays(image_name,filename):
  df_category = pd.read_excel(filename)
  dict_category = df_category.set_index('Image Name').T.to_dict('list')
  size1 = len(dict_category[image_name][0])
  labels = dict_category[image_name][0][1:size1].split(',')
  size2 = len(dict[image_name][1])
  parents = dict_category[image_name][1][1:size1].split(',') 
  return labels,parents
  


