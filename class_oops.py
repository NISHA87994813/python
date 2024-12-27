class Student:
    name="";
    age="";
    salary="";
st=Student()
st.name="nisha";
st.age=20;
st.salary=30000;

st1=Student()
st1.name="ujala";
st1.age=22;
st1.salary=40000;
if st.salary>st1.salary:
    print(st.name)
    print(st.age)
    print(st.salary)
else:
    print(st1.name)
    print(st1.age)
    print(st1.salary)
