Remote Site BESS + Diesel Generator Dispatch Model

This model simulates the dispatch of a Battery Energy Storage System (BESS) and a diesel generator to meet a randomised variable load profile at a remote site. It evaluates configurations based on cost and CO2 emissions. The model is a work in progress.

File Structure
- BESS_Model.ipynb = Main Model Code
- Load_data.csv = Site Load Profile
- Gen Eff 150kW.csv = Generator Efficiency Curve
- results_genX.csv = Saved Dataframe of most recent model run
- results_gen250/260/270/280.csv = Presaved results for generator sizes, used for Streamlit Dashboard
- model_streamlit.py = Code to run Streamlit Dashboard

Features
- Time-step simulation of generator and BESS dispatch
- Enforced constraints on BESS state of charge (SoC), charge/discharge logic, and generator output
- Tracks unmet load, emissions, fuel cost
- Allows user-defined generator sizing, BESS sizes are pre-set
- Streamlit dashboard 

Inputs
- Load profile (CSV, 204kW peak load)
- Generator size (user input, 0.8p.f applied, 250kVA is minimum recommended size to meet all load).
- BESS power/energy combinations. Pre-defined list, both Power (kW) and Energy (kWh): [50, 100, 150, 200, 250, 300]
- Diesel fuel cost, emissions factor, round-trip efficiency are tracked.

Outputs
- Model recommends optimal configurations for lowest:
a) Cost
b) CO2
- Time-series plots for the optimal configurations.
- Summary statistics for optimal configurations.
- Outputs a table of all BESS configurations.
- User can run Streamlit dashboard to interact with pre-computed configuration tables for 250kW, 260kW, 270kW and 280kW generator sizes (instructions below).

Streamlit dashboard
- Results for 250kW, 260kW, 270kW and 280kW generator sizes have already been collected and stored for use in an interactive streamlit dashboard
- Allows the user to select between generator sizes and observe optimal configurations for cost and CO2, without the need of running the main model code. 
- Only displays configurations that meet all site load.
- To use, insert: streamlit run model_streamlit.py    into a terminal within the ‘BESS Hybrid Model’ folder structure (this runs the model_streamlit.py code)

Limitations and Further Work
- This is an ongoing work in progress. The model demonstrates the combined use of BESS and a diesel generator to meet site load, and the trade-offs between reducing CO2 (larger BESS required, greater rent costs) and reducing Cost (smaller BESS used, greater CO2). However there are elements of the model that I seek to improve. 
- Dispatch Logic: The current logic functions correctly but could be made more robust. In particular, it tends to allow "pulse charging," where the BESS hovers just above the minimum SoC and frequently cycles unnecessarily. Refining this behavior would improve realism and reduce wear modeling.
- Renewable Integration: Adding a solar PV component would allow for more realistic hybrid microgrid simulations and enable renewables-first dispatch.
- Grid Connectivity and Arbitrage: Future versions could simulate grid-connected systems, incorporating time-of-use pricing and energy arbitrage logic to optimize when the BESS charges or discharges based on tariffs.
- Streamlit dashboard: Adding visualisations and more variables would enable a more interactive and customisable user experience 
