from PIL import Image

predir=r'D:\ustb78\【Sync】\pro\教材\教改编译结题相关\教改编译结题相关\参考资料\\'

image = Image.open(predir+'img9.jpg' )
                   



width, height = image.size
width = int(width * 2.378*0.5)
height = int(height * 2.12*0.5)

image = image.resize((width, height))
image.save(predir+r"scale.jpg")