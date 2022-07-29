from PIL import Image

import glob


def watermark_with_photo(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    # transparent.show()
    transparent.save(output_image_path)



if __name__ == '__main__':
    # img = '4231.webp'
    for i in glob.glob("/Users/macbook/PycharmProjects/petsproject/final/*/*"):
        try:
            watermark_with_photo(i, i,
                             'maskfinal.png', position=(0,0))
            print("Finish", i )
        except Exception as e:
            print(e)
            print(i)



