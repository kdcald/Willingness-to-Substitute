# --------------------------------------------------------------- # 
# import libraries and data
# --------------------------------------------------------------- # 
import pandas as pd
import os
import numpy as np

# set working directory
path = "/Users/Krystal/Library/CloudStorage/GoogleDrive-kdcald@gmail.com/My Drive/Work/OpenPhil Contracting Work/Willingness to Substitute"
os.chdir(path)
os.getcwd()

# import raw data
df = pd.read_csv("To share/w-to-sub-raw-surveymonkey-data.csv", skiprows=[1])
long_colnames = pd.read_csv("To share/long_colnames.csv") # to later merge with long df


# --------------------------------------------------------------- # 
# clean data
# --------------------------------------------------------------- # 
# remove some empty columns
cols_to_remove = ['Collector ID', 'IP Address', 'Email Address', 'First Name', 'Last Name', 
                  'Custom Data 1', 'PROLIFIC_PID', 'STUDY_ID', 'SESSION_ID',
                  'Unnamed: 18',
                  'ELECTRONIC CONSENTPlease select your choice below. You may print a copy of this consent form for your records. Clicking on the “Agree” button indicates that:\n\nYou have read the above information\nYou voluntarily agree to participate\nYou are 18 years of age or older\n']
df.drop(cols_to_remove, axis=1, inplace=True)

