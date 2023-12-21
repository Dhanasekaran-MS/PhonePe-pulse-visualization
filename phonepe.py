import streamlit as st
import pandas as pd
import warnings
import pymysql
import os
import json
import plotly.express as px
from streamlit_option_menu import option_menu
warnings.filterwarnings('ignore')

# Cloning PhonePe Pulse
# !git clone https://github.com/PhonePe/pulse.git
def format_name(string):
    captitalized_name = ' '.join(word.capitalize() for word in string.split('-'))
    return captitalized_name

def aggregated_trans():
    path1 = "/phonepe/pulse/data/aggregated/transaction/country/india/state"
    aggr_trans = os.listdir(path1)
    column1 = {"State": [], "Year": [], "Quarter": [], "Transaction_Type": [],
               "Transaction_Count": [], "Transaction_Amount": []}
    for state in aggr_trans:
        cur_state = path1 + '/' + state  # string
        year_list = os.listdir(cur_state)  # path
        for year in year_list:
            cur_year = cur_state + '/' + year  # string
            quart_list = os.listdir(cur_year)  # path
            for quart in quart_list:
                cur_quart = cur_year + '/' + quart
                file = open(cur_quart, 'r')
                A = json.load(file)
                for i in A['data']['transactionData']:
                    name = i['name']
                    count = i['paymentInstruments'][0]['count']
                    amount = i['paymentInstruments'][0]['amount']
                    column1['Transaction_Type'].append(name)
                    column1['Transaction_Count'].append(count)
                    column1['Transaction_Amount'].append(amount)
                    column1['State'].append(format_name(state))
                    column1['Year'].append(year)
                    column1['Quarter'].append(int(quart.strip('.json')))
    aggregated_transaction = pd.DataFrame(column1)
    return aggregated_transaction
    
def aggregated_user():
    path2 = "/phonepe/pulse/data/aggregated/user/country/india/state"
    aggr_user = os.listdir(path2)
    column2 = {"State": [], "Year": [], "Quarter": [], "Brand": [], "Count": [], "Percentage": []}
    for state in aggr_user:
        cur_state = path2 + '/' + state  # string
        year_list = os.listdir(cur_state)
        for year in year_list:
            cur_year = cur_state + '/' + year
            quart_list = os.listdir(cur_year)
            for quart in quart_list:
                cur_quart = cur_year + '/' + quart
                file = open(cur_quart, 'r')
                B = json.load(file)
                try:
                    for i in B["data"]['usersByDevice']:
                        brand = i['brand']
                        count = i['count']
                        percentage = i['percentage']
                        column2['Brand'].append(brand)
                        column2['Count'].append(count)
                        column2['Percentage'].append(percentage)
                        column2['State'].append(format_name(state))
                        column2['Year'].append(year)
                        column2['Quarter'].append(int(quart.strip('.json')))
                except:
                    pass
    aggregated_user = pd.DataFrame(column2)
    return aggregated_user
    
def map_trans():
    path3 = "/phonepe/pulse/data/map/transaction/hover/country/india/state"
    map_trans = os.listdir(path3)
    column3 = {"State": [], "Year": [], "Quarter": [], "District": [],
               "Transaction_Count": [], "Transaction_Amount": []}
    for state in map_trans:
        cur_state = path3 + '/' + state
        year_list = os.listdir(cur_state)
        for year in year_list:
            cur_year = cur_state + '/' + year
            quart_list = os.listdir(cur_year)
            for quart in quart_list:
                cur_quart = cur_year + '/' + quart
                file = open(cur_quart, 'r')
                C = json.load(file)
                for i in C['data']['hoverDataList']:
                    district = i['name']
                    count = i['metric'][0]['count']
                    amount = i['metric'][0]['amount']
                    column3["State"].append(format_name(state))
                    column3["Year"].append(year)
                    column3['Quarter'].append(int(quart.strip('.json')))
                    column3["District"].append(district)
                    column3["Transaction_Count"].append(count)
                    column3["Transaction_Amount"].append(amount)
    map_transaction = pd.DataFrame(column3)
    return map_transaction
    
