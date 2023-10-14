filename = input("File name: ")
if filename.endswith(".jpg"):
 print("image/jpeg")
elif filename.endswith(".jpeg"):
 print("image/jpeg")
elif filename.endswith(".png"):
 print("image/png")
elif filename.endswith(".pdf"):
 print("application/pdf")