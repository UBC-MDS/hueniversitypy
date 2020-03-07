import pandas as pd
import altair as alt

# import theme_ubc.py file with functions. 
from hueniversitypy.theme_ubc import *

# creating data to plot for tests

def test_chart_object():
    ''' A function that tests if an altair chart object is created  '''

    data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                     'B':[2, 3, 7, 4, 8, 4, 9], 
                     'C':[3, 6, 3, 5, 8, 2, 8] }))

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_ubc", theme_ubc)
    alt.themes.enable("theme_ubc")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')
    
    assert str(type(test_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"
    
def test_colours():
    ''' A function that tests the correct colours an imported into the 
    altair chart based on the theme'''

    data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                     'B':[2, 3, 7, 4, 8, 4, 9], 
                     'C':[3, 6, 3, 5, 8, 2, 8] }))

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_ubc", theme_ubc)
    alt.themes.enable("theme_ubc")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')
     
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ['#002145', '#0055B7', '#00A7E1', '#40B4E5', '#6EC4E8', '#97D4E9']
    
def test_font_type():
    ''' A function that tests the correct fonts are imported into the 
    altair chart based on the theme'''

    data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                     'B':[2, 3, 7, 4, 8, 4, 9], 
                     'C':[3, 6, 3, 5, 8, 2, 8] }))

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_ubc", theme_ubc)
    alt.themes.enable("theme_ubc")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')
     
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['font'] == 'Arial'
    assert plot_dict['config']['axisX']['labelFont'] == 'Arial'
    assert plot_dict['config']['axisX']['titleFont'] == 'Arial'
    assert plot_dict['config']['axisY']['labelFont'] == 'Arial'
    assert plot_dict['config']['axisY']['titleFont'] == 'Arial'
    
def test_font_size():
    ''' A function that tests the correct fonts sizes are used in the 
    altair chart based on the theme'''

    data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                     'B':[2, 3, 7, 4, 8, 4, 9], 
                     'C':[3, 6, 3, 5, 8, 2, 8] }))

    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_ubc", theme_ubc)
    alt.themes.enable("theme_ubc")

    # creating plot for testing with theme
    test_plot = alt.Chart(data).mark_point().encode(
        x='count()',
        y='value',
        color='variable',
    ).properties(title='Test')
     
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    
