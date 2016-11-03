### Full Stack Nano Degree resources ###
https://udacity.atlassian.net/wiki/display/BENDH/FSND+Student+Handbook

### tmux ###
Splitting terminals into windows/panes

### Python Debugging ###
* pdb

### Responsive Web Design ###
* Grunt - automates processes
* ImageOptim - optimizes image sizes
* ImageMagick - image processing tools

### Images with Markup ###
* Zocial font sent - popular social media icons

### Responsive Web Design ###
* Use srcset and sizes attributes on img tags
* For art direction, use figure element with media queries and srcsets for various combinations

Here's a rough example:
```
<picture>
    <source media="(max-width: 32em)" srcset="images/still_life-1600_large_2x.jpg 2x, images/still_life-800_large_1x.jpg 1x">
    <source srcset="images/still_life-1600_large_2x.jpg 1600w, images/still_life-800_large_2x.jpg 800w">
    <img src="images/still_life-800_large_1x.jpg" alt="This is a still life">
</picture>
```
