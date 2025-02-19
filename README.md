<h3 align="center">
Wallendar: Turn your wallpaper into a beautiful calendar.
</h3>

<p align="center">
Take your wallpaper to the next level and turn it into a beautiful calendar.
</p>

![example](/docs/example1.png)

## Features

-   **Easy to use**: Create your first wallpaper in just a few lines of code.
-   **Smart layout**: Automatically adjusts size, color and other parameters to fit your wallpaper
-   **Customizable**: Change the font, the color, the position, and much more to fit your needs.

## Installation

To install Wallendar, you currently need to clone the repository - no pip package is available yet, sorry!

```bash
git clone git@github.com:felixZmn/wallendar.git
cd wallendar
pip install -r requirements.txt
```

## Usage

Creating your first Wallpaper is quite easy: Define the path to your wallpaper and where you want to save the new wallpaper - that's it!

```python
from wallendar import Wallendar

wallendar = Wallendar(
    wallpaper_path="path/to/your/wallpaper.jpg",
    output_path="path/to/save/your/new/wallpaper.jpg",
)
wallendar.generate()
```

## Customization

To fit your needs, Wallendar offers a variety of customization options. You can change the font, the color, the position, and much more.

| Option              | Default                    | Description                                                                    |
| ------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| `.year()`           | current year               | The calendar year                                                              |
| `.month()`          | current month              | The calendar month                                                             |
| `.cal_width()`      | 1/4 of the wallpaper width | The width of the calendar                                                      |
| `offset_x()`        | `0`                        | The x-offset from the center of the wallpaper                                  |
| `offset_y()`        | `0`                        | The y-offset from the center of the wallpaper                                  |
| `font_color()`      | auto                       | The base color of the calendar                                                 |
| `font_size()`       | auto                       | Size of the font                                                               |
| `font_path()`       | Ubuntu-R.ttf               | Name of the font file or path to the font file, if not at the default location |
| `highlight()`       | []                         | a list of days to highlight, e.g. [1, 15, 31]                                  |
| `highlight_color()` | (221, 72, 20)              | The color of the highlighted days, as RGB tuple                                |
| `header_color()`    | same as `font_color()`     | The color of the header                                                        |
