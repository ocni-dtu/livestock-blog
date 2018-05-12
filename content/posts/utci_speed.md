Date: 2018-05-11
Modified: 2018-05-11
Status: draft
Authors: Christian Kongsgaard
Tags: livestock, python, grasshopper, 
Title: UTCI Speed Test
HeaderImage: /images/GH+Py.png
Summary: .

I'm sure that some of you, who are reading this have experienced that some Grasshopper components takes a long time to
run. Some of the components you can download are quite computational expensive and therefore takes a long time to compute. 
Eventhough Rhino 6 should make it possible to run components on multiple cores, and thereby cutting down the computation 
 time, I thought a small study on other measures to speed up your own components would be in place.

For the speed test I will use the equation for [Universal Thermal Climate Index (UTCI)](http://www.utci.org/), which is a
6th degree polynomial, which should be efficient to demonstrate the computation time. 
[Ladybug Tools](http://www.food4rhino.com/app/ladybug-tools) have implemented the
equation in one of their components and I have taken that implementation (striped it for some input checks) and I will 
start by comparing the time it takes to compute the UTCI, when you feed the data into the component, in the three different ways
you can in Grasshopper; Item, List and as a Tree. If you are interested in testing it yourself, you can download the 
Grasshopper script I used for it [here]({filename}/data/Time UTCI.gh). 

In the second part of this post I will show how fast the UTCI can be computed in CPython, and what can be done to try 
to reach that speed, when in Grasshopper using the [Livestock Template Method]({filename}/how_is_it_working.md).

## Grasshopper
![alt text]({filename}/images/utci_speed_3.png)

I have used the built-in timer in Grasshopper to test how long it takes to compute UTCI, if the component takes the input
data as Item, List or Tree data. The components, which takes lists and trees are looping through the data inside the component.
The graph above clearly shows that looping through your data, whether it is a list or tree is much much faster than implementing 
the component to take Item inputs. Interesting enough; is the tree input a little bit faster than the pure list. I'm not
that familiar with the internals of Grasshopper, to have a good explanation for that, but maybe someone can elaborate on 
it in the comments. I have implemented it so that, while I add another year to the list implementation, I put the new year
to another tree-branch in the tree implementation. So in each tree-branch there is only one year worth of data.   