<h1 align = "center"> Codechef Solutions Downloader </h1>
<h3 align = "center"> A web crawler that allows you to download all your AC submissions on CodeChef. </h3>

<h2 align = "center"> About </h2>

I came across many CodeChef Solution Downloaders but none of them worked for me, so I came up with my Python3-based script.

This script will allow you to document all your AC submissions on CodeChef for situations like when we try to download our solutions and archive them (a very cumbersome task, due to which people rarely try it). It doesn’t ship with a list of features and is a minimalist software for people who might want to download their submissions on this site. It supports all languages that are currently supported on CodeChef and saves the codes with appropriate extensions and downloads the user’s last accepted submission for a problem. The saved files are sorted according to their contest codes.

Edit: The downloader has been modified to fetch public submissions of a given user too

<h2 align = "center"> How to use? </h2>

Clone repository to your PC
Install dependencies:

    pip install lxml
    pip install bs4
    pip install requests

Run python3 main.py in CMD/Terminal and follow on-screen instructions

Let me know about any feedback, feature requests and bugs you face! (ᵔᴥᵔ)

<p align="center"> <h2 align = "center"> Proof of Concept</h2> </p>

<a href = "https://pastebin.com/vFcpNKBK">Console Output</a>

<img src = "https://s3.amazonaws.com/discourseproduction/original/2X/f/f34c6bfb9d6a5c664b83fd7ca55ee77c6b5523b9.png">

<h2 align = "center"> Credits </h2>

<p align="center"> <a href = "https://discuss.codechef.com/t/a-tool-to-download-all-your-successful-codechef-solutions-in-one-go/13890">mb1994’s project</a> </p>

<p align="center"> <a href = "https://discuss.codechef.com/t/codechef-solutions-downloader/30333">sandy999’s project</a> </p>


<h2 align = "center"> License </h2>
<p align="center"> <a href  = "https://github.com/ArnavVarshney/CCSolutionsDownloader/blob/master/LICENSE"> MIT License </a> </p>
