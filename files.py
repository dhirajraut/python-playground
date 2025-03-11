
if __name__ == "__main__":

  try:
    with open("data.txt") as file:
      contents = file.read()
      print (contents)
      contents = contents.replace("\n", " ")
      tokens = contents.split(" ")
      print (tokens)
  except FileNotFoundError:
    print ("file doesnt exists.")

  try:
    with open("data_copy.txt", "w") as newFile:
      newFile.write (contents)
  except FileExistsError: # For demonstration. In this case file will be overwritten.
    print ("file exists")