# clean column names
new_col_names = {
'Respondent ID':'respondent_id', 
'Start Date':'start_date', 
'End Date' : 'end_date',
'Which of the following foods do you eat at least once/year?' : 'foods_eaten', 
'Unnamed: 11' : 'dairy_eats', 
'Unnamed: 12' : 'eggs_eats', 
'Unnamed: 13' : 'seafood_eats', 
'Unnamed: 14' : 'chicken_eats', 
'Unnamed: 15' : 'turkey_eats', 
'Unnamed: 16' : 'beef_eats', 
'Unnamed: 17' : 'pork_eats', 
'Which of the following dairy products do you eat at least once/year?' : 'dairy_product_butter', 
'Unnamed: 20' : 'dairy_product_cream', 
'Unnamed: 21' : 'dairy_product_cheesecottage', 
'Unnamed: 22' : 'dairy_product_cheesecheddar', 
'Unnamed: 23' : 'dairy_product_cheeseamerican', 
'Unnamed: 24' : 'dairy_product_cheeseother', 
'Unnamed: 25' : 'dairy_product_dressing', 
'Unnamed: 26' : 'dairy_product_icecream', 
'Unnamed: 27' : 'dairy_product_milk', 
'Unnamed: 28' : 'dairy_product_sourcream', 
'Unnamed: 29' : 'dairy_product_yogurt', 
'Unnamed: 30' : 'dairy_product_other', 
'Which of the following egg products do you eat at least once/year?' : 'eggs_product_eggs', 
'Unnamed: 32' : 'eggs_product_liquid', 
'Unnamed: 33' : 'eggs_product_mayo', 
'Unnamed: 34' : 'eggs_product_dried', 
'Unnamed: 35' : 'eggs_product_other', 
'Which of the following seafood products do you eat at least once/year?' : 'seafood_product_fishfresh', 
'Unnamed: 37' : 'seafood_product_fishcanned', 
'Unnamed: 38' : 'seafood_product_crab', 
'Unnamed: 39' : 'seafood_product_lobster', 
'Unnamed: 40' : 'seafood_product_imitationcrablobster', 
'Unnamed: 41' : 'seafood_product_shrimp', 
'Unnamed: 42' : 'seafood_product_crayfish', 
'Unnamed: 43' : 'seafood_product_clams', 
'Unnamed: 44' : 'seafood_product_mussels', 
'Unnamed: 45' : 'seafood_product_oysters', 
'Unnamed: 46' : 'seafood_product_scallops', 
'Unnamed: 47' : 'seafood_product_escargot', 
'Unnamed: 48' : 'seafood_product_calamari', 
'Unnamed: 49' : 'seafood_product_other', 
'Which of the following chicken products do you eat at least once/year?' : 'chicken_product_breast', 
'Unnamed: 51' : 'chicken_product_thighdrumstick', 
'Unnamed: 52' : 'chicken_product_wings', 
'Unnamed: 53' : 'chicken_product_ground', 
'Unnamed: 54' : 'chicken_product_roast', 
'Unnamed: 55' : 'chicken_product_sausage', 
'Unnamed: 56' : 'chicken_product_hotdog', 
'Unnamed: 57' : 'chicken_product_bacon', 
'Unnamed: 58' : 'chicken_product_deli', 
'Unnamed: 59' : 'chicken_product_cutlet', 
'Unnamed: 60' : 'chicken_product_nuggets', 
'Unnamed: 61' : 'chicken_product_finger', 
'Unnamed: 62' : 'chicken_product_canned', 
'Unnamed: 63' : 'chicken_product_jerky', 
'Unnamed: 64' : 'chicken_product_other', 
'Which of the following turkey products do you eat at least once/year?' : 'turkey_product_breast', 
'Unnamed: 66' : 'turkey_product_thighdrumstick', 
'Unnamed: 67' : 'turkey_product_wings', 
'Unnamed: 68' : 'turkey_product_ground', 
'Unnamed: 69' : 'turkey_product_roast', 
'Unnamed: 70' : 'turkey_product_sausage', 
'Unnamed: 71' : 'turkey_product_hotdog', 
'Unnamed: 72' : 'turkey_product_bacon', 
'Unnamed: 73' : 'turkey_product_deli', 
'Unnamed: 74' : 'turkey_product_cutlet', 
'Unnamed: 75' : 'turkey_product_nugget', 
'Unnamed: 76' : 'turkey_product_finger', 
'Unnamed: 77' : 'turkey_product_canned', 
'Unnamed: 78' : 'turkey_product_jerky', 
'Unnamed: 79' : 'turkey_product_organs', 
'Unnamed: 80' : 'turkey_product_other', 
'Which of the following beef products do you eat at least once/year?' : 'beef_product_steak', 
'Unnamed: 82' : 'beef_product_ribs', 
'Unnamed: 83' : 'beef_product_ground', 
'Unnamed: 84' : 'beef_product_sausage', 
'Unnamed: 85' : 'beef_product_hotdog', 
'Unnamed: 86' : 'beef_product_deli', 
'Unnamed: 87' : 'beef_product_roast', 
'Unnamed: 88' : 'beef_product_jerky', 
'Unnamed: 89' : 'beef_product_canned', 
'Unnamed: 90' : 'beef_product_bacon', 
'Unnamed: 91' : 'beef_product_cured', 
'Unnamed: 92' : 'beef_product_oragns', 
'Unnamed: 93' : 'beef_product_shank', 
'Unnamed: 94' : 'beef_product_other', 
'Which of the following pork products do you eat at least once/year?' : 'pork_product_loin', 
'Unnamed: 96' : 'pork_product_ground', 
'Unnamed: 97' : 'pork_product_roast', 
'Unnamed: 98' : 'pork_product_ribs', 
'Unnamed: 99' : 'pork_product_bacon', 
'Unnamed: 100' : 'pork_product_sausage', 
'Unnamed: 101' : 'pork_product_hotdog', 
'Unnamed: 102' : 'pork_product_deli', 
'Unnamed: 103' : 'pork_product_cured', 
'Unnamed: 104' : 'pork_product_canned', 
'Unnamed: 105' : 'pork_product_organs', 
'Unnamed: 106' : 'pork_product_rinds', 
'Unnamed: 107' : 'pork_product_ham', 
'Unnamed: 108' : 'pork_product_jerky', 
'Unnamed: 109' : 'pork_product_shank', 
'Unnamed: 110' : 'pork_product_other', 
'How familiar are you with plant-based alternatives for dairy products? Plant-based means that the product was made without animal-sourced ingredients.' : 'dairy_alternatives_familiar', 
'What types of products or brands do you think of for plant-based dairy alternatives?' : 'dairy_alternatives_brands', 
'How likely you would be to substitute each product with its plant-based alternative?' : 'dairy_sub_butter', 
'Unnamed: 114' : 'dairy_sub_cream', 
'Unnamed: 115' : 'dairy_sub_cheesecottage', 
'Unnamed: 116' : 'dairy_sub_cheesecheddar', 
'Unnamed: 117' : 'dairy_sub_cheeseamerican', 
'Unnamed: 118' : 'dairy_sub_cheeseother', 
'Unnamed: 119' : 'dairy_sub_dressing', 
'Unnamed: 120' : 'dairy_sub_icecream', 
'Unnamed: 121' : 'dairy_sub_milk', 
'Unnamed: 122' : 'dairy_sub_sourcream', 
'Unnamed: 123' : 'dairy_sub_yogurt', 
'Unnamed: 124' : 'dairy_sub_other', 
'Why are you willing to substitute these dairy products?' : 'dairy_why_butter', 
'Unnamed: 126' : 'dairy_why_cream', 
'Unnamed: 127' : 'dairy_why_cheesecottage', 
'Unnamed: 128' : 'dairy_why_cheesecheddar', 
'Unnamed: 129' : 'dairy_why_cheeseamerican', 
'Unnamed: 130' : 'dairy_why_cheeseother', 
'Unnamed: 131' : 'dairy_why_dressing', 
'Unnamed: 132' : 'dairy_why_icecream', 
'Unnamed: 133' : 'dairy_why_milk', 
'Unnamed: 134' : 'dairy_why_sourcream', 
'Unnamed: 135' : 'dairy_why_yogurt', 
'Unnamed: 136' : 'dairy_why_other', 
'What are some of your favorite plant-based dairy alternative products or brands?' : 'dairy_alternatives_favourites', 
'How familiar are you with plant-based alternatives for egg products? Plant-based means that the product was made without animal-sourced ingredients.' : 'eggs_alternatives_familiar', 
'What types of products or brands do you think of for plant-based egg alternatives?' : 'eggs_alternatives_brands', 
'Please indicate how likely you would be to regularly substitute each product with its plant-based alternative. Plant-based means that the product was made without animal-sourced ingredients.' : 'eggs_sub_eggs', 
'Unnamed: 141' : 'eggs_sub_liquid', 
'Unnamed: 142' : 'eggs_sub_mayo', 
'Unnamed: 143' : 'eggs_sub_dried', 
'Unnamed: 144' : 'eggs_sub_other', 
'Please explain why you already substitute or would be willing to substitute each of these products.' : 'eggs_why_eggs', 
'Unnamed: 146' : 'eggs_why_liquid', 
'Unnamed: 147' : 'eggs_why_mayo', 
'Unnamed: 148' : 'eggs_why_dried', 
'Unnamed: 149' : 'eggs_why_other', 
'What are some of your favorite plant-based egg alternative products or brands?' : 'eggs_alternatives_favourites', 
'How familiar are you with plant-based alternatives for seafood products? Plant-based means that the product was made without animal-sourced ingredients.' : 'seafood_alternatives_familiar', 
'What types of products or brands do you think of for plant-based seafood alternatives?' : 'seafood_alternatives_brands', 
'Please indicate how likely you would be to regularly substitute each product with its plant-based alternative. Plant-based means that the product was made without animal-sourced ingredients..1' : 'seafood_sub_fishfresh', 
'Unnamed: 154' : 'seafood_sub_fishcanned', 
'Unnamed: 155' : 'seafood_sub_crab', 
'Unnamed: 156' : 'seafood_sub_lobster', 
'Unnamed: 157' : 'seafood_sub_imitationcrablobster', 
'Unnamed: 158' : 'seafood_sub_shrimp', 
'Unnamed: 159' : 'seafood_sub_crayfish', 
'Unnamed: 160' : 'seafood_sub_clams', 
'Unnamed: 161' : 'seafood_sub_mussels', 
'Unnamed: 162' : 'seafood_sub_oysters', 
'Unnamed: 163' : 'seafood_sub_scallops', 
'Unnamed: 164' : 'seafood_sub_escargot', 
'Unnamed: 165' : 'seafood_sub_calamari', 
'Unnamed: 166' : 'seafood_sub_other', 
'Please explain why you already substitute or would be willing to substitute each of these products..1' : 'seafood_why_fishfresh', 
'Unnamed: 168' : 'seafood_why_fishcanned', 
'Unnamed: 169' : 'seafood_why_crab', 
'Unnamed: 170' : 'seafood_why_lobster', 
'Unnamed: 171' : 'seafood_why_imitationcrablobster', 
'Unnamed: 172' : 'seafood_why_shrimp', 
'Unnamed: 173' : 'seafood_why_crayfish', 
'Unnamed: 174' : 'seafood_why_clams', 
'Unnamed: 175' : 'seafood_why_mussels', 
'Unnamed: 176' : 'seafood_why_oysters', 
'Unnamed: 177' : 'seafood_why_scallops', 
'Unnamed: 178' : 'seafood_why_escargot', 
'Unnamed: 179' : 'seafood_why_calamari', 
'Unnamed: 180' : 'seafood_why_other', 
'What are some of your favorite plant-based seafood alternative products or brands?' : 'seafood_alternatives_favourites', 
'How familiar are you with plant-based alternatives for chicken products? Plant-based means that the product was made without animal-sourced ingredients.' : 'chicken_alternatives_familiar', 
'What types of products or brands do you think of for plant-based chicken alternatives?' : 'chicken_alternatives_brands', 
'Please indicate how likely you would be to regularly substitute each product with its plant-based alternative. Plant-based means that the product was made without animal-sourced ingredients..2' : 'chicken_sub_breast', 
'Unnamed: 185' : 'chicken_sub_thighdrumstick', 
'Unnamed: 186' : 'chicken_sub_wings', 
'Unnamed: 187' : 'chicken_sub_ground', 
'Unnamed: 188' : 'chicken_sub_roast', 
'Unnamed: 189' : 'chicken_sub_sausage', 
'Unnamed: 190' : 'chicken_sub_hotdog', 
'Unnamed: 191' : 'chicken_sub_bacon', 
'Unnamed: 192' : 'chicken_sub_deli', 
'Unnamed: 193' : 'chicken_sub_cutlet', 
'Unnamed: 194' : 'chicken_sub_nuggets', 
'Unnamed: 195' : 'chicken_sub_finger', 
'Unnamed: 196' : 'chicken_sub_canned', 
'Unnamed: 197' : 'chicken_sub_jerky', 
'Unnamed: 198' : 'chicken_sub_other', 
'Please explain why you already substitute or would be willing to substitute each of these products..2' : 'chicken_why_breast', 
'Unnamed: 200' : 'chicken_why_thighdrumstick', 
'Unnamed: 201' : 'chicken_why_wings', 
'Unnamed: 202' : 'chicken_why_ground', 
'Unnamed: 203' : 'chicken_why_roast', 
'Unnamed: 204' : 'chicken_why_sausage', 
'Unnamed: 205' : 'chicken_why_hotdog', 
'Unnamed: 206' : 'chicken_why_bacon', 
'Unnamed: 207' : 'chicken_why_deli', 
'Unnamed: 208' : 'chicken_why_cutlet', 
'Unnamed: 209' : 'chicken_why_nuggets', 
'Unnamed: 210' : 'chicken_why_finger', 
'Unnamed: 211' : 'chicken_why_canned', 
'Unnamed: 212' : 'chicken_why_jerky', 
'Unnamed: 213' : 'chicken_why_other', 
'What are some of your favorite plant-based chicken alternative products or brands?' : 'chicken_alternatives_favourites', 
'How familiar are you with plant-based alternatives for turkey products? Plant-based means that the product was made without animal-sourced ingredients.' : 'turkey_alternatives_familiar', 
'What types of products or brands do you think of for plant-based turkey alternatives?' : 'turkey_alternatives_brands', 
'Please indicate how likely you would be to regularly substitute each product with its plant-based alternative. Plant-based means that the product was made without animal-sourced ingredients..3' : 'turkey_sub_breast', 
'Unnamed: 218' : 'turkey_sub_thighdrumstick', 
'Unnamed: 219' : 'turkey_sub_wings', 
'Unnamed: 220' : 'turkey_sub_ground', 
'Unnamed: 221' : 'turkey_sub_roast', 
'Unnamed: 222' : 'turkey_sub_sausage', 
'Unnamed: 223' : 'turkey_sub_hotdog', 
'Unnamed: 224' : 'turkey_sub_bacon', 
'Unnamed: 225' : 'turkey_sub_deli', 
'Unnamed: 226' : 'turkey_sub_cutlet', 
'Unnamed: 227' : 'turkey_sub_nugget', 
'Unnamed: 228' : 'turkey_sub_finger', 
'Unnamed: 229' : 'turkey_sub_canned', 
'Unnamed: 230' : 'turkey_sub_jerky', 
'Unnamed: 231' : 'turkey_sub_organs', 
'Unnamed: 232' : 'turkey_sub_other', 
'Please explain why you already substitute or would be willing to substitute each of these products..3' : 'turkey_why_breast', 
'Unnamed: 234' : 'turkey_why_thighdrumstick', 
'Unnamed: 235' : 'turkey_why_wings', 
'Unnamed: 236' : 'turkey_why_ground', 
'Unnamed: 237' : 'turkey_why_roast', 
'Unnamed: 238' : 'turkey_why_sausage', 
'Unnamed: 239' : 'turkey_why_hotdog', 
'Unnamed: 240' : 'turkey_why_bacon', 
'Unnamed: 241' : 'turkey_why_deli', 
'Unnamed: 242' : 'turkey_why_cutlet', 
'Unnamed: 243' : 'turkey_why_nugget', 
'Unnamed: 244' : 'turkey_why_finger', 
'Unnamed: 245' : 'turkey_why_canned', 
'Unnamed: 246' : 'turkey_why_jerky', 
'Unnamed: 247' : 'turkey_why_organs', 
'Unnamed: 248' : 'turkey_why_other', 
'What are some of your favorite plant-based turkey alternative products or brands?' : 'turkey_alternatives_favourites', 
'How familiar are you with plant-based alternatives for beef products? Plant-based means that the product was made without animal-sourced ingredients.' : 'beef_alternatives_familiar', 
'What types of products or brands do you think of for plant-based beef alternatives?' : 'beef_alternatives_brands', 
'Please indicate how likely you would be to regularly substitute each product with its plant-based alternative. Plant-based means that the product was made without animal-sourced ingredients..4' : 'beef_sub_steak', 
'Unnamed: 253' : 'beef_sub_ribs', 
'Unnamed: 254' : 'beef_sub_ground', 
'Unnamed: 255' : 'beef_sub_sausage', 
'Unnamed: 256' : 'beef_sub_hotdog', 
'Unnamed: 257' : 'beef_sub_deli', 
'Unnamed: 258' : 'beef_sub_roast', 
'Unnamed: 259' : 'beef_sub_jerky', 
'Unnamed: 260' : 'beef_sub_canned', 
'Unnamed: 261' : 'beef_sub_bacon', 
'Unnamed: 262' : 'beef_sub_cured', 
'Unnamed: 263' : 'beef_sub_oragns', 
'Unnamed: 264' : 'beef_sub_shank', 
'Unnamed: 265' : 'beef_sub_other', 
'Please explain why you already substitute or would be willing to substitute each of these products..4' : 'beef_why_steak', 
'Unnamed: 267' : 'beef_why_ribs', 
'Unnamed: 268' : 'beef_why_ground', 
'Unnamed: 269' : 'beef_why_sausage', 
'Unnamed: 270' : 'beef_why_hotdog', 
'Unnamed: 271' : 'beef_why_deli', 
'Unnamed: 272' : 'beef_why_roast', 
'Unnamed: 273' : 'beef_why_jerky', 
'Unnamed: 274' : 'beef_why_canned', 
'Unnamed: 275' : 'beef_why_bacon', 
'Unnamed: 276' : 'beef_why_cured', 
'Unnamed: 277' : 'beef_why_oragns', 
'Unnamed: 278' : 'beef_why_shank', 
'Unnamed: 279' : 'beef_why_other', 
'What are some of your favorite plant-based beef alternative products or brands?' : 'beef_alternatives_favourites', 
'How familiar are you with plant-based alternatives for pork products? Plant-based means that the product was made without animal-sourced ingredients.' : 'pork_alternatives_familiar', 
'What types of products or brands do you think of for plant-based pork alternatives?' : 'pork_alternatives_brands', 
'Please indicate how likely you would be to regularly substitute each product with its plant-based alternative. Plant-based means that the product was made without animal-sourced ingredients..5' : 'pork_sub_loin', 
'Unnamed: 284' : 'pork_sub_ground', 
'Unnamed: 285' : 'pork_sub_roast', 
'Unnamed: 286' : 'pork_sub_ribs', 
'Unnamed: 287' : 'pork_sub_bacon', 
'Unnamed: 288' : 'pork_sub_sausage', 
'Unnamed: 289' : 'pork_sub_hotdog', 
'Unnamed: 290' : 'pork_sub_deli', 
'Unnamed: 291' : 'pork_sub_cured', 
'Unnamed: 292' : 'pork_sub_canned', 
'Unnamed: 293' : 'pork_sub_organs', 
'Unnamed: 294' : 'pork_sub_rinds', 
'Unnamed: 295' : 'pork_sub_ham', 
'Unnamed: 296' : 'pork_sub_jerky', 
'Unnamed: 297' : 'pork_sub_shank', 
'Unnamed: 298' : 'pork_sub_other', 
'Please explain why you already substitute or would be willing to substitute each of these products..5' : 'pork_why_loin', 
'Unnamed: 300' : 'pork_why_ground', 
'Unnamed: 301' : 'pork_why_roast', 
'Unnamed: 302' : 'pork_why_ribs', 
'Unnamed: 303' : 'pork_why_bacon', 
'Unnamed: 304' : 'pork_why_sausage', 
'Unnamed: 305' : 'pork_why_hotdog', 
'Unnamed: 306' : 'pork_why_deli', 
'Unnamed: 307' : 'pork_why_cured', 
'Unnamed: 308' : 'pork_why_canned', 
'Unnamed: 309' : 'pork_why_organs', 
'Unnamed: 310' : 'pork_why_rinds', 
'Unnamed: 311' : 'pork_why_ham', 
'Unnamed: 312' : 'pork_why_jerky', 
'Unnamed: 313' : 'pork_why_shank', 
'Unnamed: 314' : 'pork_why_other', 
'What are some of your favorite plant-based pork alternative products or brands?' : 'pork_alternatives_favourites', 
'What is your gender?' : 'gender', 
'Unnamed: 317' : 'gender_other', 
'What is your age?' : 'age', 
'Where do you live?' : 'location', 
'How do you typically describe your diet?' : 'diet', 
'Unnamed: 321' : 'diet_other', 
'What is your race/ethnicity?' : 'ethnicity', 
'What is your annual household income before taxes?' : 'income', 
'Feel free to leave any final comments below.' : 'final_comments' 
}

