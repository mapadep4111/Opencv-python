import time
import random
import vk_api
import numpy as np
import cv2
from PIL import ImageGrab

vk_session = vk_api.VkApi('acount', 'password')
vk_session.auth()

vk = vk_session.get_api()

x = 0
#zero = np.zeros([100,100,3])
#print(zero)

upload = vk_api.VkUpload(vk_session)
zero = np.zeros([300,220,3],dtype='uint8')
cv2.rectangle(zero,(1,1),(219,299),(0,0,random.randint(0,255)),thickness=random.randint(-1,3))
cv2.imwrite('2.png',zero)

photo = upload.photo(  # Подставьте свои данные
        '2.png',
        album_id=272136266,
        group_id=190825223
    )

vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )

print(photo, '\nLink: ', vk_photo_url)

while True:
    screen = np.array(ImageGrab.grab(bbox=(0,40,1280,1024)))
    zero = np.zeros([300,220,3],dtype='uint8')
    cv2.rectangle(zero,(1,1),(219,299),(0,0,random.randint(0,255)),thickness=random.randint(-1,3))
    cv2.imwrite(str(x) + '.png',screen)

    '''print(vk.wall.post(message='(Подключена автоматизация : python ) \n Дата :'+ time.strftime("%x %H:%M:%S") + '\n' + 'Проверка целого числа с начала отсчета : ' + str(x) + "\n" + str(zero)))
    time.sleep(random.randint(0,1))'''

    photo = upload.photo(  # Подставьте свои данные
        str(x) + '.png',
        album_id=272136266,
        group_id=190825223
    )

    print(photo, '\nLink: ', vk_photo_url)
    if x == 0 :
        photo = upload.photo(  # Подставьте свои данные
            '0.png',
            album_id=272136266,
            group_id=190825223
        )

        print(photo, '\nLink: ', vk_photo_url)
    x = x + 1
