def theme_alberta(palette='alpha'):
    """ 
    Applies a University of Alberta theme to all subsequential altair plot objects so they are displayed with the U of A visual identity.
    See the visual identity at https://www.ualberta.ca/toolkit/visual-identity/our-colours. 
    Four palettes based on the U of A visual identity guidelines can be selected: 'alpha', 'beta', 'gamma' and 'delta'.
	
    Parameters
    ----------
    palette : 'alpha', 'beta', 'gamma' or 'delta'
    	specifies which colour palette defined in the visual identity documentation is used. 
	
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    	an altair plot with the U of A visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_alberta', theme_alberta)
    >>> alt.themes.enable('theme_alberta')
    
    """