def map_user():
    path4 = "/phonepe/pulse/data/map/user/hover/country/india/state"
    map_user = os.listdir(path4)
    column4 = {"State": [], "Year": [], "Quarter": [], "District": [],
               "Registered_Users": [], "App_Opens": []}
    for state in map_user:
        cur_state = path4 + '/' + state
        year_list = os.listdir(cur_state)
        for year in year_list:
            cur_year = cur_state + '/' + year
            quart_list = os.listdir(cur_year)
            for quart in quart_list:
                cur_quart = cur_year + '/' + quart
                file = open(cur_quart, 'r')
                D = json.load(file)
                for i in D['data']['hoverData'].items():
                    district = i[0]
                    registered_users = i[1]['registeredUsers']
                    app_opens = i[1]['appOpens']
                    column4["State"].append(format_name(state))
                    column4["Year"].append(year)
                    column4['Quarter'].append(int(quart.strip('.json')))
                    column4["District"].append(district)
                    column4["Registered_Users"].append(registered_users)
                    column4["App_Opens"].append(app_opens)
    map_user = pd.DataFrame(column4)
    return map_user

def top_trans():
    path5 = "/phonepe/pulse/data/top/transaction/country/india/state"
    top_trans = os.listdir(path5)
    column5 = {"State": [], "Year": [], "Quarter": [], "Entity": [],
               "Count": [], "Amount": []}
    for state in top_trans:
        cur_state = path5 + '/' + state
        year_list = os.listdir(cur_state)
        for year in year_list:
            cur_year = cur_state + '/' + year
            quart_list = os.listdir(cur_year)
            for quart in quart_list:
                cur_quart = cur_year + '/' + quart
                file = open(cur_quart, 'r')
                E = json.load(file)
                for i in E['data']['districts']:
                    district = i['entityName']
                    count = i['metric']['count']
                    amount = i['metric']['amount']
                    column5['State'].append(format_name(state))
                    column5['Year'].append(year)
                    column5['Quarter'].append(int(quart.strip('.json')))
                    column5['Entity'].append(district)
                    column5['Count'].append(count)
                    column5['Amount'].append(amount)
                for j in E['data']['pincodes']:
                    district = j['entityName']
                    count = j['metric']['count']
                    amount = j['metric']['amount']
                    column5['State'].append(format_name(state))
                    column5['Year'].append(year)
                    column5['Quarter'].append(int(quart.strip('.json')))
                    column5['Entity'].append(district)
                    column5['Count'].append(count)
                    column5['Amount'].append(amount)
    top_transaction = pd.DataFrame(column5)
    return top_transaction
    
def top_user():
    path6 = "/phonepe/pulse/data/top/user/country/india/state"
    top_us = os.listdir(path6)
    column6 = {"State": [], "Year": [], "Quarter": [], "Entity": [],
               "Registered_Users": []}
    for state in top_us:
        cur_state = path6 + '/' + state
        year_list = os.listdir(cur_state)
        for year in year_list:
            cur_year = cur_state + '/' + year
            quart_list = os.listdir(cur_year)
            for quart in quart_list:
                cur_quart = cur_year + '/' + quart
                file = open(cur_quart, 'r')
                F = json.load(file)
                for i in F['data']['districts']:
                    entity = i['name']
                    registered_users = i['registeredUsers']
                    column6['State'].append(format_name(state))
                    column6['Year'].append(year)
                    column6['Quarter'].append(int(quart.strip('.json')))
                    column6['Entity'].append(entity)
                    column6['Registered_Users'].append(registered_users)
                for j in F['data']['pincodes']:
                    entity = j['name']
                    registered_users = j['registeredUsers']
                    column6['State'].append(format_name(state))
                    column6['Year'].append(year)
                    column6['Quarter'].append(int(quart.strip('.json')))
                    column6['Entity'].append(entity)
                    column6['Registered_Users'].append(registered_users)
    top_user = pd.DataFrame(column6)
    return top_user

