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

    """
    # Typography
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
                "anchor": "start", # equivalent of left-aligned.
                "fontColor": "#000000"
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "tickSize": 5, # default, including it just to show you can change it
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "ticks": False, # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "Y Axis Title (units)", 
                # titles are by default vertical left of axis so we need to hack this 
                "titleAngle": 0, # horizontal
                "titleY": -10, # move it up
                "titleX": 18, # move it to the right so it aligns with the labels 
            },

            "range": {
                
                "category": main_palette,
            }
    }
    }