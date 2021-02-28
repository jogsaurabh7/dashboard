import streamlit as st
#import numpy as np
import pandas as pd
from PIL import Image
import os, os.path
import pandas_profiling as pf
import streamlit.components.v1 as components
#from pandasgui import show
import dtale


st.title("DashBoard")
imgs = []

# Add a selectbox to the sidebar:
DashBoard_selectbox = st.sidebar.selectbox('Choose the DashBoard Type ',
                                           (['_____', 'GL Reports', 'Sales Reports', 'Purchase Reports']))
report_list = ['_____', 'Credit Limit','Cash Flow', 'Sales', 'Sales Orders', 'Purchases', 'Purchase Orders', 'Receivables', 'Payables']
Reports_selectbox = st.sidebar.selectbox('Select Report', report_list)

gl_images = ['cashflow.png', 'creditcontrol.png', 'Sales ratios.png', 'monthlyCashFlow.png', 'Credit Period.png',
             'OverDue.png', 'payablestatus.png', 'Receivables.png']
sales_images = ['sales top10.png', 'CostCenterSale.png', 'SalesManSales.png', 'SoPending.png', 'OrderToSales.png',
                'o2c.png', 'WoSalesPending.png']
purchase_images = ['PurchseMonth.png', 'PendingPo.png', 'ordertopurchase.png', 'POratesVariation.png',
                   'PoQtrCostCete.png']


def gl():
    st.write(DashBoard_selectbox)
    st.image(gl_images)
    pass


def sales():
    st.write(DashBoard_selectbox)
    st.image(sales_images)
    pass


def purchase():
    st.write(DashBoard_selectbox)
    st.image(purchase_images)
    pass


if DashBoard_selectbox == 'GL Reports':
    gl()
elif DashBoard_selectbox == 'Sales Reports':
    sales()
elif DashBoard_selectbox == 'Purchase Reports':
    purchase()


@st.cache(suppress_st_warning=True)
def get_data(filename):
    with st.spinner('Getting Data...It may take a some time...'):
        df = pd.read_csv(filename)

    return df


def RunReport():
    col1, col2 = st.beta_columns(2)
    with st.spinner('Getting Data...It may take a some time...'):
        #df = pd.read_pickle(dfname)
        st.dataframe(df)

    with col1:
        b1 = st.button("Get Statistical Analysis")
    with col2:
        b2 = st.button("Analyse with DTale")



    if b1:
        with st.spinner('Proessing...It may take a some time...'):
            st.write('Statistical Analysis ...')
            report = pf.ProfileReport(df, title='Profile Report....').to_html()
            components.html(report, height=2500, width=1000, scrolling=True)

    elif b2:
        with st.spinner('Proessing...It may take a some time...'):
            st.write('Opening DTale in another tab...')
            dtale.show(df)



if Reports_selectbox == report_list[1]:
    st.subheader(report_list[1])
    df=get_data('CreditLimit.csv')
    RunReport()

elif Reports_selectbox == report_list[2]:
    st.subheader(report_list[2])
    df = get_data('cashflow.csv')
    RunReport()

elif Reports_selectbox == report_list[3]:
    st.subheader(report_list[3])
    df = get_data('sales.csv')
    RunReport()

elif Reports_selectbox == report_list[4]:
    st.subheader(report_list[4])
    df = get_data('SO.csv')
    RunReport()

elif Reports_selectbox == report_list[5]:
    st.subheader(report_list[5])
    df = get_data('purchase.csv')
    RunReport()

elif Reports_selectbox == report_list[6]:
    st.subheader(report_list[6])
    df = get_data('PO.csv')
    RunReport()

elif Reports_selectbox == report_list[7]:
    st.subheader(report_list[7])
    df = get_data('Receivables.csv')
    RunReport()

elif Reports_selectbox == report_list[8]:
    st.subheader(report_list[8])
    df = get_data('Payable.csv')
    RunReport()
