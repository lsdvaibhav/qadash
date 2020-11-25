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

	if choice == 'EDA':
		st.subheader("Exploratory Data Analysis")
		import matplotlib.pyplot as plt
		import pandas as pd

		# initialize list of lists 
		data = [['item1',16,16,16,16,18,16,18], ['item2',15,15,15,14,15,14,15], ['item3', 14,14,14,14,13,14,13]] 

		# Create the pandas DataFrame 
		df = pd.DataFrame(data, columns = ['Item','d1','d2','d3','d4','d5','d6','d7']) 
		x = ['d1','d2','d3','d4','d5','d6','d7']
		for index in df.index:
		  y = [df.loc[index]['d1'],df.loc[index]['d2'],df.loc[index]['d3'],df.loc[index]['d4'],df.loc[index]['d5'],df.loc[index]['d6'],df.loc[index]['d7']]
		  label = df.loc[index]['Item']
		  # plotting the line 1 points 
		  plt.plot(x,y, label = label)


		plt.xlabel('Dates')
		# Set the y axis label of the current axis.
		plt.ylabel('Prices')
		# Set a title of the current axes.
		plt.title('More than one items are compared')
		# show a legend on the plot
		plt.legend()
		# Display a figure.
		plt.show()
		
		df = df.transpose()
		
		st.line_chart(df)
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
		if data is not None:
			df = pd.read_csv(data)

			itemList = df['Item']

			options = st.multiselect('Select items to compare',itemList)
			if len(options) != 0: 
				st.write('You selected:', options)
			
				selectedDf = df['Item'].isin(options)
				selectdDf.set_index('Item')
				selectedDf = selectedDf[:,4:]

				st.dataframe(selectedDf)
				df = selectedDf.transpose()
				st.line_chart(df)
			df = pd.read_csv(data)
			st.dataframe(df.head())

			if st.checkbox("Show Shape"):
				st.write(df.shape)

			if st.checkbox("Show Columns"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			if st.checkbox("Summary"):
				st.write(df.describe())

			if st.checkbox("Show Selected Columns"):
				selected_columns = st.multiselect("Select Columns",all_columns)
				new_df = df[selected_columns]
				st.dataframe(new_df)

			if st.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts())

			if st.checkbox("Correlation Plot(Matplotlib)"):
				plt.matshow(df.corr())
				st.pyplot()

			if st.checkbox("Correlation Plot(Seaborn)"):
				st.write(sns.heatmap(df.corr(),annot=True))
				st.pyplot()


			if st.checkbox("Pie Plot"):
				all_columns = df.columns.to_list()
				column_to_plot = st.selectbox("Select 1 Column",all_columns)
				pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
				st.write(pie_plot)
				st.pyplot()



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
