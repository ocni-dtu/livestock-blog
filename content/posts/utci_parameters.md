Date: 2018-10-21
Modified: 2018-10-21
Status: published
Authors: Christian Kongsgaard
Tags: python, livestock, comfort, utci
Title: UTCI Parameters
Summary: Ever wondered, which parameter in the UTCI calculation is the most important? 

The Universal Thermal Climate Index (UTCI) is a widely used outdoor comfort metric. It is currently released as a
6th order polynomial formula with four inputs: Mean Radiant Temperature, Air Temperature, Wind Speed and Relative 
Humidity. 

I often hear that different measures are needed for achieving outdoor comfort in different climates. These claims
often only backed up by experience and I therefore figured that a parameter study of UTCI would be in place to bring 
some clarity.

The UTCI regression model is based on the advanced multi-node thermoregulation model 'Fiala', which tries to solve the 
human energy balance. The raw model is rather complex and time consuming to compute and therefore the authors of UTCI 
chose to fit a polynomial to approximate the original model. The polynomial takes four inputs; mean radiant temperature, 
air temperature, wind speed and relative humidity.

