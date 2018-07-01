Date: 2018-07-01
Modified: 2018-07-01
Status: draft
Authors: Christian Kongsgaard
Tags: python, grasshopper, webinar, tutorial, livestock template method,
Title: Webinar: Grasshopper Components and the Livestock Template Method
HeaderImage: /images/webinar.png
Summary: 

Last week I did a webinar with [Thank God It's Computational](https://www.tgic.io/) 
on the Livestock Template Method.

We covered a more advanced example than the ones presented in the tutorials on this site. 
I showed how the Livestock Template Method could be used to calculate UTCI, similar to the way I did it,
for my [UTCI Post]({filename}/posts/utci_speed.md). 
We compared the time it took to compute the UTCI, using the component with the Livestock Template Method and the
Ladybug Tools implementation, which does the computation in Grasshopper. 
Furthermore I showed how you can minimize the amount of code in your Grasshopper component, by using it
as a shell. In that way you can keep your code in one editor, making it easier to reuse code and doing version control.

Lastly I showed how to modify the UTCI component so you can make the computation on a remote machine, using the
[SSH template]({filename}/posts/ssh.md).  

The webinar can we found at this [link](https://www.bigmarker.com/TGIC/Grasshopper-Components-and-the-Livestock-Template-Method),
 and the recording is available [here](somehere)

As said in the webinar, if you have any questions about the project or think you have project, 
where it would be benefitial to implement the Livestock Template Method, don't hesitate to contact me, 
my contact info can be found on this site. If you find any bugs please create a issue on 
[Github](https://github.com/livestock3d/livestock3d/issues)

Finally; a big thanks to Vignesh Kaushik for inviting and hosting the webinar. Also thanks to all the participants
who showed up and asked interesting questions.
