import calendar
from .utils import can_create_file
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class Wallendar:
    """
    A class for generating a wallpaper with a calendar.
    """

    def __init__(self, source_path: str, target_path: str):
        # required params
        try:
            self._img = Image.open(source_path)
        except IOError:
            raise IOError("Unable to load image")
        try:
            can_create_file(target_path)
            self._target_path = target_path
        except IOError:
            raise IOError("Unable to write to target path")
        # optional params
        self._year = calendar.datetime.datetime.now().year
        self._month = calendar.datetime.datetime.now().month
        self._cal_width = -1  # auto
        self._offset_x = 0
        self._offset_y = 0
        self._font_size = -1  # auto
        self._font_path = "Ubuntu-R.ttf"
        self._font_color = tuple()
        self._header_color = tuple()
        self._highlighted_days = []
        self._highlight_color = (221, 72, 20)

    def year(self, year: int):
        """
        Set the year for the calendar.
        """
        self._year = year
        return self

    def month(self, month: int):
        """
        Set the month for the calendar.
        """
        self._month = month
        return self

    def cal_width(self, width: int):
        """
        Set the width of the calendar.
        """
        self._cal_width = width
        return self

    def offset_x(self, offset: int):
        """
        Set the x offset of the calendar.
        """
        self._offset_x = offset
        return self

    def offset_y(self, offset: int):
        """
        Set the y offset of the calendar.
        """
        self._offset_y = offset
        return self

    def font_size(self, size: int):
        """
        Set the font size of the calendar.
        """
        self._font_size = size
        return self

    def font_path(self, path: str):
        """
        Set the path to the font file.
        """
        # ToDo: font discovery
        self._font_path = path
        return self

    def highlight(self, days: list):
        """
        Highlight days in the calendar.
        """
        self._highlighted_days = days
        return self

    def highlight_color(self, color: tuple):
        """
        Set the color for the highlighted days.
        """
        self._highlight_color = color
        return self

    def font_color(self, color: tuple):
        """
        Set the color for the text.
        """
        self._font_color = color
        return self

    def header_color(self, color: tuple):
        """
        Set the color for the header.
        """
        self._header_color = color
        return self

    def generate(self):
        """
        Generate the wallpaper.
        """
        try:
            cal = calendar.monthcalendar(self._year, self._month)
        except ValueError:
            raise ValueError("Invalid year or month")

        # load font
        try:
            font = ImageFont.truetype(self._font_path)
        except IOError:
            raise IOError("Unable to load font")

        img_width, img_height = self._img.size

        if self._cal_width == -1:
            self._cal_width = img_width // 4
        cell_width = self._cal_width // 7

        if self._font_size == -1:
            self._font_size = cell_width // 2

        font = ImageFont.truetype(self._font_path, self._font_size)

        cell_height = cell_width
        header_height = cell_width
        table_height = header_height + (len(cal) * cell_height)

        # center table in image; add offset
        start_x = (img_width - self._cal_width) // 2
        start_y = (img_height - table_height) // 2
        # add offset
        start_x += self._offset_x
        start_y += self._offset_y

        draw = ImageDraw.Draw(self._img)

        if self._font_color == ():
            # calculate ideal font color
            region = self._img.crop((start_x, start_y, start_x +
                                    self._cal_width, start_y + table_height))
            average_color = np.array(region).mean(axis=(0, 1))
            brightness = np.mean(average_color)
            self._font_color = (0, 0, 0) if brightness > 127 else (
                255, 255, 255)  # Black or white

        if self._header_color == ():
            self._header_color = self._font_color

        # draw weekday header
        weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        for i, day in enumerate(weekdays):
            x = start_x + i * cell_width + 10
            draw.text((x, start_y + 10), day,
                      fill=self._header_color, font=font)

        # draw calendar days
        for row_idx, week in enumerate(cal):
            for col_idx, day in enumerate(week):
                if day != 0:
                    x = start_x + col_idx * cell_width + 15
                    y = start_y + header_height + row_idx * cell_height + 10
                    if day in self._highlighted_days:
                        draw.text((x, y), str(day),
                                  fill=self._highlight_color, font=font)
                    else:
                        draw.text((x, y), str(day),
                                  fill=self._font_color, font=font)

        self._img.save(self._target_path)
