import pandas as pd
import altair as alt

# Import theme_alberta.py
from hueniversitypy.theme_alberta import *

# Create toy dataframe to plot 
data = pd.melt(pd.DataFrame({"A": [1, 86, 62, 29, 16, 42, 69],
                         "B": [21, 41, 97, 14, 75, 7, 32],
                         "C": [57, 90, 98, 67, 9, 46, 87]}))

# Create plot for testing
alberta_plot = alt.Chart(data).mark_point().encode(
    x="count()",
    y="value",
    color="variable"
).properties(title="Test")

def test_chart_object_alberta():
    """ Test whether a chart object has been created"""
    
    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    assert str(type(alberta_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"

def test_colours_alberta():
    """ A function that tests if an altair chart has colours imported from the University of Alberta's theme applied to it 
    adhering to the university's visual identity"""

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ["#007C41", "#FFDB05", "#7D9AAA", "#A8B400", "#A79E70"]

def test_font_type_alberta():
    """A function that tests if an altair chart has font type imported from the University of Alberta's theme applied to it 
    adhering to the university's visual identity"""

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['font'] == "Arial"
    assert plot_dict['config']['axisX']['labelFont'] == "Arial"
    assert plot_dict['config']['axisX']['titleFont'] == "Arial"
    assert plot_dict['config']['axisY']['labelFont'] == "Arial"
    assert plot_dict['config']['axisY']['titleFont'] == "Arial"

def test_font_size_alberta():
    """A function that tests if an altair chart has font size imported from the University of Alberta's theme applied to it 
    adhering to the university's visual identity"""

    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")
    
    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    
def wrong_colour():
    ''' A function that checks if the correct colours are used,
    shoud fail'''
    
    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['range']['category'] != ["#007C41", "#FFDB05", "#7D9AAA", "#A8B400", "#A79E70"], 'theme is not enabled, enable with \n>>> alt.themes.register("theme_alberta", theme_alberta) \n>>> alt.themes.enable("theme_alberta")'
    
def wrong_font():
    ''' A function that tests the if correct fonts are used,
    shoud fail'''
    
    # Call the theme to apply themes to all subsequent plots
    alt.themes.register("theme_alberta", theme_alberta)
    alt.themes.enable("theme_alberta")

    plot_dict = alberta_plot.to_dict()
    assert plot_dict['config']['title']['font'] != 'Arial', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_alberta", theme_alberta) \n>>> alt.themes.enable("theme_alberta")'
    assert plot_dict['config']['axisX']['labelFont'] != 'Arial', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_alberta", theme_alberta) \n>>> alt.themes.enable("theme_alberta")'
    assert plot_dict['config']['axisX']['titleFont'] != 'Arial', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_alberta", theme_alberta) \n>>> alt.themes.enable("theme_alberta")'
    assert plot_dict['config']['axisY']['labelFont'] != 'Arial', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_alberta", theme_alberta) \n>>> alt.themes.enable("theme_alberta")'
    assert plot_dict['config']['axisY']['titleFont'] != 'Arial', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_alberta", theme_alberta) \n>>> alt.themes.enable("theme_alberta")'
