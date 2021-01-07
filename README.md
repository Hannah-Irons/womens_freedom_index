## Udacity Data Science nanodegree: Write a Data Science Blog Post

# An analysis into Women's Freedom using the Human Freedom Index

## Installation

Python 3.8.5 64 bit

Libraries used:
- numpy
- pandas
- os
- matplotlib.pyplot
- sklearn

## Motivation

Freedom is a difficult thing to quantify; it has no units and can't be measured, but it can be categorised and even defined in a way that can be comparable between countries. The Human freedom Index sets a scale of 0-10 for it's freedom factors, they are split into Pesonal freedoms and Econmic Freedoms. The motivations for this project is to single out and analyse Women's freedom and wondering if an inherently 'free' country means it's free for everybody.  

## File descriptions

- run_file.py
The run_file is the core script of this project. It os where the csv datafile for the 2019 Human Freedom Index is gathered, assessed, processed and analysed. To clean an analyse the data the run_file calls functions from the function_file. 

- function_file.py
The function_file contains each function and function description that is used in run_file. 

- /data/datasets_93172_883723_hfi_cc_2019.csv
2019 data from the Human Freedom Index resourced from Kaggle
LINK: https://www.kaggle.com/gsutters/the-human-freedom-index

- /results
All plots created, formatted and saved by this project.