# rename columns
df.rename(columns=new_col_names, inplace=True)

# remove respondents who did not eat any animal products 
df = df[df['foods_eaten'] != 'None of the above']

# remove respondents if all of the demographic questions are null
demo_vars = ['gender','age','location','diet','ethnicity','income']
df = df[~df[demo_vars].isna().all(1)]

# remove vegan respondents
# there is one respondent who described their diet as vegan but then also said they eat all the animal products
# removing this person due to inconsistent results
df = df[df['diet'] != 'Vegan']

# --------------------------------------------------------------- # 
# create numerical version of df
# --------------------------------------------------------------- # 
# create copy of df to make numerical version
df_num = df.copy()

# creating subsets of column types to use later
food_cols = [
    'dairy_eats', 'eggs_eats', 'seafood_eats', 'chicken_eats', 'turkey_eats', 'beef_eats', 'pork_eats', 
    'dairy_product_butter', 'dairy_product_cream', 'dairy_product_cheesecottage', 'dairy_product_cheesecheddar', 'dairy_product_cheeseamerican', 
    'dairy_product_cheeseother', 'dairy_product_dressing', 'dairy_product_icecream', 'dairy_product_milk', 'dairy_product_sourcream', 
    'dairy_product_yogurt', 'dairy_product_other', 'eggs_product_eggs', 'eggs_product_liquid', 'eggs_product_mayo', 'eggs_product_dried', 'eggs_product_other', 
    'seafood_product_fishfresh', 'seafood_product_fishcanned', 'seafood_product_crab', 'seafood_product_lobster', 'seafood_product_imitationcrablobster', 
    'seafood_product_shrimp', 'seafood_product_crayfish', 'seafood_product_clams', 'seafood_product_mussels', 'seafood_product_oysters', 
    'seafood_product_scallops', 'seafood_product_escargot', 'seafood_product_calamari', 'seafood_product_other', 'chicken_product_breast', 
    'chicken_product_thighdrumstick', 'chicken_product_wings', 'chicken_product_ground', 'chicken_product_roast', 'chicken_product_sausage', 
    'chicken_product_hotdog', 'chicken_product_bacon', 'chicken_product_deli', 'chicken_product_cutlet', 'chicken_product_nuggets', 
    'chicken_product_finger', 'chicken_product_canned', 'chicken_product_jerky', 'chicken_product_other', 'turkey_product_breast', 
    'turkey_product_thighdrumstick', 'turkey_product_wings', 'turkey_product_ground', 'turkey_product_roast', 'turkey_product_sausage', 
    'turkey_product_hotdog', 'turkey_product_bacon', 'turkey_product_deli', 'turkey_product_cutlet', 'turkey_product_nugget', 'turkey_product_finger', 
    'turkey_product_canned', 'turkey_product_jerky', 'turkey_product_organs', 'turkey_product_other', 'beef_product_steak', 'beef_product_ribs', 
    'beef_product_ground', 'beef_product_sausage', 'beef_product_hotdog', 'beef_product_deli', 'beef_product_roast', 'beef_product_jerky', 'beef_product_canned', 
    'beef_product_bacon', 'beef_product_cured', 'beef_product_oragns', 'beef_product_shank', 'beef_product_other', 'pork_product_loin', 'pork_product_ground', 
    'pork_product_roast', 'pork_product_ribs', 'pork_product_bacon', 'pork_product_sausage', 'pork_product_hotdog', 'pork_product_deli', 'pork_product_cured', 
    'pork_product_canned', 'pork_product_organs', 'pork_product_rinds', 'pork_product_ham', 'pork_product_jerky', 'pork_product_shank', 'pork_product_other'
    ]
