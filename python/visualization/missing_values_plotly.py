# Missing values 시각화_plotly
def missing_values_vis(df, height = 900, width = 800):
  temp = list(df.isna().sum())

  #then we create a list of columns and their missing values as inner list to a separate list
  lst= []
  for i, col in enumerate(df.columns):
    lst.append([col,temp[i]])

  #finally create a dataframe
  temp_df = pd.DataFrame(data=lst,columns=['Column_Name','Missing_Values'])

  # create bar plots with their missing values
  fig = px.bar(temp_df[temp_df['Missing_Values'] > 0].sort_values(by = 'Missing_Values'),
               x = 'Missing_Values', y = 'Column_Name', orientation = 'h', 
               height = height, width = width, color = 'Missing_Values',
               text = 'Missing_Values', title = 'Missing values in the dataset')
  fig.update_traces(textposition = 'outside')
  fig.show()
