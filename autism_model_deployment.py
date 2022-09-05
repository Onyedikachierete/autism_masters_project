import streamlit as st
import pickle
import pandas as pd

st.title("Autism Prediction Model")

st.text("An App Built by Onyedikachi A. Erete")
st.text("Student ID: B00858757")
st.text("School of Computing, Engineering and Intelligent Systems, Magee Campus")
st.text("Supervisor: Dr. Saugat Bhattacharyya")

st.write("This app uses 17 inputs to classify patients as autistic or non autistic using the model built on the autism dataset. Use the form below to get started!")

autism_pickle = open("autism_classification_model.pickle", "rb")
aut = pickle.load(autism_pickle)
autism_pickle.close()

A1_Score = st.selectbox("I often notice small sounds when others do not:", options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A2_Score = st.selectbox("I usually concentrate more on the whole picture, rather than the small details:", options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A3_Score = st.selectbox("I find it easy to do more than one thing at once:",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A4_Score = st.selectbox("If there is an interruption, I can switch back to what I was doing very quickly:",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A5_Score = st.selectbox("I find it easy to 'read between the lines' when someone is talking to me:",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A6_Score = st.selectbox("I know how to tell if someone listening to me is getting bored:",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A7_Score = st.selectbox("When I'm reading a story I find it difficult to work out the characters' intentions:", options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A8_Score = st.selectbox("I like to collect information about categories of things(e.g. types of car, types of bird, types of train, types of plant etc):",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A9_Score = st.selectbox("I find it easy to work out what someone is thinking or feeling just by looking at their face:",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
A10_Score = st.selectbox("I find it difficult to work out people's intentions:",  options = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"])
age = st.number_input("Age:", min_value = 0)
gender = st.selectbox("Gender:", options = ["Female", "Male"])
ethnicity = st.selectbox("Ethnicity:", options = ["Asian", "Black", "Hispanic", "Latino", "Middle_Eastern", "Pasifika", "South_Asian", "Turkish", "White_European", "Others"])
jaundice = st.selectbox("Did you have Jaundice at the Time of Birth?", options = ["Yes", "No"])
austim = st.selectbox("Has your immediate Family Member been Diagnosed with Autism before?", options = ["Yes", "No"])
used_app_before = st.selectbox("Have you Used this App Before?", options = ["Yes", "No"])
relation = st.selectbox("Relation:", options = ["Health_care_professional", "Parent", "Relative", "Self", "Others"])

#One Hot Encoding A1-A10 Score Variables
#From the Autism Spectrum Quotient, A1-A10 are answers to questions patients were asked.
#For A1, A7, A8 and A10, 1 is the score for those who "definitely or slightly" agree and 0 is the score for those who "slightly or definitely" disagree.
#For A2, A3, A4, A5, A6 and A9, 0 is the score for patients who "definitely or slightly" agree and 1 for those who "sligthly or definitely" disagree.
if (A1_Score == "Definitely Agree") or (A1_Score == "Slightly Agree"):
    A1_Score = 1
else:
    A1_Score = 0


if (A7_Score == "Definitely Agree") or (A7_Score == "Slightly Agree"):
    A7_Score = 1
else:
    A7_Score = 0

if (A8_Score == "Definitely Agree") or (A8_Score == "Slightly Agree"):
    A8_Score = 1
else:
    A8_Score = 0

if (A10_Score == "Definitely Agree") or (A10_Score == "Slightly Agree"):
    A10_Score = 1
else:
    A10_Score = 0


if (A2_Score == "Definitely Disagree") or (A2_Score == "Slightly Disagree"):
    A2_Score = 1
else:
    A2_Score = 0

if (A3_Score == "Definitely Disagree") or (A3_Score == "Slightly Disagree"):
    A3_Score = 1
else:
    A3_Score = 0


if (A4_Score == "Definitely Disagree") or (A4_Score == "Slightly Disagree"):
    A4_Score = 1
else:
    A4_Score = 0


if (A5_Score == "Definitely Disagree") or (A5_Score == "Slightly Disagree"):
    A5_Score = 1
else:
    A5_Score = 0


if (A6_Score == "Definitely Disagree") or (A6_Score == "Slightly Disagree"):
    A6_Score = 1
else:
    A6_Score = 0


if (A9_Score == "Definitely Disagree") or (A9_Score == "Slightly Disagree"):
    A9_Score = 1
else:
    A9_Score = 0
    
#One Hot Encode Ethnicity Variable
ethnicity_Asian, ethnicity_Black, ethnicity_Hispanic, ethnicity_Latino, ethnicity_Middle_Eastern, ethnicity_Pasifika, ethnicity_South_Asian, ethnicity_Turkish, ethnicity_White_European, ethnicity_Others = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
if ethnicity == 'Black':
    ethnicity_Black = 1
elif ethnicity == 'Hispanic':
    ethnicity_Hispanic = 1
elif ethnicity == 'Latino':
    ethnicity_Latino = 1
elif ethnicity == 'Middle-Eastern':
    ethnicity_Middle_Eastern = 1
elif ethnicity == 'Pasifika':
    ethnicity_Pasifika = 1
elif ethnicity == 'South_Asian':
    ethnicity_South_Asian = 1
elif ethnicity == 'Turkish':
    ethnicity_Turkish = 1
elif ethnicity == 'White_European':
    ethnicity_White_European = 1
elif ethnicity == 'Others':
    ethnicity_Others = 1

#One Hot Enconde Gender Variable
gender_m = 0
if gender == 'Male':
    gender_m = 1

#One Hot Encode Jaundice Variable
if jaundice == 'Yes':
    jaundice = 1
else:
    jaundice = 0

#One Hot Encode Austim Variable
if austim == 'Yes':
    austim = 1
else:
    austim = 0

#One Hot Encode Used_App_Before variable
if used_app_before == 'Yes':
    used_app_before = 1
else:
    used_app_before = 0

#One Hot Encode Relation Variable
relation_Health_care_professional, relation_Parent, relation_Relative, relation_Self, relation_Others = 0, 0, 0, 0, 0
if relation == 'Parent':
    relation_Parent = 1
elif relation == 'Relative':
    relation_Relative = 1
elif relation == 'Self':
    relation_Self = 1
elif relation == 'Others':
    relation_Others = 1
    
my_predictors = {
    'A1_Score': A1_Score, 
    'A2_Score': A2_Score, 
    'A3_Score': A3_Score, 
    'A4_Score': A4_Score, 
    'A5_Score': A5_Score,
    'A6_Score': A6_Score,
    'A7_Score': A7_Score, 
    'A8_Score': A8_Score, 
    'A9_Score': A9_Score, 
    'A10_Score': A10_Score, 
    'age': age,
    'jaundice': jaundice,
    'austim': austim,
    'used_app_before': used_app_before, 
    'gender_m': gender_m,
    'ethnicity_Black': ethnicity_Black,
    'ethnicity_Hispanic': ethnicity_Hispanic, 
    'ethnicity_Latino': ethnicity_Latino,
    'ethnicity_Middle_Eastern': ethnicity_Middle_Eastern,
    'ethnicity_Others': ethnicity_Others, 
    'ethnicity_Pasifika': ethnicity_Pasifika,
    'ethnicity_South_Asian': ethnicity_South_Asian,
    'ethnicity_Turkish': ethnicity_Turkish,
    'ethnicity_White_European': ethnicity_White_European,
    'relation_Others':relation_Others,
    'relation_Parent':relation_Parent,
    'relation_Relative':relation_Relative,
    'relation_Self': relation_Self,
                  }


df = pd.DataFrame.from_dict([my_predictors])


prediction = aut.predict(df)

if st.button("Predict"):
    result = prediction[0]
    if result == 0:
        result = 'Non Autistic'
    else:
        result = 'Autistic'

    st.write("You are Predicted to be {}".format(result))