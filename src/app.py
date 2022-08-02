import pandas as pd 

url = 'https://raw.githubusercontent.com/4GeeksAcademy/decision-tree-project-tutorial/main/diabetes.csv'
df = pd.read_csv(url, header=0, sep=",")

#Step 2:
df.head(5)
df.info()
df.describe()
df.sample(5)
df[df['Pregnancies']==0]
len(df[df['BloodPressure']==0])
len(df[df['Insulin']==0])
f,ax=plt.subplots(figsize=(10,10))
sns.heatmap(df.corr(),annot=True,linewidths=0.5,linecolor="black",fmt=".1f",ax=ax)
plt.show()

df['Insulin']
df['Insulin'].value_counts()
len(df[df['BMI']==0])

#limpieza de datos
#insulina
df_0=df[(df['Outcome']==0) & (df["Insulin"] > 0)]
insuline_mean_0=df_0['Insulin'].mean()

df_no0=df[(df['Outcome']!=0) & (df["Insulin"] > 0)]
insuline_mean_no0=df_no0['Insulin'].mean()

def insulina(insulin_value, outcome_value, insuline_mean_0,insuline_mean_no0):
    if outcome_value==0 and insulin_value==0:
        return insuline_mean_0
    elif outcome_value==1 and insulin_value==0:
        return insuline_mean_no0
    else:
        return insulin_value

df['Insulin'] = df.apply(lambda x: insulina(x['Insulin'], x['Outcome'],insuline_mean_0,insuline_mean_no0), axis=1)

df.describe()

#limpieza de datos
#bmi
df_0=df[(df['Outcome']==0) & (df["BMI"] > 0)]
bmi_mean_0=df_0['BMI'].mean()

df_no0=df[(df['Outcome']!=0) & (df["BMI"] > 0)]
bmi_mean_no0=df_no0['BMI'].mean()

def BMI_fun(bmi_value, outcome_value, bmi_mean_0,bmi_mean_no0):
    if outcome_value==0 and bmi_value==0:
        return bmi_mean_0
    elif outcome_value==1 and bmi_value==0:
        return bmi_mean_no0
    else:
        return bmi_value

df['BMI'] = df.apply(lambda x: BMI_fun(x['BMI'], x['Outcome'],bmi_mean_0,bmi_mean_no0), axis=1)

df.describe()

#limpieza de datos
#Glucose
df_0=df[(df['Outcome']==0) & (df["Glucose"] > 0)]
glucose_mean_0=df_0['Glucose'].mean()

df_no0=df[(df['Outcome']!=0) & (df["Glucose"] > 0)]
glucose_mean_no0=df_no0['Glucose'].mean()

def glucose_fun(glucose_value, outcome_value, glucose_mean_0,glucose_mean_no0):
    if outcome_value==0 and glucose_value==0:
        return glucose_mean_0
    elif outcome_value==1 and glucose_value==0:
        return glucose_mean_no0
    else:
        return glucose_value

df['Glucose'] = df.apply(lambda x: glucose_fun(x['Glucose'], x['Outcome'],glucose_mean_0,glucose_mean_no0), axis=1)

df.describe()

#limpieza de datos
#BloodPressure
df_0=df[(df['Outcome']==0) & (df["BloodPressure"] > 0)]
BloodPressure_mean_0=df_0['BloodPressure'].mean()

df_no0=df[(df['Outcome']!=0) & (df["BloodPressure"] > 0)]
BloodPressure_mean_no0=df_no0['BloodPressure'].mean()

def BloodPressure_fun(BloodPressure_value, outcome_value, BloodPressure_mean_0,BloodPressure_mean_no0):
    if outcome_value==0 and BloodPressure_value==0:
        return BloodPressure_mean_0
    elif outcome_value==1 and BloodPressure_value==0:
        return BloodPressure_mean_no0
    else:
        return BloodPressure_value

df['BloodPressure'] = df.apply(lambda x: BloodPressure_fun(x['BloodPressure'], x['Outcome'],BloodPressure_mean_0,BloodPressure_mean_no0), axis=1)

df.describe()

#limpieza de datos
#SkinThickness
df_0=df[(df['Outcome']==0) & (df["SkinThickness"] > 0)]
SkinThickness_mean_0=df_0['SkinThickness'].mean()

df_no0=df[(df['Outcome']!=0) & (df["SkinThickness"] > 0)]
SkinThickness_mean_no0=df_no0['SkinThickness'].mean()

def SkinThickness_fun(SkinThickness_value, outcome_value, SkinThickness_mean_0,SkinThickness_mean_no0):
    if outcome_value==0 and SkinThickness_value==0:
        return SkinThickness_mean_0
    elif outcome_value==1 and SkinThickness_value==0:
        return SkinThickness_mean_no0
    else:
        return SkinThickness_value

df['SkinThickness'] = df.apply(lambda x: SkinThickness_fun(x['SkinThickness'], x['Outcome'],SkinThickness_mean_0,SkinThickness_mean_no0), axis=1)

df.describe()