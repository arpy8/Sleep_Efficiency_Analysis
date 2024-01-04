# Sleep Efficiency Analysis

## Overview
A Streamlit app designed to predict the quality of sleep based on various sleep-related parameters. The app utilizes a machine learning model, specifically a Random Forest classifier to provide users with an estimated sleep score.

## How to Use the App
1. **Gender Selection:** Choose your gender from the provided dropdown menu (Male or Female).
2. **Age:** Adjust the age slider to input your age within the range of 18 to 100.
3. **Sleep Duration:** Slide the sleep duration bar to input the number of hours you sleep per day, ranging from 0 to 24.
4. **Caffeine Consumption:** Use the caffeine consumption slider to input the amount of caffeine consumed, ranging from 0 to 1000.
5. **Awakenings:** Adjust the awakenings slider to input the number of times you wake up during the night, ranging from 0 to 10.
6. **Deep Sleep Percentage:** Slide the deep sleep percentage bar to input the percentage of deep sleep, ranging from 0 to 100.
7. **Light Sleep Percentage:** Slide the light sleep percentage bar to input the percentage of light sleep, ranging from 0 to 100.

###### Note: The final output is a percentage, of how good your sleep score was.
- 80% or above: good
- 50% or above: moderate
- 49% or below: poor

[refer to this link for source ](https://www.firstbeat.com/en/blog/a-good-nights-sleep-what-does-it-mean/#:~:text=Sleep%20score%20100%20means%20your,amount%20and%20quality%20of%20sleep.) 

Upon entering these parameters, the app allows you to click the "Predict" button. The machine learning model will then provide a sleep score based on the input data.

## Setup and Requirements (to run the app locally)
- The app employs the Streamlit library, so ensure you have it installed (`pip install streamlit`).
- The machine learning model is saved as a Pickle file (`rf_model.pkl`) in the `model` directory.
- Clone the repository and run the Python script to launch the Streamlit app.

```bash
git clone https://github.com/arpy8/Sleep_Efficiency_Analysis.git
cd Sleep_Efficiency_Analysis
streamlit run app.py
```

## Contributor
- Username: [arpy8](https://github.com/arpy8)