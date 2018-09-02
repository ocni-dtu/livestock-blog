## Github Repository for Livestock3D Web page
Go to [Livestock3D](https://livestock3d.github.io/) to visit the site.

## Pelican

* The Livestock3D web page is build with [Pelican](http://docs.getpelican.com/en/stable/)
* A tutorial on how to use it can be found [here](http://pythonforundergradengineers.com/how-i-built-this-site-1.html)
* The docs for Pelican can be found [here](http://docs.getpelican.com/en/stable/)
* You will need to pip install pelican and gh-pages to update the web page.

## Maintaining the Web Page

If you want to update the web page clone the repo.
There is two branches: master and development.

* master is hosting the web page
* development is where you create the content

When you have cloned the repo; checkout the development branch.
Create all your changes and in the terminal call:

> pelican content -o output -s pelicanconf.py

Commit and push your changes. Then call in the terminal:

> ghp-import -b master output

This will put everything from the output folder to the master branch.

Checkout master and push your changes.