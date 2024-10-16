import streamlit as st
import pandas as pd
import pymysql
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="RedBus by Sakthi", layout='wide', initial_sidebar_state='expanded')
st.markdown(
    """
    <style>
    .stSidebar {
        background-color: IndianRed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def get_data_from_db():
    
    host = 'localhost'
    user = 'root'
    password = 'root123'
    database = 'red_bus'

    
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    try:
        
        query = """
        SELECT Bus_name, Bus_type, Start_time, End_time, Total_duration, 
               Price, Seats_Available, Ratings, Route_link, Route_name, State_Name
        FROM bus_details
        """
        
        
        df = pd.read_sql(query, connection)
        
    finally:
        
        connection.close()
    
    return df

df = get_data_from_db()
#print(df)  # Display the fetched data

if 'menu' not in st.session_state:
    st.session_state['menu'] = 'home'

# Sidebar menu buttons
st.sidebar.title("Main Menu")
if st.sidebar.button("Home"):
    st.session_state['menu'] = 'home'
if st.sidebar.button("Select the Bus"):
    st.session_state['menu'] = 'select_bus'
if st.sidebar.button("For Booking"):
    st.session_state['menu'] = 'booking'
if st.sidebar.button("Feedback"):
    st.session_state['menu'] = 'feedback'

st.title("RedBus Ticket Booking")
st.subheader("India's No. 1 Online Bus Ticket Booking Site")

image_url = "https://s3.rdbuz.com/Images/rdc/rdc-redbus-logo.svg"
st.markdown(
    f'<img src="{image_url}" style="width: 7rem; height: 5rem; cursor: pointer;">',
    unsafe_allow_html=True
)


if st.session_state['menu'] == 'home':
    st.info("""Project Done By: Sakthi Krishnakumar     
            Batch ID: MDT40         
            Contact No: 9150991467          
            Email ID: devisri55871@gmail.com            
            """)
    #st.info("Click Home button to know the project details")
    st.markdown("[For more about the project click here my GitHub account](https://github.com/sakthi1810/Redbus---Scraping-data)")

    st.subheader("Project Title:")
    st.write("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader("Skills Takeaway From This Project:")
    st.write("Web Scraping using Selenium, Python, Streamlit, SQL")
    st.subheader("Domain")
    st.write("Transportation")
    st.subheader("Approach:")
    st.subheader("Data Scraping:")
    st.write("Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.")
    st.subheader("Data Storage:")
    st.write("Store the scraped data in a SQL database.")
    st.subheader("Streamlit Application:")
    st.write("""Develop a Streamlit application to display and filter the scraped data.         
Implement various filters such as bustype, route, price range, star rating, availability.""")
    st.subheader("Data Analysis/Filtering using Streamlit:")
    st.write("""Use SQL queries to retrieve and filter data based on user inputs.           
Use Streamlit to allow users to interact with and filter the data through the application.
""")
    st.markdown("[For more about the project click here my GitHub account](https://github.com/sakthi1810/Redbus---Scraping-data)")

elif st.session_state['menu'] == 'booking':
    st.markdown("[To Book Bus Ticket Click Here](https://www.redbus.in/)")
    
    locations = df['Route_name'].unique().tolist()  
    from_location = st.selectbox("From", locations)
    to_location = st.selectbox("To", locations)
    
    if st.button("Search Buses"):
        # Filter based on user input
        filtered_buses = df[
            (df['Route_name'].str.contains(from_location, case=False)) & 
            (df['Route_name'].str.contains(to_location, case=False))
        ]
        
        if not filtered_buses.empty:
            st.table(filtered_buses)
        else:
            st.error("No buses found for the selected route.")

elif st.session_state['menu'] == 'feedback':
    st.subheader("Feedback Form")
    
    route_name = st.selectbox("Select Route Name", df['Route_name'].unique())
    price = st.selectbox("Select Price Range", df['Price'].unique())
    feedback = st.text_area("Enter your feedback here")
    
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

elif st.session_state['menu'] == 'select_bus':
    st.subheader("Available Buses")
    if not df.empty:    
        # Filter options
        route = st.selectbox("Select the Route", df['Route_name'].unique(), index=0)  
        seat_type = st.selectbox("Select the Seat Type", ["Sleeper", "Seater"], index=0)
        ac_type = st.selectbox("Select the AC Type", ["A/C", "Non A/C"], index=0)
        rating_filter = st.selectbox("Select the Ratings", ["3 to 4", "4 to 5", '5 to 9'], index=0)
        
        
        filtered_buses = df[
            (df['Route_name'] == route) &  
            (df['Bus_type'].str.contains(seat_type)) &
            (df['Bus_type'].str.contains(ac_type)) & 
            (df['Ratings'] >= float(rating_filter.split()[0])) & 
            (df['Ratings'] <= float(rating_filter.split()[2]))
            
        ]

        # Display data in a table format
        st.table(filtered_buses)
    else:
        st.error("No data found in the database.")
else:
    st.info("Select an option from the menu on the left.")
    st.info("Click Home button to know the project details")
    st.markdown("[To Book Bus Ticket Click Here](https://www.redbus.in/)")
    st.markdown("[For more about the project click here my GitHub account](https://github.com/sakthi1810/Redbus---Scraping-data)")
