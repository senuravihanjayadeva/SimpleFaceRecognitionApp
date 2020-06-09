import face_recognition
from PIL import Image, ImageDraw


image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]



image_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

#create array of encoding and names
known_face_encodings = [

 bill_face_encoding,
 steve_face_encoding
 

]

known_face_names = [

    "Bill Gates",
    "Steve Jobs"

]

#Load Test Image to find faces in
test_image = face_recognition.load_image_file('./img/groups/bill-steve.jpg')

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

