from PIL import Image,ImageDraw
import face_recognition as fc

image_of_bill = fc.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = fc.face_encodings(image_of_bill)[0]

image_of_steve = fc.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding = fc.face_encodings(image_of_steve)[0]

known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_names = [
    "Bill Gates",
    "Steve Jobs"
]

test_image = fc.load_image_file('./img/groups/bill-steve-elon.jpg')

# find faces in test image
face_locations = fc.face_locations(test_image)
face_encodings = fc.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
    matches = fc.compare_faces(known_face_encodings,face_encoding)
    name = "unknown person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    
    # draw box
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))

    # draw label
    text_width,text_height = draw.textsize(name)
    draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6,bottom-text_height-5),name,fill=(255,255,255,255))

# delete the instance from memory
del draw

# display image
pil_image.show()