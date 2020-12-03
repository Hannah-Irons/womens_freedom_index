'''
FUNCTION file for Udacity Data science nanodegree: Project One - Write a Data Science Blog Post
Author: Hannah Costa

'''
import numpy as np
import matplotlib.pyplot as plt

def convert_float(dataframe):
  '''
  INPUT
    dataframe - Global variable. Any dataframe acceptable.
    col - Local variable. Used to go through all column in the dataframe.
  OUTPUT
    dataframe - Global varable. The input dataframe is replaced in the function. If the following 
    logic is a pllicable on a column level.  

  The function will cycle through each column in the dataframe and replace any dashes or spaces
  with the NaN value definition from the numpy library. If the column is numeric in nature but
  formatted as an object is will change it's datatype to a float. If the column in naturally a 
  string then the function will print "Could no concvert " followed by the column name and move
  on to the next column.

  While debugging this function and viewing the dataset, at first looks I believed all blanks in 
  the data was given by a '-' however one factor that was a scored factor was failing 
  (ef_regulation_labor_dismissal) and the currently commented out section identified the row in 
  that column that failed and that it was an empty space. 

  Therefore, if a column that you expect to able to turn into a float fails, then you can 
  uncomment the green section and rerun the function to get the row number that is failing, and 
  subsequently find out why it failed. I've kept it commented out because if the whole column
  fails for another reason then it will print every row of that column, so it's best used when
  a problem column has already been identified.   
  '''


  for col in dataframe:
    try:
      dataframe[col] = dataframe[col].replace(['-', ' '], np.NaN)
      dataframe[col] = dataframe[col].astype(float)
    except:
      # uncomment the following tree lines to debug a failing column that should be able convert.
      # for row in dataframe[col]:
      #   if not isinstance(row, float):
      #     print(row)
      print('Could not convert ' + col)

def most_missing_col(dataframe, threshold):
  '''
  INPUT
    dataframe - Global variable. The processed dataframe, with NaNs.
    threshold - The threshold for percenatge of missing values.
  OUTPUT
    missing_col_list - List of vrables that have more missing values than the threshold identified.

  The function will create a list of variables from the dataframe that have a greater percentage of
  missing values that provided by the threshold input. 
  '''

  missing_col_list = list(dataframe.columns[dataframe.isnull().mean() > threshold])

  return missing_col_list



def country_per_region(selected_region, response, dataframe):
  '''
  INPUT
    selected_region - any region defined by the dataset
    response - which variable you want to take the mean of over the region
    dataframe - the dataset that contains Region
  OUTPUT
    out_data - The aggregated mean of the reponse variable over the selected region.

  This function works well to loop over multiple regions, or variables to get the mean
  of that variable for each region. It needs to be called inside a loop. But works fine
  on its own.

'''

  out_data = dataframe[dataframe["region"] == selected_region].groupby(["countries"]).mean()[response]

  return out_data


def plot_save_Region_correlation(var_1, var_2, region):
  '''
  INPUT
    var_1 - an input variable for plotting
    var_2 - an input varaible for plotting 
    region - for a selected region
  OUTPUT
    saved plot. no global returned variable.

  This function produces and saves a graph to compare two variables for a filtered region.

  '''
  save_name = "women's_freedom_correlated_with_freedom_score_for_" + region

  plt.figure(figsize = (10,8))
  plt.subplots_adjust(bottom = 0.2)

  plt.plot(var_1, linestyle = 'solid', color ='r')
  plt.plot(var_2, linestyle='solid', color='#4b0082')
  plt.ylabel("variable score")
  plt.xlabel("country")
  plt.xticks(rotation = 90)
  plt.legend(("Human Freedom Score", "Personal woman's score"), loc='lower right')
  plt.grid(True)

  plt.title("The average personal women's freedom score aggregated for the top correlated factors. \n Region = " + region)

  plt.savefig('./results/' + save_name + '.png')
  plt.close()


def correlations_top_bottom(dataframe, region_select, var, n):
  '''
  INPUT
    dataframe - The datafram, must contain region.
    region_select - The selected region
    var - teh response variable to check correlations against
    n - number to variables to print
  OUTPUT
    Print top - Print the highest correlated factors
    Print bottom - Print the highest anti-correlated factors

  This function prints out the highest correlated and anti-correlated factors compared with a given variable.
  The number of highest factors printed is given by n.

  '''

  correlations = dataframe[dataframe["region"] == region_select].corr()
  sorted_corr = correlations[var].sort_values()

  Top = sorted_corr[-n:]
  print(Top)
  Bottom = sorted_corr[:n]
  print(Bottom)


def variable_per_region(selected_region, var, response, dataframe):
  '''
  INPUT
    selected_region - Region of interest
    var - correlated variable of interest
    response - the orginal variable it was checked for correlations against. 
  OUTPUT
    out_data - the relation ship between the correlated pair for a selected region.

  This function gives the mean value of the correlated factor to the response factor for a
  given region so that they can be plotted before potential modelling.

'''

  out_data = dataframe[dataframe["region"] == selected_region].groupby([var]).mean()[response]

  return out_data

