import pandas as pd
import altair as alt

# Import theme_alberta.py
from hueniversitypy.theme_alberta import *

def test_chart_object_alberta():
    """ Test whether a chart object has been created"""
    
    # Create toy dataframe to plot 
    data = pd.melt(pd.DataFrame({"A": [1, 86, 62, 29, 16, 42, 69],
                             "B": [21, 41, 97, 14, 75, 7, 32],
                             "C": [57, 90, 98, 67, 9, 46, 87]}))

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    # Create plot for testing
    alberta_plot = alt.Chart(data).mark_point().encode(
        x="count()",
        y="value",
        color="variable"
    ).properties(title="Test")

    assert str(type(alberta_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"

def test_colours_alberta():
    """ Test whether the correct colour palette is applied to the chart object"""
    
    # Create toy dataframe to plot 
    data = pd.melt(pd.DataFrame({"A": [1, 86, 62, 29, 16, 42, 69],
                             "B": [21, 41, 97, 14, 75, 7, 32],
                             "C": [57, 90, 98, 67, 9, 46, 87]}))

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    # Create plot for testing
    alberta_plot = alt.Chart(data).mark_point().encode(
        x="count()",
        y="value",
        color="variable"
    ).properties(title="Test")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ["#007C41", "#FFDB05", "#7D9AAA", "#A8B400", "#A79E70"]

def test_font_type_alberta():
    """Test whether the correct font is applied to the chart object"""
    
    # Create toy dataframe to plot 
    data = pd.melt(pd.DataFrame({"A": [1, 86, 62, 29, 16, 42, 69],
                             "B": [21, 41, 97, 14, 75, 7, 32],
                             "C": [57, 90, 98, 67, 9, 46, 87]}))

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    # Create plot for testing
    alberta_plot = alt.Chart(data).mark_point().encode(
        x="count()",
        y="value",
        color="variable"
    ).properties(title="Test")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['font'] == "Arial"
    assert plot_dict['config']['axisX']['labelFont'] == "Arial"
    assert plot_dict['config']['axisX']['titleFont'] == "Arial"
    assert plot_dict['config']['axisY']['labelFont'] == "Arial"
    assert plot_dict['config']['axisY']['titleFont'] == "Arial"

def test_font_size_alberta():
    """Test whether the correct fonts sizes are applied to the chart object"""
    # Create toy dataframe to plot 
    
    data = pd.melt(pd.DataFrame({"A": [1, 86, 62, 29, 16, 42, 69],
                             "B": [21, 41, 97, 14, 75, 7, 32],
                             "C": [57, 90, 98, 67, 9, 46, 87]}))

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    # Create plot for testing
    alberta_plot = alt.Chart(data).mark_point().encode(
        x="count()",
        y="value",
        color="variable"
    ).properties(title="Test")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    