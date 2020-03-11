import pandas as pd
import altair as alt

# import theme_mcgill.py file with functions. 
from hueniversitypy.theme_mcgill import theme_mcgill

# creating data to plot for tests
data = pd.melt(pd.DataFrame({'A': [1, 4, 6, 8, 3, 6, 7], 
                 'B':[2, 3, 7, 4, 8, 4, 9], 
                 'C':[3, 6, 3, 5, 8, 2, 8] }))

# creating test plot
test_plot = alt.Chart(data).mark_point().encode(
    x='count()',
    y='value',
    color='variable',
).properties(title = 'Test')
    


def test_chart_object():
    ''' A function that tests if an altair chart object is created  '''
    
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")

    assert str(type(test_plot)) == f"<class 'altair.vegalite.v{alt.__version__[0]}.api.Chart'>"
    
def test_colours():
    ''' A function that tests the correct colours an imported into the 
    altair chart based on the theme'''
    
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")
    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['range']['category'] == ["#ED1B2F","#FFD794","#B5E1E1","#C8EAF5","#D5E6A8"]
    
def test_font_type():
    #
    ''' A function that tests the correct fonts are imported into the 
    altair chart based on the theme'''
    
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")
    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['font'] == 'Lato'
    assert plot_dict['config']['axisX']['labelFont'] == 'Lato'
    assert plot_dict['config']['axisX']['titleFont'] == 'Lato' 
    assert plot_dict['config']['axisY']['labelFont'] == 'Lato'
    assert plot_dict['config']['axisY']['titleFont'] == 'Lato'
    
def test_font_size():
    ''' A function that tests the correct fonts sizes are used in the 
    altair chart based on the theme'''
    
    alt.themes.register("theme_mcgill", theme_mcgill)
    alt.themes.enable("theme_mcgill")
    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['fontSize'] == 18
    assert plot_dict['config']['axisX']['labelFontSize'] == 12
    assert plot_dict['config']['axisX']['titleFontSize'] == 12
    assert plot_dict['config']['axisY']['labelFontSize'] == 12
    assert plot_dict['config']['axisY']['titleFontSize'] == 12
    
def wrong_colour():
    ''' A function that checks if the correct colours are used,
    shoud fail'''
    
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")
    
    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['range']['category'] != ["#ED1B2F","#FFD794","#B5E1E1","#C8EAF5","#D5E6A8"], 'theme is not enabled, enable with \n>>> alt.themes.register("theme_mcgill", theme_mcgill) \n>>> alt.themes.enable("theme_mcgill")'
    
def wrong_font():
    ''' A function that tests the if correct fonts are used,
    shoud fail'''
    
    # call the theme function to enforce themes on all subsequent plots 
    alt.themes.register("theme_toronto", theme_toronto)
    alt.themes.enable("theme_toronto")

    plot_dict = test_plot.to_dict()
    assert plot_dict['config']['title']['font'] != 'Lato', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_mcgill", theme_mcgill) \n>>> alt.themes.enable("theme_mcgill")'
    assert plot_dict['config']['axisX']['labelFont'] != 'Lato', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_mcgill", theme_mcgill) \n>>> alt.themes.enable("theme_mcgill")'
    assert plot_dict['config']['axisX']['titleFont'] != 'Lato', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_mcgill", theme_mcgill) \n>>> alt.themes.enable("theme_mcgill")'
    assert plot_dict['config']['axisY']['labelFont'] != 'Lato', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_mcgill", theme_mcgill) \n>>> alt.themes.enable("theme_mcgill")'
    assert plot_dict['config']['axisY']['titleFont'] != 'Lato', 'theme is not enabled, enable with \n>>> alt.themes.register("theme_mcgill", theme_mcgill) \n>>> alt.themes.enable("theme_mcgill")'
    

