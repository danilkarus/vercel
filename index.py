import vk_api
import time

vk_session = vk_api.VkApi('89043933326', 'theflackmg123321111') # Вводите логин и пароль вашей странички
vk_session.auth()

vk = vk_session.get_api()

while True:
            response_ph = vk.photos.get(count = 1, album_id = 'profile', rev = 1)

            if response_ph ['items']:
                ph_id = response_ph['items'][0]
                ph_response_delete = vk.photos.delete(photo_id = ph_id['id'])
            response = vk.wall.get(count = 1)

            if response ['items']:
                post = response['items'][0]
                post_response_delete = vk.wall.delete(post_id = post['id'])

            # загружаем новую.
            upload = vk_api.VkUpload(vk_session)
            photo = upload.photo_profile('ava.jpg')

            response = vk.wall.get(count = 1)

            if response ['items']:
                post = response['items'][0]
                post_response_delete = vk.wall.delete(post_id = post['id'])
            time.sleep(60)
            response_ph = vk.photos.get(count = 1, album_id = 'profile', rev = 1)

            if response_ph ['items']:
                ph_id = response_ph['items'][0]
                ph_response_delete = vk.photos.delete(photo_id = ph_id['id'])
            response = vk.wall.get(count = 1)

            if response ['items']:
                post = response['items'][0]
                post_response_delete = vk.wall.delete(post_id = post['id'])

            # загружаем новую.
            upload = vk_api.VkUpload(vk_session)
            photo = upload.photo_profile('ava1.jpg')

            response = vk.wall.get(count = 1)

            if response ['items']:
                post = response['items'][0]
                post_response_delete = vk.wall.delete(post_id = post['id'])
            time.sleep(60)
    
