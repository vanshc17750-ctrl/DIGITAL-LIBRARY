import request
from PIL import Image
from io import BytesIO

r  = request.get("https://www.bing.com/images/search?view=detailV2&ccid=hXWwNOQw&id=CDD74C0F9635959D0D7E819CF4FEB696EE2BB835&thid=OIP.hXWwNOQw15ZVWKlMs-xv0wAAAA&mediaurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F30994370%2Fpexels-photo-30994370.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-optical-chemist-340351297-30994370.jpg%26fm%3Djpg&exph=336&expw=474&q=image&form=IRPRST&ck=B605357BC571076B0123B7DF1013E4E8&selectedindex=9&itb=1&ajaxhist=0&ajaxserp=0&vt=0&sim=11")
i = Image.open(BytesIO(r.content))
fp = open("image.jpg", "wb")
i.save(fp)
fp.close()