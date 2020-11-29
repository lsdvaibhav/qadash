# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 


# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 


def main():
	"""Semi Automated analysis App with Streamlit """
	st.subheader("Exploratory Data Analysis")
	data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
	if data is not None:
		df = pd.read_csv(data , error_bad_lines=False)
		itemList = df['Item']
		options = st.multiselect('Select items to compare',itemList)
		if st.button("show chart"): 
			selectedDf = df[df['Item'].isin(options)]
			st.dataframe(selectedDf)
			dff = selectedDf.drop(['Item','Website','Quantity'] , axis = 1)
			df = dff.transpose()
			df = df.replace({'-': None})
			df = df.astype(float)
			df = df.fillna(df.mean())
			st.line_chart(df)
if __name__ == '__main__':
	main()
