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
	"""Semi Automated ML App with Streamlit """

	activities = ["EDA","Plots"]	
	choice = st.sidebar.selectbox("Select Activities",activities)
	import matplotlib.pyplot as plt
	# line 1 points
	x1 = [10,20,30]
	y1 = [20,40,10]
	# plotting the line 1 points 
	plt.style.use('seaborn-darkgrid')
	plt.plot(x1, y1, marker='o', markersize=10, linewidth=2, label = "line 1")
	# line 2 points
	x2 = [10,20,30]
	y2 = [40,10,30]
	# plotting the line 2 points 
	plt.plot(x2, y2, marker='o', markersize=10, linewidth=2, label = "line 2")
	plt.xlabel('x - axis')
	# Set the y axis label of the current axis.
	plt.ylabel('y - axis')
	# Set a title of the current axes.
	plt.title('Two or more lines on same plot with suitable legends ')
	# show a legend on the plot
	plt.legend()
	# Display a figure.
	fig ,ax  = plt.subplots()
	st.pyplot(fig)
	plt.show()
	if choice == 'EDA':
		st.subheader("Exploratory Data Analysis")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
		if data is not None:
			df = pd.read_csv(data)
			itemList = df['Item']
			options = st.multiselect('Select items to compare',itemList)
			if st.button("show chart"): 
				selectedDf = df[df['Item'].isin(options)]
				st.dataframe(selectedDf)
				df = selectedDf.transpose()
				df = df.drop(['Item','Website','Quantity']) 
				st.line_chart(df)

	elif choice == 'Plots':
		st.subheader("Data Visualization")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())


			if st.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
				st.pyplot()
		
			# Customizable Plot

			all_columns_names = df.columns.tolist()
			type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
			selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

			if st.button("Generate Plot"):
				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

				# Plot By Streamlit
				if type_of_plot == 'area':
					cust_data = df[selected_columns_names]
					st.area_chart(cust_data)

				elif type_of_plot == 'bar':
					cust_data = df[selected_columns_names]
					st.bar_chart(cust_data)

				elif type_of_plot == 'line':
					cust_data = df[selected_columns_names]
					st.line_chart(cust_data)

				# Custom Plot 
				elif type_of_plot:
					cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
					st.write(cust_plot)
					st.pyplot()


	


if __name__ == '__main__':
	main()
