from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')


face_locations = face_recognition.face_locations(image)


#loop through fce locations
for face_location in face_locations:
    top, right, bottom, left = face_location

    #face image using the array
    face_image = image[top:bottom, left:right]

    #get actual dace image using pillow library
    pil_image = Image.fromarray(face_image)
    pil_image.show()

    #save imageof faces
    pil_image.save(f'{top}.jpg')