import face_recognition

image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')

#face encoding(This will get facial features that can compare to other images)

#[0] means this method gives an array we just want the first item
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]


#image to compare
#[0] means this method gives an array we just want the first item
#face encoding(This will get facial features that can compare to other images)
unknown_image = face_recognition.load_image_file('./img/unknown/bill-gates-4.jpg')

unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

#compare faces
results = face_recognition.compare_faces([bill_face_encoding],unknown_face_encoding )

if results[0]:
    print('This is Bill Gates')
else:
    print('This is not Bill Gates')