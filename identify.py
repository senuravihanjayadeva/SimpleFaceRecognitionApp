import face_recognition
from PIL import Image, ImageDraw

################################################################################

image_of_senura = face_recognition.load_image_file('./img/known/Senura.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
senura_face_encoding = face_recognition.face_encodings(image_of_senura)[0]

################################################################################

image_of_lahiru = face_recognition.load_image_file('./img/known/Lahiru.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
lahiru_face_encoding = face_recognition.face_encodings(image_of_lahiru)[0]

################################################################################

image_of_rusiru = face_recognition.load_image_file('./img/known/Rusiru.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
rusiru_face_encoding = face_recognition.face_encodings(image_of_rusiru)[0]

################################################################################

image_of_kalana = face_recognition.load_image_file('./img/known/Kalana.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
kalana_face_encoding = face_recognition.face_encodings(image_of_kalana)[0]

################################################################################

#create array of encoding and names
known_face_encodings = [

 senura_face_encoding,
 lahiru_face_encoding,
 rusiru_face_encoding,
 kalana_face_encoding
 

]

known_face_names = [

    "Senura Jayadeva",
    "Lahiru Fernando",
    "Rusiru Abishek",
    "Kalana Gayanga"

]

#Load Test Image to find faces in
test_image = face_recognition.load_image_file('./img/groups/team4.jpg')

#find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#covert to PIL format
pil_image = Image.fromarray(test_image)

#create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identify.jpg')