def to_sql(at, au, mt, mu, tt, tu):
    mydb = pymysql.Connection(host='127.0.0.1', user='root', passwd='Dhana@123')
    cur = mydb.cursor()
    cur.execute("create database if not exists phonepe")
    mydb = pymysql.Connection(host='127.0.0.1', user='root', passwd='Dhana@123', database='phonepe')
    cur = mydb.cursor()

    tab_agg_trans = '''create table if not exists AggrTrans(State varchar(50), 
                                                            Year year, 
                                                            Quarter int, 
                                                            Transaction_Type text,
                                                            Transaction_Count bigint, 
                                                            Transaction_Amount bigint)'''
    cur.execute(tab_agg_trans)
    ins_at = '''insert ignore into AggrTrans values(%s,%s,%s,%s,%s,%s)'''
    for index, row in at.iterrows():
        values = (row['State'], row['Year'],
                  row['Quarter'], row['Transaction_Type'],
                  row['Transaction_Count'], row['Transaction_Amount'])
        cur.execute(ins_at, values)
        mydb.commit()

    tab_agg_user = '''create table if not exists AggrUser(State varchar(50), 
                                                          Year year, 
                                                          Quarter int, 
                                                          Brand varchar(30), 
                                                          Count bigint, 
                                                          Percentage float)'''
    cur.execute(tab_agg_user)
    ins_au = '''insert ignore into AggrUser values(%s,%s,%s,%s,%s,%s)'''
    for index, row in au.iterrows():
        values = (row['State'], row['Year'],
                  row['Quarter'], row['Brand'],
                  row['Count'], row['Percentage'])
        cur.execute(ins_au, values)
        mydb.commit()

    tab_map_trans = '''create table if not exists MapTrans(State varchar(50), 
                                                           Year year, 
                                                           Quarter int, 
                                                           District varchar(60),
                                                           Transaction_Count bigint, 
                                                           Transaction_Amount bigint)'''
    cur.execute(tab_map_trans)
    ins_mt = '''insert ignore into MapTrans values(%s,%s,%s,%s,%s,%s)'''
    for index, row in mt.iterrows():
        values = (row['State'], row['Year'],
                  row['Quarter'], row['District'],
                  row['Transaction_Count'], row['Transaction_Amount'])
        cur.execute(ins_mt, values)
        mydb.commit()

    tab_map_user = '''create table if not exists MapUser(State varchar(50), 
                                                         Year year, 
                                                         Quarter int, 
                                                         District varchar(60),
                                                         Registered_Users bigint, 
                                                         App_Opens bigint)'''
    cur.execute(tab_map_user)
    ins_mu = '''insert ignore into MapUser values(%s,%s,%s,%s,%s,%s)'''
    for index, row in mu.iterrows():
        values = (row['State'], row['Year'],
                  row['Quarter'], row['District'],
                  row['Registered_Users'], row['App_Opens'])
        cur.execute(ins_mu, values)
        mydb.commit()

    tab_top_trans = '''create table if not exists TopTrans(State varchar(50), 
                                                           Year year, 
                                                           Quarter int, 
                                                           Entity varchar(50),
                                                           Count bigint, 
                                                           Amount bigint)'''
    cur.execute(tab_top_trans)
    ins_tt = '''insert ignore into TopTrans values(%s,%s,%s,%s,%s,%s)'''
    for index, row in tt.iterrows():
        values = (row['State'], row['Year'],
                  row['Quarter'], row['Entity'],
                  row['Count'], row['Amount'])
        cur.execute(ins_tt, values)
        mydb.commit()

    tab_top_user = '''create table if not exists TopUser(State varchar(50), 
                                                         Year year, 
                                                         Quarter int, 
                                                         Entity varchar(50),
                                                         Registered_Users bigint)'''
    cur.execute(tab_top_user)
    ins_tu = '''insert ignore into TopUser values(%s,%s,%s,%s,%s)'''
    for index, row in tu.iterrows():
        values = (row['State'], row['Year'],
                  row['Quarter'], row['Entity'],
                  row['Registered_Users'])
        cur.execute(ins_tu, values)
        mydb.commit()
def process_data():
    agt = aggregated_trans()
    agu = aggregated_user()
    mpt = map_trans()
    mpu = map_user()
    tpt = top_trans()
    tpu = top_user()
    to_sql(agt,agu,mpt,mpu,tpt,tpu)

