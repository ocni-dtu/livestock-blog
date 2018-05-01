Date: 2018-04-30
Modified: 2018-04-30
Status: draft
Authors: Christian Kongsgaard
Tags: livestock, python, grasshopper, 
Title: UTCI Speed Test
HeaderImage: /images/GH+Py.png
Summary: .

In this post I will compare the time it takes to compute the Universal Thermal Climate Index (UTCI).
First I will look at different ways of computing the UTCI in CPython. This post are written as a Jupyter Notebook, meaning
that you can try out the code yourself and check how long it takes to make the computations on your own machine.
In the second part I will implement the best performing UTCI algorithm in Grasshopper, comparing how it perform if you implement
it with the Livestock Template Method and just a normal Grasshopper Python Component.