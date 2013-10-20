# Buster

Super simple, Totally awesome, Brute force **static site generator for [Ghost](http://ghost.org "The Open Source Blogging Platform")**.

*Generate Static Pages. Preview. Deploy to Github Pages.*

## The interface

`setup [--gh-repo=<repo-url>]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a GIT repository inside `static/` directory.

`generate [--domain=<local-address>]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generates static pages from locally running Ghost instance.

`preview`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preview what's generated on `localhost:9000`.

`deploy`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Commits and deploys changes static files to Github repository.

`add-domain <domain-name>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Adds CNAME file with custom domain name as required by Github Pages.

Buster assumes you have `static/` folder in your current directory (or creates one during `setup` command). You can specify custom directory path using `[--dir=<path>]` option to any of the above commands.

## Requirements

* wget: Use `brew install wget` to install wget on your Mac. Available by default on most linux distributions.

The following python packages would be installed automatically when installed via `pip`:

* [docopt](https://github.com/docopt/docopt): Creates beautiful command line interfaces *easily*.
* [GitPython](https://github.com/gitpython-developers/GitPython): Python interface for GIT.

## Ghost. What?

[Ghost](http://ghost.org/features/ "Ghost Features.") is a beautifully designed, completely customisable and completely [Open Source](https://github.com/TryGhost/Ghost "Ghost on Github") **Blogging Platform**. If you haven't tried it out yet, check it out. You'll love it.

The Ghost Foundation is not-for-profit organization funding open source software and trying to completely change the world of online publishing. Consider [donating to Ghost](http://ghost.org/about/donate/ "You are awesome!")

### Buster?

Inspired by THE GhostBusters.

![Ghost Buster Movie](http://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png "Ghost Buster Movie Poster")


## Contributing

Checkout the existing [issues](https://github.com/axitkhurana/buster/issues) or create a new one. Pull requests welcome!


----


*Made with [jugaad](http://en.wikipedia.org/wiki/Jugaad) in [Dilli](http://en.wikipedia.org/wiki/Delhi).*
