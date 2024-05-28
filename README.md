## Presentations by T. Teijeiro

This repository contains different presentations given by T. Teijeiro as a [BCAM](https://www.bcamath.org) researcher. The slides of each presentation are in a different branch, with this README file updated accordingly.

Slides are created with [Reveal.js](https://revealjs.com/), and deployed using Github pages. Only one presentation is deployed at a given time.

### Export to PDF:

For a proper export to `pdf`, run the following command (adjusting the `--max-slides` flag accordingly):

```bash
$ docker run --rm -t --net=host -v `pwd`:/slides -v "/usr/share/fonts:/home/node/.local/share/fonts" astefanutti/decktape generic --key=" " --max-slides=50 index.html slides.pdf
```

### Tuning the CSS Theme:

The current Theme is named *BCAM* and is a modification of [*white*](https://revealjs.com/themes/). If you want to modify it, or add additional CSS rules, this should be done in `css/theme/source/bcam.scss`. Then, this file should be compiled with [SASS](https://sass-lang.com/) as follows:

```bash
$ sass css/theme/source/bcam.scss dist/theme/bcam.css
```

