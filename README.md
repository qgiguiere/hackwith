# Hackwith

The source code for the website hackwith.dev

The purpose of this project is to create a collection of free and open source tools for anyone interested in cybersecurity. There are many great sources for finding new tools but I found myself spending a lot of time on tools that didn't work or finding a different tool later that was better than the one I was using and having to start over. I wanted to make something that would provide more information up front and make it easier to compare tools and decide which one you want to use.

I made the website open source so that others could easily add their tools or tools that they use. If you would like to add a tool to the site, see the guidelines below.

## Contributing

If you want to add the tool please make a pull request. All the information on the tools is stored in json files at `static/json`. Find the json file that applies to the to the tool and edit it following the format of the file. Generally this will include the following information:

`name` - The name of the tool

`description` - a brief description of the tool. Usually the header of the Github repo will work but it can be different if it describes the tool better.

`language` - The programming language the tool is written in.

`maintained` - Whether or not the tool is currently maintained.

`link` - link to the Github repo or wherever the tool is hosted.

`stars` - the number of stars it has on Github. If it is not on Github, put blank quotation marks instead `""`. A script updates the star count daily so don't worry about updating it if the count changes.

`id` - make sure your version is up to date and enter the number following the previous tool on the list.

`author` - The author of the tool if it is easy to find. Not required if you can't figure it out in a reasonable amount of time.

If you want to edit information about a tool already on the site, please submit a pull request and provide information about why your edit is correct. 

## To Do

* Improve the UI - I kept it simple but if anyone wants to edit it to make it look better please feel free.
* Add more categories
* Add more granular options - such as Android & iOS instead of just mobile.