# Creating MySql Database Connection
mydb = pymysql.Connection(host='127.0.0.1', user='root', passwd='Dhana@123', database='phonepe')
st.set_page_config(page_title='phonepe pulse', page_icon=':bar_chart:', layout='wide')
# Option Menu --> Map, Analysis, Visualization
option = option_menu(menu_title=None,
                     options=['Map', 'Analysis', 'Visualization'],
                     icons=['geo-alt', 'file-bar-graph', 'graph-up'],
                     orientation='horizontal',
                     menu_icon="app-indicator",
                     styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px",
                                          "--hover-color": "#6F36AD"},
                             "nav-link-selected": {"background-color": "#6F36AD"}})
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
# Dashboard for MAP
if option == 'Map':
    st.sidebar.markdown('# :violet[Phone]Pe :grey[Pulse] :green[Visualization]')
    st.write('Select Type and Year to visualize Map')
    col1, col2 = st.columns([3, 3])
    with col1:
        map_type = st.selectbox('', options=['Transactions', 'Users'], label_visibility='collapsed',
                                placeholder='Select Transactions or Users', index=None)
    with col2:
        map_yr = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023], label_visibility='collapsed',
                              placeholder='Select a Year to view', index=None)
    # when the type is transaction :
    if map_type == 'Transactions' and map_yr is not None:
        map_query = f'''select state,year,sum(Transaction_Count) as transactions,sum(Transaction_Amount) as Amount 
                        from maptrans where year = {map_yr} group by state;'''
        df = pd.read_sql_query(map_query, mydb)
        fig = px.choropleth(df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='state',
                            color="transactions",
                            title='PhonePe India Transactions',
                            color_continuous_scale='turbid',
                            width=1000, height=800, hover_name='state')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
    # When the type is Users :
    if map_type == 'Users' and map_yr is not None:
        query = f'''select state,sum(registered_users)as registered_users from mapuser where year = {map_yr} 
                    group by state;'''
        df = pd.read_sql_query(query, mydb)
        fig = px.choropleth(df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='state',
                            color="registered_users",
                            title='PhonePe India Transactions',
                            color_continuous_scale='reds',
                            width=1000, height=800, hover_name='state')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
