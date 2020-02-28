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
