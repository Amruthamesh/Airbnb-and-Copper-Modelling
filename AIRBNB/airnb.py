import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
import os

# Streamlit part
st.set_page_config(layout="wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

def load_data(file_path):
    return pd.read_csv(file_path)

df = load_data("C:/testing streamlit/Airbnb.csv")

def save_to_csv(dataframe, filename):
    """ Save DataFrame to CSV with a full path """
    file_path = f"C:/testing streamlit/{filename}"
    try:
        if not dataframe.empty:
            dataframe.to_csv(file_path, index=False)
            st.write(f"CSV file saved as {filename}")
        else:
            st.write(f"DataFrame is empty. No CSV file saved for {filename}.")
    except Exception as e:
        st.write(f"Error saving CSV file: {e}")

with st.sidebar:
    select = option_menu("Main Menu", ["Home", "Data Exploration", "About"])

if select == "Home":
    image1 = Image.open("C:/testing streamlit/airbnb-logo.png")
    st.image(image1)
    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')


if select == "Data Exploration":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["***PRICE ANALYSIS***", "***AVAILABILITY ANALYSIS***", "***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])
    
    with tab1:
        st.title("**PRICE DIFFERENCE**")
        col1, col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select the Country", df["country"].unique(), key="country_selectbox_1")
            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)
            room_ty = st.selectbox("Select the Room Type", df1["room_type"].unique(), key="room_type_selectbox_1")
            df2 = df1[df1["room_type"] == room_ty]
            df2.reset_index(drop=True, inplace=True)
            df_bar = pd.DataFrame(df2.groupby("property_type")[["price", "review_scores", "number_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)
            fig_bar = px.bar(df_bar, x='property_type', y="price", title="PRICE FOR PROPERTY_TYPES", hover_data=["number_of_reviews", "review_scores"], color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)
            save_to_csv(df_bar, "price_analysis_property_types.csv")

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            proper_ty = st.selectbox("Select the Property_type", df2["property_type"].unique(), key="property_type_selectbox_1")
            df4 = df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop=True, inplace=True)
            df_pie = pd.DataFrame(df4.groupby("host_response_time")[["price", "bedrooms"]].sum())
            df_pie.reset_index(inplace=True)
            fig_pi = px.pie(df_pie, values="price", names="host_response_time", hover_data=["bedrooms"], color_discrete_sequence=px.colors.sequential.BuPu_r, title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME", width=600, height=500)
            st.plotly_chart(fig_pi)
            save_to_csv(df_pie, "price_analysis_host_response_time.csv")

        col1, col2 = st.columns(2)
        with col1:
            hostresponsetime = st.selectbox("Select the host_response_time", df4["host_response_time"].unique(), key="host_response_time_selectbox_1")
            df5 = df4[df4["host_response_time"] == hostresponsetime]
            df5.reset_index(drop=True, inplace=True)
            df_do_bar = pd.DataFrame(df5.groupby("bed_type")[["minimum_nights", "maximum_nights", "price"]].sum())
            df_do_bar.reset_index(inplace=True)
            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], title='MINIMUM NIGHTS AND MAXIMUM NIGHTS', hover_data='price', barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
            st.plotly_chart(fig_do_bar)
            save_to_csv(df_do_bar, "price_analysis_min_max_nights.csv")

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            df_do_bar_2 = pd.DataFrame(df5.groupby("bed_type")[["bedrooms", "beds", "accommodates", "price"]].sum())
            df_do_bar_2.reset_index(inplace=True)
            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], title='BEDROOMS AND BEDS ACCOMMODATES', hover_data='price', barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=600, height=500)
            st.plotly_chart(fig_do_bar_2)
            save_to_csv(df_do_bar_2, "price_analysis_bedroom_beds_accommodates.csv")

    with tab2:
        st.title("**AVAILABILITY ANALYSIS**")
        col1, col2 = st.columns(2)

        with col1:
            country_a = st.selectbox("Select the Country_a", df["country"].unique(), key="country_selectbox_2")
            df1_a = df[df["country"] == country_a]
            df1_a.reset_index(drop=True, inplace=True)
            property_ty_a = st.selectbox("Select the Property Type", df1_a["property_type"].unique(), key="property_type_selectbox_2")
            df2_a = df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop=True, inplace=True)
            df_a_sunb_30 = px.sunburst(df2_a, path=["room_type", "bed_type", "is_location_exact"], values="availability_30", width=600, height=500, title="Availability_30", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
            save_to_csv(df2_a[["room_type", "bed_type", "is_location_exact", "availability_30"]], "availability_analysis_30.csv")

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            df_a_sunb_60 = px.sunburst(df2_a, path=["room_type", "bed_type", "is_location_exact"], values="availability_60", width=600, height=500, title="Availability_60", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_60)
            save_to_csv(df2_a[["room_type", "bed_type", "is_location_exact", "availability_60"]], "availability_analysis_60.csv")

        with col1:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            df_a_sunb_90 = px.sunburst(df2_a, path=["room_type", "bed_type", "is_location_exact"], values="availability_90", width=600, height=500, title="Availability_90", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_90)
            save_to_csv(df2_a[["room_type", "bed_type", "is_location_exact", "availability_90"]], "availability_analysis_90.csv")

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            df1_b = df1_a[["room_type", "bed_type", "is_location_exact", "minimum_nights", "maximum_nights", "availability_30", "availability_60", "availability_90"]].copy()
            df1_b.to_csv("C:/testing streamlit/availability_analysis.csv", index=False)
            st.write("CSV file has been saved with availability data.")
            st.write("")

    with tab3:
        st.title("**LOCATION BASED**")
        st.write("")

        country_b = st.selectbox("Select the Country_b", df["country"].unique(), key="country_selectbox_3")
        df1_b = df[df["country"] == country_b]
        df1_b.reset_index(drop=True, inplace=True)
        property_ty_b = st.selectbox("Select the Property Type", df1_b["property_type"].unique(), key="property_type_selectbox_3")
        df2_b = df1_b[df1_b["property_type"] == property_ty_b]
        df2_b.reset_index(drop=True, inplace=True)
        room_ty_b = st.selectbox("Select the Room Type", df2_b["room_type"].unique(), key="room_type_selectbox_3")
        df3_b = df2_b[df2_b["room_type"] == room_ty_b]
        df3_b.reset_index(drop=True, inplace=True)
        df_map = df3_b.copy()
        st.write("")
        st.write("Map of the properties")
        fig_map = px.scatter_mapbox(df_map, lat="latitude", lon="longitude", color="price", size="price", hover_name="name", hover_data=["room_type", "property_type"], color_continuous_scale=px.colors.cyclical.IceFire, title="Location Based Analysis", mapbox_style="carto-positron", zoom=10, height=600, width=900)
        st.plotly_chart(fig_map)
        save_to_csv(df_map[["name", "latitude", "longitude", "price", "room_type", "property_type"]], "location_based_analysis.csv")

    with tab4:
        st.title("**GEOSPATIAL VISUALIZATION**")
        st.write("")
        st.write("")

        df_geospatial = df.copy()
        df_geospatial.reset_index(drop=True, inplace=True)
        df_geospatial = df_geospatial[["latitude", "longitude", "price"]]
        df_geospatial = df_geospatial.dropna()
        df_geospatial.reset_index(drop=True, inplace=True)
        fig_geo_map = px.scatter_mapbox(df_geospatial, lat="latitude", lon="longitude", color="price", size="price", color_continuous_scale=px.colors.sequential.Viridis, title="Geospatial Visualization", mapbox_style="carto-positron", zoom=10, height=600, width=900)
        st.plotly_chart(fig_geo_map)
        save_to_csv(df_geospatial, "geospatial_visualization.csv")

    with tab5:
        st.title("**TOP CHARTS**")
        st.write("")
        st.write("")

        df_top_charts = df.copy()
        df_top_charts.reset_index(drop=True, inplace=True)
        df_top_charts = df_top_charts[["room_type", "property_type", "price"]]
        df_top_charts_grouped = df_top_charts.groupby(["room_type", "property_type"]).mean().reset_index()
        df_top_charts_sorted = df_top_charts_grouped.sort_values(by="price", ascending=False)
        fig_top_charts = px.bar(df_top_charts_sorted, x="room_type", y="price", color="property_type", title="Top Charts by Room Type and Property Type", height=500, width=700)
        st.plotly_chart(fig_top_charts)
        save_to_csv(df_top_charts_sorted, "top_charts.csv")

if select == "About":
    st.write("")
    st.write("")
    st.write("This is an Airbnb Data Analysis App built with Streamlit and Plotly. It includes various sections for data exploration and visualization based on Airbnb dataset.")
    st.write("")
    st.write("Feel free to explore the different tabs to analyze the data based on different aspects including price, availability, location, geospatial aspects, and top charts.")

# Additional functionality and improvements
def handle_data(dataframe):
    """ Handle non-numeric data and prepare DataFrame for numerical operations. """
    df_numeric = dataframe.select_dtypes(include=[np.number])  # Use numpy directly
    return df_numeric

# Sample call to handle_data
df_numeric = handle_data(df)
correlation_matrix = df_numeric.corr()
st.write("Correlation Matrix:")
st.write(correlation_matrix)