eats_cols = [
    'dairy_eats', 'eggs_eats', 'seafood_eats', 'chicken_eats', 'turkey_eats', 'beef_eats', 'pork_eats'
    ]
familiar_cols = [col for col in df if col.endswith('familiar')]
sub_cols = [col for col in df.columns if 'sub' in col]

# create binary version of food_cols
# first convert nans to 0s 
df_num[food_cols] = df_num[food_cols].fillna(0)
# convert these columns to binary
for x in food_cols:
    df_num[x] = df_num[x].astype('category').cat.codes

#convert 0's back to nans for these cols, so it's easier to work with them in tableau
food_cols_nans = [x for x in food_cols if not x in eats_cols or eats_cols.remove(x)]
df_num[food_cols_nans] = df_num[food_cols_nans].replace(0, np.nan)

# convert familiar_cols to factors then numeric
familiar_scale = {'Not at all familiar': 1, 'Slightly familiar': 2,
            'Somewhat familiar': 3, 'Moderately familiar': 4, 'Extremely familiar': 5}
df_num[familiar_cols] = df_num[familiar_cols].replace(familiar_scale)

# convert sub_cols to factors then numeric
sub_scale = {'Definitely would not' : -3,
             'Very unlikely' : -2,
             'Unlikely' : -1,
             'Neutral' : 0,
             'Likely' : 1,
             'Very likely' : 2, 
             'Already substitute' : 3 }
