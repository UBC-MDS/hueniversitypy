def theme_alberta():
    """ 
    Applies a University of Alberta theme to all subsequential altair plot objects so they are displayed with the U of A visual identity.
    See the visual identity at https://www.ualberta.ca/toolkit/visual-identity/our-colours. 
    Four palettes based on the U of A visual identity guidelines can be selected: 'alpha', 'beta', 'gamma' and 'delta'. 
    See more details about the package on GitHub: https://github.com/UBC-MDS/hueniversitypy/blob/master/README.md 

	
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    	an altair plot with the U of A visual identity colour theme applied. 

    Example
    ----------
    >>> from hueniversitypy.theme_alberta import *
    >>> data = pandas.DataFrame({'X': numpy.random.randint(100, size=100), 
                                'Y': numpy.random.randint(100, size=100), 
                                'Cat': [['A', 'B', 'C'][numpy.random.randint(3, size=1)[0]] for i in range(100)]})
    >>> scatterplot = (altair.Chart(data).mark_circle(size=60, opacity=0.5).encode(x='X', y='Y', color='Cat'))
    >>> altair.themes.register("theme_alberta", theme_alberta)
    >>> altair.themes.enable("theme_alberta")
    >>> scatterplot
    """

    # Code attribution: Sergio Sanchez
    # https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    # University font
    font = "Arial"
    labelFont = "Arial"

    # Specify colour palette for Alberta
    alberta_palette = ["#007C41", "#FFDB05", "#7D9AAA", "#A8B400", "#A79E70"]

    return {
        "config": {
            # Title font and size
            "title": {
                "fontSize" : 18,
                "font": font,
                "anchor": "start",
                "fontColor": "#000000"
            } ,
            # Axes font and sizes
            "axisX": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "X Axis Title (units)"
            },
            "axisY": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "Y Axis Title (units)"
            },
            # Add colour palette
            "range": {
                "category": alberta_palette
            }
        }
    }
