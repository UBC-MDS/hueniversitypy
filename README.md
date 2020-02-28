## hueniversitypy

![](https://github.com/UBC-MDS/hueniversitypy/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/hueniversitypy/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/hueniversitypy) ![Release](https://github.com/UBC-MDS/hueniversitypy/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/hueniversitypy/badge/?version=latest)](https://hueniversitypy.readthedocs.io/en/latest/?badge=latest)

Python package for creating visualizations in line with visual identities of Canadian universities

### Summary

### `hueniversitypy` in the Python ecosystem

The hueniversitypy package fits into the python ecosystem with other python packages that allow users to change the theme of plot objects. This package is different than others as it utilizes the altair plotting package rather than other types of plotting packages. As a result there are very few packages in the Python ecosystem that apply themes to altair plots, as described in this [GitHub issue]( https://github.com/altair-viz/altair/issues/1333). One other package that is designed to change the theme of altair plots for Los Angeles Times publications can be found [here]( https://github.com/datadesk/altair-latimes). Our package will be different as the goal of the change in plot theme is to adhere to certain university visual identities, rather than the LA times theme.  

### Installation:

```
pip install -i https://test.pypi.org/simple/ hueniversitypy
```
#### Functions used in the package
- `theme_alberta()` - creates visualizations in line with [the University of Alberta's visual identity](https://www.ualberta.ca/toolkit/visual-identity/our-colours)
- `theme_mcgill()` - creates visualizations in line with [McGill University's visual identity](https://mcgill.ca/visual-identity/visual-identity-guide#mcgilllogo)
- `theme_toronto()` - creates visualizations in line with [the University of Toronto's visual identity](https://www.utm.utoronto.ca/communications/sites/files/communications/public/shared/UofT%20Style%20Guide%20%2B%20Boundless%20Guide%20Feb%202012.pdf)
- `theme_ubc()` - creates visualizations in line with [the University of British Columbia's visual identity](https://brand.ubc.ca/guidelines/downloads/ubc-colour-and-fonts/)

### Features
- TODO

### Dependencies

- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://hueniversitypy.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
