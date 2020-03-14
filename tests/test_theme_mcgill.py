import pandas as pd
import altair as alt

# import theme_mcgill.py file with functions 
from hueniversitypy.theme_mcgill import *


# create dummy dataframe
data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                 'B':[2, 3, 7, 4, 8, 4, 9], 
                 'C':[3, 6, 3, 5, 8, 2, 8] }))

# create test plot
mcgill_plot = alt.Chart(data).mark_point().encode(
    x='count()',
    y='value',
    color='variable',
).properties(title = 'Test')
    
def test_chart_object():
    """Tests if an altair chart object is created"""
    
    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")

    assert str(type(mcgill_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"
    
def test_colours():
    """Tests if colours from the McGill theme has been applied to chart"""
    
    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")
    
    plot_dict = mcgill_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ["#ED1B2F","#FFD794","#B5E1E1","#C8EAF5","#D5E6A8"]
    
def test_font_type():
    """Tests if font type from the McGill theme has been applied to chart"""
    
    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")
    
    plot_dict = mcgill_plot.to_dict()
    assert plot_dict['config']['title']['font'] == 'Lato'
    assert plot_dict['config']['axisX']['labelFont'] == 'Lato'
    assert plot_dict['config']['axisX']['titleFont'] == 'Lato' 
    assert plot_dict['config']['axisY']['labelFont'] == 'Lato'
    assert plot_dict['config']['axisY']['titleFont'] == 'Lato'
    
def test_font_size():
    """Tests if font size from the McGill theme has been applied to chart"""
    
    # call the theme function to enforce theme on all subsequent plots
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")
    
    plot_dict = mcgill_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    