from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import ssl
import streamlit as st 

ssl._create_default_https_context = ssl._create_unverified_context  

st.set_page_config(page_title="ipyvizzu-story in Streamlit", layout="centered")
#st.sidebar.title("Poll results - Presentation tools")
#st.title("Streamlit 🎈 + ipyvizzu-story 📈🎬🚀")
st.markdown(" ### Hey there! Good to have you here! 😊") 
st.markdown("A few weeks ago, we asked data scientists in 5 LinkedIn groups about how often they have to present the results of their analysis to business stakeholders. At the bottom of this notebook, you can find the animated data story about the combined results of these polls, created with ipyvizzu-story, a new, open-source data storytelling tool for computational notebooks. 🎬📈🚀 You can fork and reuse the content if you sign up for [Deepnote](https://deepnote.com). ")

def create_chart():
    # initialize chart
    data = Data()
    df = pd.read_csv("Data/Poll_results.csv")
    data.add_data_frame(df)
    #@title Create the story
    
    story = Story(data=data)
    story.set_size(700, 450)

    slide1 = Slide(
        Step( 
            Style({
                "legend": {"label": {"fontSize": "1.1em"}, "paddingRight": "-1em"},
                "plot": { 
                    "marker": { "label": { "fontSize": "1.1em"}}, 
                    "paddingLeft": "10em",
                    "xAxis": {"title": { "color": "#00000000"}, "label": { "fontSize": "1.1em"}},
                    "yAxis": {"label": { "fontSize": "1.1em"}}},
                "logo": {"width": "6em"}
            }),
            Config.stackedBar({
                "x": "Vote percentage [%]",
                "y": "Group number",
                "stackedBy": "Answer",
                "title": "Stacked Bar Chart"
            })
        )
    )
    story.add_slide(slide1)

    slide2 = Slide(
    Step(
        Style({ "plot": { "xAxis": { "label": { "color": "#00000000"}}}}),
        Config({ "split": True, "title": "Splitted Bar chart"})
    )
    )
    story.add_slide(slide2)

    slide3 = Slide(
    Step(
        Style({ "plot": { "marker": { "label": { "fontSize": "0.916667em"}}}}),
        Config({ "x": {"set": ["Vote count","Answer"]}, "label": "Vote count", "title": "Splitted bar chart - vote count"}),
    )
)
    story.add_slide(slide3)

    slide4 = Slide()
    slide4.add_step(
        Step(
            Style({ "plot": { "yAxis": { "title": { "color": "#00000000"}}}}),
            Config({ "x": "Answer", "y": ["Group number","Vote count"], "split": False, "legend": "color"})
        )
    )

    slide4.add_step(
        Step(
            Style({ "plot": { "marker": { "label": { "fontSize": "1.1em"}}}}),
            Config({ "y": "Vote count", "title": "Column chart"}),
        )
    )
    story.add_slide(slide4)

    slide5 = Slide()
    slide5.add_step(
        Step(
            Config({ "x": ["Answer percentage [%]","Answer"], "y": None, "label":"Answer percentage [%]"})
        )
    )

    slide5.add_step(
        Step(
            Style({ "plot": { "xAxis": {"label": {"color": "#00000000"}}}}),
            Config({ "coordSystem": "polar", "title":"Pie chart"})
        )
    )
    story.add_slide(slide5)
    
    # Switch on the tooltip that appears when the user hovers the mouse over a chart element.
    story.set_feature("tooltip", True)

    return story._repr_html_(),df


CHART,df = create_chart()
html(CHART, width=700, height=450)

st.markdown('''
            [Source](https://twitter.com/VizzuHQ/status/1575473747599007744)
            ''')    