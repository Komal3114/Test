st = open("Student.txt","w")
st.write("Name : Komal Kushwaha \n Semester : 6th \n Enrollment No: 0501AD231035")
st.close()
print("File Created!")

st = open("Student.txt","r")
constant = st.read()
print(constant)
st.close()

st = open("Student.txt","a")
st.write("\n Name: Swaransh Taneja \n sem : 6th \n Enrollment No. : 0502AD231036")
st.close()
print("Data Added")

st = open("Student.txt","r")
print(st.read())
st.close()