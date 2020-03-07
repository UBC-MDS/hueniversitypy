def theme_ubc():
    """ 
    Applies a University of British Columbia theme to all subsequential altair plot objects so they are displayed with the UBC visual identity. 
    See the visual identity at https://brand.ubc.ca/guidelines/downloads/ubc-colour-and-fonts/ 
		
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    an altair plot with the UBC visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_ubc', theme_ubc)
    >>> alt.themes.enable('theme_ubc')
    """
    #attribution to Sergio Sanchez 
    #https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    font = "Arial"
    labelFont = "Arial" 
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    # Colors
    main_palette = ['#002145', '#0055B7', '#00A7E1', '#40B4E5', '#6EC4E8', '#97D4E9']

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
