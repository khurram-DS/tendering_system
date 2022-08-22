import streamlit as st
# Eda packages

import pandas as pd
import numpy as np

#Data viz packages

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

#function

def main():
    
    title_container1 = st.container()
    col1, col2 ,  = st.columns([6,12])
    from PIL import Image
    image = Image.open('static/asia.jpeg')
    with title_container1:
        with col1:
            st.image(image, width=200)
        with col2:
            st.markdown('<h1 style="color: red;">ASIA Consulting</h1>',
                           unsafe_allow_html=True)
    
    
    
    
    st.sidebar.image("static/BMI.jpg", use_column_width=True)
    activites = ["About","Expanding columns"]
    choice =st.sidebar.selectbox("Select Activity",activites)
    
    st.text('------------------------------------------------------------------------------------------------------------------------------')
    

    if choice == "About":
        st.subheader("About ACS")
        st.text("""ACS is a consulting company specialized in data analysis was established during 2010. Our mission is to clarify the right direction for business owners in order to get better business results using very advanced statistical approaches, also, to support postgraduate students to prove their finding using academic statistical analysis. Providing the work in a high level of quality is one of our important goals. Our future vision is to be a leader in 
business analytics advisor for all successful business owners.
Our qualified staff is our strength of many of our successful projects. 
ACS did more than 100 successful projects since 2010/11. We are focusing on providing a 
sophisticated work with co-operated with our international parter. ACS has an international
agreement with Statistics Solutions (Ltd.) to be authorized for selling a statistical 
package in the GCC region, and that makes ACS more credible in statistical performance.""")
        
        

        st.write("**This Project is for expanding columns values to multiple row and and the value to different columns**")
        
 
        
        st.text('© Asia Consulting for Statistics')
#overall analysis    
    elif choice == "Expanding columns":

        st.subheader("Expanding columns")
        

        st.text('------------------------------------------------------------------------------------------------------------------------------')
        
        
        st.text('Upload the files to only fix the Dates')
        
        
    
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        st.write("**Data has been loaded Successfully**")
        
        df = get_df(file)
        if st.checkbox("Show Raw Data"):
            st.write(df)
        
        
        st.write("**Expanding columns to different rows and columns**")
        if st.checkbox("Lets Expand columns to different rows and columns"):
            
            st.subheader("Treat your columns")
            
            all_columns=df.columns.to_list()
            selected_columns= st.selectbox("Select Columns You want to fix", all_columns)
            #df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            if st.checkbox("Click to Expand the columns"):
                data=[]
                data = df[selected_columns].str.split('\n',expand=True).stack().reset_index().merge(df.reset_index(),left_on ='level_0',right_on='index').drop(['level_0','level_1','index'],1)
                data['Each Configurable list']=data[0]
                data['Name of the co-contractor']=(data[0].str.split(':').str[1])
                data['Name of the co-contractor']=data['Name of the co-contractor'].str.replace(', Contractor number'," ")
                data['Contractor number']=(data[0].str.split(':').str[2])
                data['Contractor number']=data['Contractor number'].str.replace(', Winner'," ")
                data['Winner']=(data[0].str.split(':').str[3])
                data['Winner']=data['Winner'].str.replace(', Price Offer'," ")
                data['Price Offer']=(data[0].str.split(':').str[4])
                
                data = data.drop(0, axis=1)
                st.write(data)

                
        
                import base64
                import io
                towrite = io.BytesIO()
                downloaded_file = data.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
                towrite.seek(0)  # reset pointer
                b64 = base64.b64encode(towrite.read()).decode() 
                linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="Tendering_system_database_expanded.xlsx">Download excel file</a>'
                st.markdown(linko, unsafe_allow_html=True)
        
        
      

if __name__=='__main__':
    main()
