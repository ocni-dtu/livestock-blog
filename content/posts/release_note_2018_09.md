Date: 2018-09-17
Modified: 2018-09-17
Status: published
Authors: Christian Kongsgaard
Tags: livestock, release
Title: Livestock Release 2018.09
HeaderImage: /images/release_2018_09.png
Summary: Announcement and release notes for Livestock 2018.09

I am really happy to announce the first public release of Livestock. So far Livestock has only existed as a biproduct 
of my [master thesis]({filename}/pages/portfolio.md), but over the summer I have worked hard on streamlining the 
workflow to make it more user-friendly. That also means that the number of components have gone down compared to what 
was part of the thesis, in order to focus on improving a subset of components and functionalities. However, the plan 
is to release all the components from my thesis, but it have to wait for a later release. Livestock is hereby moved 
from the "alpha-phase" into "beta" as I expect there is still some bugs crawling around. If you encounter any please 
create an [Github Issue](https://github.com/livestock3d/livestock/issues) and I will try to fix it as soon as possible.
 
[Kristoffer Negendahl](https://www.linkedin.com/in/kristoffernegendahl/) has gone from being my thesis supervisor to an 
more active, but equally valuable, part of the team. He has, besides counselling, been the first tester of Livestock 
and used it at his day job at [BIG](https://big.dk).

# Livestock
To read more about Livestock, what it can do, its goals and the philosophy behind; Please visit the 
[Livestock Introduction Page]({filename}/pages/livestock.md)

# Dependencies
Livestock depend on several other open source libraries and without them it would not have been possible to create Livestock.
So I would like to thank all of their maintainers and contributors for sharing their work with the world.
A special thanks to Philipp Kraft, who created [CMF](https://github.com/philippkraft/cmf) with him and his project 
Livestock would not have existed.

### Dependency List
* [CMF](https://github.com/philippkraft/cmf)
* [NumPy](https://github.com/numpy/numpy)
* [SciPy](https://github.com/scipy/scipy)
* [Progressbar](https://github.com/WoLpH/python-progressbar)
* [Shapely](https://github.com/simplegeo/shapely)
* [PyShp](https://github.com/GeospatialPython/pyshp)
 
# Livestock 2018.09 Release Notes
Download the [Livestock 2018.09 Release](https://github.com/livestock3d/livestock/releases) from Github and follow the 
[Installation Instructions]({filename}/posts/install.md)

## Grasshopper Components
The following components have been added to the Livestock Grasshopper package:

0 | Miscellaneous

* Livestock Python Executor

1 | Geometry

* Livestock Save Mesh
* Livestock Load Mesh

2 | CMF

* Livestock CMF Ground
* Livestock CMF Solve
* Livestock CMF Results
* Livestock CMF Outputs
* Livestock CMF Solver Settings


# Tutorials

[Hill Slope Run-Off]({filename}/posts/tutorial_hill_slope.md)
