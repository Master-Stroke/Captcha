from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)

text = input('Что будет написано в капче: ')

captcha_text = {text}

save = input('Введите названия файла: ')

data = image.generate(captcha_text)

image.write(captcha_text, f'{save}')