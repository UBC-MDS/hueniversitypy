def theme_toronto(palette='cool'):
    """ 
    Applies a University of Toronto theme to all subsequential altair plot objects so they are displayed with the U of T visual identity. 
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
