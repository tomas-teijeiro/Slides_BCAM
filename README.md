## Slides for ECCOMAS 2024

These slides correspond to the presentation *Generating Efficient Randomized Quadrature Rules for 2D and 3D Trunk Spaces using Machine Learning*, by T. Teijeiro, D. Pardo and V. Calo. 

They were presented In session: [MS005D - Deep Learning Computing IV](https://eccomas2024.org/event/session/57b14175-f81f-11ee-a60e-000c29ddfc0c)

Slides created with [Reveal.js](https://revealjs.com/).

### Export to PDF:

For a proper export to `pdf`, run the following command (adjusting the `--max-slides` flag accordingly):

```bash
$ docker run --rm -t --net=host -v `pwd`:/slides -v "/usr/share/fonts:/home/node/.local/share/fonts" astefanutti/decktape generic --key=" " --max-slides=52 index.html slides.pdf
```

### Tuning the CSS Theme:

The current Theme is named *BCAM* and is a modification of [*white*](https://revealjs.com/themes/). If you want to modify it, or add additional CSS rules, this should be done in `css/theme/source/bcam.scss`. Then, this file should be compiled with [SASS](https://sass-lang.com/) as follows:

```bash
$ sass css/theme/source/bcam.scss dist/theme/bcam.css
```

