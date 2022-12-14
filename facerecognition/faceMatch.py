import face_recognition as fc

image_of_bill = fc.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = fc.face_encodings(image_of_bill)[0]

unknown_image = fc.load_image_file('./img/unknown/bill-gates-4.jpg')
unknown_face_encoding = fc.face_encodings(unknown_image)[0]

results = fc.compare_faces([bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print('This is not Bill Gates')