def theme_mcgill():
    """ 
    Applies McGill University's theme to all subsequential altair plot objects so they are displayed with the McGill visual identity.
    See the visual identity at https://mcgill.ca/visual-identity/visual-identity-guide#mcgilllogo
     
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    an altair plot with the McGill University's visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_mcgill', theme_mcgill)
    >>> alt.themes.enable('theme_mcgill')
    """

    # Typography
    font = "Lato"
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
                "anchor": "start", 
                "fontColor": "#000000"
            },
            # Axes fonts and sizes
            "axisX": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "title": "Y Axis Title (units)", 
            },
             # Adding colour palette
            "range": {
                
                "category": main_palette,
            }
    }
    }
    alt.themes.register("theme_mcGill", theme_mcgill)
    alt.themes.enable("theme_mcGill")