# Dashboard for Analysis
elif option == 'Analysis':
    # Sidebar Buttons (SelectBox)
    with st.sidebar:
        st.header(":blue[Choose Type,Year and Quarter to do Analysis]")
        st.divider()
        opt, dummy = st.columns([5, 1])
        with opt:
            trans = st.selectbox('', options=['Transactions', 'Users'], index=None, placeholder='Type',
                                 label_visibility='collapsed')
            year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023], placeholder='Year',
                                label_visibility='collapsed')
            quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')
    st.markdown(f'## ANALYSIS BASED ON :red[{year}] - QUARTER - :red[{quarter}]')
    # When User selects transactions
    if trans == 'Transactions':
        tab1, tab2, tab3 = st.tabs(['Details', 'Category', 'TOP 10'])
        # Transaction Details Tab
        with tab1:
            st.markdown('#### :orange[PhonePe] :green[India]')
            col1, col2, col3 = st.columns(3)
            with col1:
                query1 = f'''select concat(sum(Transaction_Count)/10000000,' Cr') as trans from aggrtrans where 
                             year={year} and quarter = {quarter};'''
                all_trans = pd.read_sql_query(query1, mydb)
                st.dataframe(all_trans, column_config={"trans": "Total Number of Transactions"}, hide_index=True)
            with col2:
                query2 = f'''select concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as value from aggrtrans 
                             where year={year} and quarter={quarter};'''
                trans_val = pd.read_sql_query(query2, mydb)
                st.dataframe(trans_val, column_config={"value": "Total Payment Value"}, hide_index=True)
            with col3:
                query3 = f'''select concat('₹ ',sum(Transaction_Amount)/sum(Transaction_Count)) as avg from aggrtrans 
                             where year={year} and quarter={quarter};'''
                avg_val = pd.read_sql_query(query3, mydb)
                st.dataframe(avg_val, column_config={"avg": "Average Payment Value"}, hide_index=True)
        # Transactions Category Tab
        with tab2:
            st.markdown(f"### :grey[Tables on Transaction Count and Payment Value based on the category]")
            col1, col2 = st.columns([4, 4])
            with col1:
                query4 = f'''select transaction_type as mode , concat(sum(transaction_count)/100000,' lakh') as tc 
                             from aggrtrans where year={year} and quarter={quarter} group by transaction_type;'''
                cat_count = pd.read_sql_query(query4, mydb)
                st.dataframe(cat_count, column_config={"mode": "Type of Transaction", "tc": "No Of Transactions"},
                             hide_index=True)
            with col2:
                query5 = f'''select transaction_type as mode , concat('₹',sum(transaction_amount)/10000000,' Cr') as amt 
                             from aggrtrans where year={year} and quarter={quarter} group by transaction_type;'''
                cat_val = pd.read_sql_query(query5, mydb)
                st.dataframe(cat_val, column_config={"mode": "Type of Transaction", "amt": "Transaction Value"},
                             hide_index=True)
        # Transaction Top-10 Tab
        with tab3:
            # Creating select biox for top 10 based on transaction count and amount transferred
            select = st.selectbox('Select Option To Get TOP 10 :', options=['Number Of Transactions', 'Amount'])
            # Based on Transactions
            if select == "Number Of Transactions":
                # Top 10 States based on transaction
                if st.button("Top 10 States"):
                    st.markdown(
                        f"Top 10 States Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query6 = f'''select dense_rank()over(order by sum(Transaction_Count) desc) as rnk,state as State,
                                 concat(sum(Transaction_Count)/10000000,' Cr') as tc from aggrtrans 
                                 where year={year} and quarter={quarter} group by state order by rnk asc limit 10;'''
                    top_state = pd.read_sql_query(query6, mydb)
                    st.dataframe(top_state, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Districts based on transaction
                if st.button("Top 10 Districts"):
                    st.markdown(
                        f"Top 10 Districts Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query7 = f'''select dense_rank()over(order by count desc) as rnk,entity as District, 
                                 concat(count/100000, ' lakh') as tc from toptrans where year={year} and 
                                 quarter={quarter} and entity not regexp '^[0-9]' order by rnk asc limit 10;'''
                    top_district = pd.read_sql_query(query7, mydb)
                    st.dataframe(top_district, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Postal based on transaction
                if st.button("Top 10 Postal"):
                    st.markdown(
                        f"Top 10 Postal Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query8 = f'''select dense_rank()over(order by count desc) as rnk, entity as Postal, 
                                 concat(count/100000,' lakh') as tc from toptrans where year={year} and 
                                 quarter={quarter} and entity regexp '^[0-9]' order by rnk asc limit 10;'''
                    top_post = pd.read_sql_query(query8, mydb)
                    st.dataframe(top_post, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
            # Based on Amount
            elif select == "Amount":
                # Top 10 states based on Amount
                if st.button("Top 10 States"):
                    st.markdown(f"Top 10 States Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query6 = f'''select dense_rank()over(order by sum(Transaction_Amount) desc) as rnk,state as State,
                                 concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as amt from aggrtrans 
                                 where year={year} and quarter={quarter} group by state order by rnk asc limit 10;'''
                    top_state = pd.read_sql_query(query6, mydb)
                    st.dataframe(top_state, column_config={"rnk": "Rank", "amt": "Payment Value"}, hide_index=True)
                # Top 10 Districts based on Amount
                if st.button("Top 10 Districts"):
                    st.markdown(f"Top 10 Districts Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query7 = f'''select dense_rank()over(order by amount desc) as rnk,entity as District, 
                                 concat('₹ ',amount/10000000, ' Cr') as tc from toptrans where year={year} and 
                                 quarter={quarter} and entity not regexp '^[0-9]' order by rnk asc limit 10;'''
                    top_district = pd.read_sql_query(query7, mydb)
                    st.dataframe(top_district, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Postal based on Amount
                if st.button("Top 10 Postal"):
                    st.markdown(f"Top 10 Postal Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query8 = f'''select dense_rank()over(order by amount desc) as rnk, entity as Postal, 
                                 concat('₹ ',amount/10000000,' Cr') as tc from toptrans where year={year} and 
                                 quarter={quarter} and entity regexp '^[0-9]' order by rnk asc limit 10;'''
                    top_post = pd.read_sql_query(query8, mydb)
                    st.dataframe(top_post, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
    # When the transaction type is Users
    elif trans == 'Users':
        tab1, tab2 = st.tabs(['Details', 'TOP 10'])
        # User Details
        with tab1:
            st.markdown(f'#### :grey[PhonePe Users Data In INDIA by Q{quarter} - {year}]')
            query9 = f'''select concat(sum(Registered_Users)/10000000,' Cr') as users from mapuser where year={year} 
                         and quarter={quarter} group by year,quarter;'''
            usercount = pd.read_sql_query(query9, mydb)
            st.dataframe(usercount, column_config={"users": f"PhonePe users"}, hide_index=True)
            st.markdown("#### Total no of app opens in the selected period of time")
            query10 = f'''select case when sum(app_opens)=0 then 'N/A' else concat(sum(app_opens)/10000000, ' Cr') 
                          end as ao from mapuser where year={year} and quarter ={quarter} group by year, quarter; '''
            app_opens = pd.read_sql_query(query10, mydb)
            st.dataframe(app_opens, column_config={"ao": f"App Opens"}, hide_index=True)
        # User Top 10
        with tab2:
            # Top 10 User States
            if st.button("Top 10 States"):
                st.markdown(f'#### Top 10 States Based on Registered Users Q{quarter} - {year}:')
                query11 = (f'''select dense_rank()over(order by sum(registered_users) desc)as rnk,state,
                               concat(sum(registered_users)/100000,' lakh') as reguser from topuser
                               where year={year} and quarter={quarter} group by state order by rnk asc limit 10;''')
                state = pd.read_sql_query(query11, mydb)
                st.dataframe(state, column_config={"reguser": f"Registered Users"}, hide_index=True)
            # Top 10 User Districts
            if st.button("Top 10 Districts"):
                st.markdown(f'#### Top 10 District Based on Registered Users Q{quarter} - {year}:')
                query12 = f'''select dense_rank()over(order by registered_users desc) as rnk,entity as Districts,
                              concat(registered_users/100000,' lakh') as reguser from topuser
                              where year=2019 and quarter=1 and entity not regexp '^[0-9]' order by rnk asc limit 10;'''
                dist = pd.read_sql_query(query12, mydb)
                st.dataframe(dist, column_config={"reguser": f"Registered Users"}, hide_index=True)
            # Top 10 User Postal
            if st.button("Top 10 Postal"):
                st.markdown(f'#### Top 10 Postal Based on Registered Users Q{quarter} - {year}:')
                query13 = f'''select dense_rank()over(order by registered_users desc) as rnk,entity as Districts,
                              concat(registered_users/100000,' lakh') as reguser from topuser
                              where year=2019 and quarter=1 and entity regexp '^[0-9]' order by rnk asc limit 10;'''
                dist = pd.read_sql_query(query13, mydb)
                st.dataframe(dist, column_config={"reguser": f"Registered Users"}, hide_index=True)
# Dashboard for Visualization
elif option == 'Visualization':
    with st.sidebar:
        st.title(':red[We can visualize 5 chart.In those 3 are based on the option which user selects and 2 '
                 'are animated charts]')
        st.write('The :red[First chart] is a Bar Chart, We will be selecting the type of transaction to visualize '
                 'the change in count over the years')

        st.write('The :red[Second chart] is a Scatter plot chart, we will be selecting a year to visualize the change '
                 'in count of registered users inn mobile brand over 4 quarters in the year we choose')

        st.write('The :red[Third chart] is a Pie Chart, we will be selecting a year to visualize the top 10 states with'
                 'transaction count in an attractive pie chart ')

        st.write('The :red[Fourth chart] is an Animated Bar Chart,It shows the increase in transaction count over the '
                 'years with category of transaction (Overall India)')

        st.write('The :red[Fifth chart] is an Animated Scatter plot which shows the transaction count of each state '
                 'over the years along with the type of transaction')

    st.markdown('#### 📊 :orange[No.of Transactions Made Over Years in category]')
    col1, col2 = st.columns([3, 2])
    with col1:
        option = st.selectbox('', options=["Recharge & bill payments", "Peer-to-peer payments", "Merchant payments",
                                           "Financial Services", "Others"],
                              label_visibility='collapsed', index=None, placeholder='Select the Type of Transaction'
                              )
    with col2:
        btn = st.button("show")
    if option is not None and btn:
        query14 = f'''select year,sum(transaction_count) as tc,concat('₹',sum(Transaction_amount)/10000000,' Cr') 
                      as Amount from aggrtrans where transaction_type='{option}' group by year;'''
        df = pd.read_sql_query(query14, mydb)
        fig = px.bar(df, x='year', y='tc', labels={'year': "YEAR", 'tc': "Transaction count"},
                     hover_data=['Amount'], color_discrete_sequence=px.colors.sequential.Plasma)
        st.plotly_chart(fig)

    st.markdown('#### 📊 :blue[Smart Phone Brand with] :red[PhonePe] :blue[users]')
    col1, col2 = st.columns([3, 2])
    with col1:
        option1 = st.selectbox('', options=[2018, 2019, 2020, 2021],
                               label_visibility='collapsed', index=None, placeholder='Select a Year to view'
                               )
    with col2:
        btn1 = st.button(" show")
    if option1 is not None and btn1:
        query14 = f'''select brand,quarter,sum(Count) as count from aggruser where year={option1} 
                      group by brand,quarter;'''
        df = pd.read_sql_query(query14, mydb)
        fig = px.scatter(df, x='count', y='quarter', labels={'quarter': "Quarter", 'count': "Devices"},
                         hover_data=['brand'], title=f"Year-{option1}", color='brand',
                         color_discrete_sequence=px.colors.sequential.Turbo)
        st.plotly_chart(fig)
    st.markdown("#### PIE Chart")
    col1, col2 = st.columns([3, 2])
    with col1:
        option2 = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023],
                               label_visibility='collapsed', index=None, placeholder='Choose a Year'
                               )
    if option2 is not None:
        query = f'''select state, sum(Transaction_Count) as Transaction_count, 
                    concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as Amount
                    from aggrtrans where year = {option2} group by state order by Transaction_count desc limit 10;'''
        df = pd.read_sql_query(query, mydb)

        fig = px.pie(df, values='Transaction_count', names="state", labels='state', hover_name='Amount',
                     title=f"Top 10 States based on Transaction count for the year : {option2}",
                     color_discrete_sequence=px.colors.sequential.Turbo)
        st.plotly_chart(fig)

    st.markdown('#### Animated chart ')
    col1, col2 = st.columns([3, 2])
    with col1:
        option3 = st.selectbox('', options=['Hide', 'Show'], label_visibility='collapsed')
    if option3 == 'Show':
        query15 = f'''select transaction_type,year,sum(transaction_count) as tc,
                      concat('₹',sum(Transaction_Amount)/10000000,' Cr') as amount from aggrtrans
                      group by transaction_type,year;'''
        df = pd.read_sql_query(query15, mydb)
        fig = px.bar(df, x='year', y='tc', color='transaction_type', hover_name='amount',
                     color_discrete_sequence=px.colors.sequential.Turbo, animation_frame='year', range_x=[2018, 2023],
                     range_y=[0, 50000000000], title='Transaction Count Vs Year')
        st.plotly_chart(fig)
    st.markdown('#### Animated chart 2')
    col1, col2 = st.columns([3, 2])
    with col1:
        option4 = st.selectbox('', options=[' Hide ', ' Show '], label_visibility='collapsed')
    if option4 == ' Show ':
        query16 = '''select state,year,transaction_type as type,sum(transaction_count) as count,
                   concat('₹',sum(Transaction_Amount)/10000000, ' Cr') as amount from aggrtrans
                   group by state,year,transaction_type;'''
        df = pd.read_sql_query(query16, mydb)
        fig = px.scatter(df, x='count', y='state', animation_frame='year', color='type', hover_name='amount',
                         color_discrete_sequence=px.colors.sequential.Turbo, width=1000, height=1500,
                         range_x=[0, 2000000000], title='Transaction Count On State Over Years')
        st.plotly_chart(fig)
