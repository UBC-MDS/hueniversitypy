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
