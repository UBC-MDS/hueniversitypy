def theme_mcgill():
    """ 
    Applies Mcgill University's theme to all subsequential altair plot objects so they are displayed with the Mcgill visual identity. 
     
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
        an altair plot with the Mcgill University's visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_mcgill', theme_mcgill)
    >>> alt.themes.enable('theme_mcgill')
    """

    # Typography
    font = "Lato"
    # At theme_mcgill it's the same font for all text but it's good to keep them separate in case you want to           #change one later.
    labelFont = "Lato" 
    sourceFont = "Lato"
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    # Colors
    main_palette = ["#ED1B2F","#FFD794","#B5E1E1","#C8EAF5","#D5E6A8",]

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
    alt.themes.register("theme_mcGill", theme_mcgill)
    alt.themes.enable("theme_mcGill")
    
    
    
