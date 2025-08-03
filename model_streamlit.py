###### TO RUN, ENTER INTO TERMINAL: 
###### streamlit run model_streamlit.py
 

import streamlit as st
import pandas as pd

st.title("Generator + BESS Optimisation Dashboard")

# Generator selection
gen_size = st.selectbox("Select Generator Size (kW)", [250, 260, 270, 280])
file_path = f"results_gen{gen_size}.csv"

try:
    # Load CSV
    og_df = pd.read_csv(file_path)
    
    og_df["Feasible"] = og_df["Feasible"].astype(str).str.lower()
    df0 = og_df[og_df["Feasible"] == "yes"]
    # Gets rid of surplus columns
    df = df0.iloc[:,:8]
    if df.empty:
        st.warning("No feasible configurations available for this generator size.")
    else:
        # Sorting option
        sort_option = st.selectbox("Sort Results By", ["Total_Cost_£", "CO2_kg"])

        # Sort and show dataframe
        df_sorted = df.sort_values(by=sort_option).reset_index(drop=True)
        st.dataframe(df_sorted)

        # Best result summary
        best_row = df_sorted.iloc[0]
        st.markdown(f"### Best Configuration to Minimise {sort_option}")
        st.write(best_row)

except FileNotFoundError:
    st.error(f"No results file found for {gen_size} kW generator.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()


