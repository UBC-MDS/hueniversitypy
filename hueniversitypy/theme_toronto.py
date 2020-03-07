def theme_toronto():
    """ 
    Applies a University of Toronto theme to all subsequential altair plot objects so they are displayed with the U of T visual identity. 
    See the visual identity at https://tinyurl.com/t3jjr49
    Three palettes based on the U of T visual identity guidelines can be selected: 'cool', 'vibrant' and 'awards'. 
	
    Parameters
    ----------
    palette : 'cool', 'vibrant' or 'awards'
    	specifies which colour palette defined in the visual identity documentation is used. 
	
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    	an altair plot with the U of T visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_toronto', theme_toronto)
    >>> alt.themes.enable('theme_toronto')

    attribution to Sergio Sanchez 
    https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602
    
    """
    # note U of T fonts are not open source, so most comprable fonts have been used for this package
    font = "Tahoma"
    # note U of T fonts are not open source, so most comprable fonts have been used for this package
    labelFont = "Tahoma" 
    sourceFont = "Tahoma"
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    # Colors
    main_palette = ["#002A5C","#FFE498","#E31837","#008BB0","#DAE5CD",]

    return {
        "config": {
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", 
                "fontColor": "#000000"
            },
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

            "range": {
                
                "category": main_palette,
            }
    }
    }