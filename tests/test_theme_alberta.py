import pandas as pd
import altair as alt

# import theme_alberta.py file with functions 
from hueniversitypy.theme_alberta import *


# creating dummy dataframe
data = pd.melt(pd.DataFrame({"A": [1, 86, 62, 29, 16, 42, 69],
                            "B": [21, 41, 97, 14, 75, 7, 32],
                            "C": [57, 90, 98, 67, 9, 46, 87]}))

# create test plot
alberta_plot = alt.Chart(data).mark_point().encode(
    x="count()",
    y="value",
    color="variable"
).properties(title="Test")

def test_chart_object_alberta():
    """Tests if an altair chart object is created"""
    
    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    assert str(type(alberta_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"

def test_colours_alberta():
    """Tests if colours from the Alberta theme has been applied to chart"""

    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ["#007C41", "#FFDB05", "#7D9AAA", "#A8B400", "#A79E70"]

def test_font_type_alberta():
    """Tests if font type from the Alberta theme has been applied to chart"""

    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['font'] == "Arial"
    assert plot_dict['config']['axisX']['labelFont'] == "Arial"
    assert plot_dict['config']['axisX']['titleFont'] == "Arial"
    assert plot_dict['config']['axisY']['labelFont'] == "Arial"
    assert plot_dict['config']['axisY']['titleFont'] == "Arial"

def test_font_size_alberta():
    """Tests if font size from the Alberta theme has been applied to chart"""

    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")
    
    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    