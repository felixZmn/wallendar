from wallendar import Wallendar


def run():
    wallendar = Wallendar(source_path="/home/felix/Pictures/Bilder/_photography/NxC7GeM.jpg",
                          target_path="/home/felix/output.png")
    wallendar.highlight_color((221, 72, 20)).highlight(
        [3, 8, 15, 23, 28]).offset_x(-600)

    wallendar.generate()


if __name__ == '__main__':
    run()
