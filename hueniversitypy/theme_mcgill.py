def theme_mcgill():
    """ 
    Applies McGill University's theme to all subsequential altair plot objects so they are displayed with the McGill visual identity.
    See the visual identity at https://mcgill.ca/visual-identity/visual-identity-guide#mcgilllogo. 
    See more details about the package on GitHub: https://github.com/UBC-MDS/hueniversitypy/blob/master/README.md 
     
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    an altair plot with the McGill University's visual identity colour theme applied. 

    Example
    ----------
    >>> from hueniversitypy.theme_mcgill import *
    >>> data = pandas.DataFrame({'X': numpy.random.randint(100, size=100), 
                                'Y': numpy.random.randint(100, size=100), 
                                'Cat': [['A', 'B', 'C'][numpy.random.randint(3, size=1)[0]] for i in range(100)]})
    >>> scatterplot = (altair.Chart(data).mark_circle(size=60, opacity=0.5).encode(x='X', y='Y', color='Cat'))
    >>> alt.themes.register('theme_mcgill', theme_mcgill)
    >>> alt.themes.enable('theme_mcgill')
    >>> scatterplot
    
    """
    # Code attribution: Sergio Sanchez
    # https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    # University font
    font = "Lato"
    labelFont = "Lato" 

    # Specify colour palette for McGill
    main_palette = ["#ED1B2F","#FFD794","#B5E1E1","#C8EAF5","#D5E6A8",]

    return {
        "config": {
            # Title font and size
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", 
                "fontColor": "#000000"
            },
            # Axes font and sizes
            "axisX": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "title": "X Axis Title (units)", 
                "titleFont": font,
                "titleFontSize": 12
             },
            "axisY": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "title": "Y Axis Title (units)", 
                "titleFont": font,
                "titleFontSize": 12

            },
             # Add colour palette
            "range": {
                "category": main_palette,
            }
        }
    }
