def theme_toronto():
    """ 
    Applies a University of Toronto theme to all subsequential altair plot objects so they are displayed with the U of T visual identity. 
    See the visual identity at https://tinyurl.com/t3jjr49
    Three palettes based on the U of T visual identity guidelines can be selected: 'cool', 'vibrant' and 'awards'. 

	
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    	an altair plot with the U of T visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_toronto', theme_toronto)
    >>> alt.themes.enable('theme_toronto')

    """
    
    # Code attribution: Sergio Sanchez
    # https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    # note U of T fonts are not open source, so the most comparable font has been used for this package
    font = "Tahoma"
    labelFont = "Tahoma" 

    # Specify colour palette for Toronto
    main_palette = ["#002A5C","#FFE498","#E31837","#008BB0","#DAE5CD",]

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
                "titleFont": font,
                "titleFontSize": 12,
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "Y Axis Title (units)", 
            },
            # Add colour palette
            "range": {
                "category": main_palette,
            }
        }
    }