df_num[sub_cols] = df_num[sub_cols].replace(sub_scale)

# --------------------------------------------------------------- # 
# create long version of df
# --------------------------------------------------------------- #
df_num_long = df_num.melt(id_vars='respondent_id')
df_num_long_merged = df_num_long.merge(long_colnames, on='variable')
df_num_long_merged.drop('variable', axis=1, inplace=True)

# --------------------------------------------------------------- # 
# create processed/unprocessed variable 
# --------------------------------------------------------------- #
# processed = 1, unprocessed = 0
processed = [
    'ground', 'sausage', 'hotdog', 'bacon', 'deli', 'jerky', 'canned', 'cutlet', 'nuggets',
    'cured','fingers', 'liquid_eggs','mayo','dried_eggs', 'hams', 'butter', 'cream', 
    'cheese_cottage', 'cheese_cheddar','cheese_american', 'cheese_other', 'dressing', 
    'ice_cream', 'milk','sour_cream', 'yogurt', 'fish_canned', 'imitation_crab']
unprocessed = [
    'roast', 'organs', 'thigh_drumstick', 'wings','breast','ribs','shank','steaks','loin', 'eggs',
    'fish_fresh', 'crab', 'lobster', 'shrimp', 'crayfish', 'clams', 'mussels', 'oysters', 
    'scallops', 'escargot', 'calamari']
df_num_long_merged['processed']= np.nan
df_num_long_merged.loc[df_num_long_merged.animal_sub_product.isin(processed),'processed']= 1
df_num_long_merged.loc[df_num_long_merged.animal_sub_product.isin(unprocessed),'processed']= 0

# --------------------------------------------------------------- # 
# save data
# --------------------------------------------------------------- #
# this df is imported to tableau for visualizing
df_num_long_merged.to_csv('To share/w-to-sub-cleaned-data-numerical-long-to-share.csv',index=False)
