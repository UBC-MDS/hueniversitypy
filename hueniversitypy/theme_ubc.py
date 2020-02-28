def theme_ubc(palette='blue'):
    """ 
    Applies a University of British Columbia theme to all subsequential altair plot objects so they are displayed with the UBC visual identity. 
    Two palettes based on the UBC visual identity guidelines can be selected: 'blue' and 'white'. 
	
    Parameters
    ----------
    palette : 'blue' or 'white'
    	specifies which colour palette defined in the visual identity documentation is used. 
	
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    	an altair plot with the UBC visual identity colour theme applied. 

    Example
    ----------
    >>> alt.themes.register('theme_ubc', theme_ubc)
    >>> alt.themes.enable('theme_ubc')

    """
