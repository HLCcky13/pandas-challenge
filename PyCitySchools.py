#!/usr/bin/env python
# coding: utf-8

# In[99]:


# Dependencies and Setup
import pandas as pd


# In[100]:


# File to Load (Remember to Change These)
school_data_to_load = "C:/Users/Hannah/Downloads/pandas-challenge/Starter_Code/Starter_Code/PyCitySchools/Resources/schools_complete.csv"
student_data_to_load = "C:/Users/Hannah/Downloads/pandas-challenge/Starter_Code/Starter_Code/PyCitySchools/Resources/students_complete.csv"


# In[101]:


# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


# In[102]:


# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[103]:


# Calculate the total number of unique schools
school_count =  len(school_data_complete["school_name"].unique())
school_count


# In[104]:


# Calculate the total number of students
student_count = len(school_data_complete["student_name"])
student_count


# In[105]:


# Calculate the total budget
total_budget = school_data["budget"].sum()
total_budget


# In[106]:


# Calculate the average math score
average_math_score = school_data_complete["math_score"].mean()
average_math_score


# In[107]:


# Calculate the average reading score
average_reading_score = school_data_complete["reading_score"].mean()
average_reading_score


# In[108]:


# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_math_percentage


# In[109]:


# Calculate the percentage of students who passeed reading (hint: look at how the math percentage was calculated)  
passing_reading_count = school_data_complete[(school_data_complete["reading_score"] >= 70)].count()["student_name"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100
passing_reading_percentage


# In[110]:


# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[
    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
overall_passing_rate


# In[111]:


# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = pd.DataFrame({"School Type": [school_count],
                              "Total Students": [student_count],
                              "Total Budget": [total_budget],
                              "Average Math Score": [average_math_score],
                              "Average Reading Score": [average_reading_score],
                              "% Passing Math": [passing_math_percentage],
                              "% Passing Reading": [passing_reading_percentage],
                              "% Overall Passing Rate": [overall_passing_rate]})

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
district_summary


# In[112]:


# Use the code provided to select the school type
school_types = school_data.set_index(["school_name"])["type"]
school_types


# In[113]:


# Calculate the total student count
per_school_counts = school_data_complete["school_name"].value_counts()
per_school_counts


# In[114]:


# Calculate the total school budget and per capita spending
per_school_budget = school_data_complete.groupby(["school_name"]).mean()["budget"]
per_school_capita = per_school_budget / per_school_counts
per_school_budget


# In[115]:


per_school_capita


# In[116]:


#Calculate per student budget
per_student_budget = per_school_budget/per_school_counts
per_student_budget


# In[117]:


# Calculate the average test scores
per_school_math = school_data_complete.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete.groupby(["school_name"]).mean()["reading_score"]
per_school_math


# In[118]:


per_school_reading


# In[119]:


# Calculate the number of schools with math scores of 70 or higher
school_passing_math = school_data_complete[(school_data_complete["math_score"] >= 70)]
school_passing_math.head()


# In[120]:


# Calculate the number of schools with reading scores of 70 or higher
school_passing_reading = school_data_complete[(school_data_complete["reading_score"] >=70)]
school_passing_reading.head()


# In[121]:


# Use the provided code to calculate the schools that passed both math and reading with scores of 70 or higher
passing_math_and_reading = school_data_complete[
    (school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)]
passing_math_and_reading.head()


# In[122]:


# Use the provided code to calculate the passing rates
per_school_passing_math = school_passing_math.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
per_school_passing_reading = school_passing_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
overall_passing_rate = passing_math_and_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100


# In[123]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = pd.DataFrame({"School Type": school_types,
                              "Total Students": per_school_counts,
                              "Total School Budget": per_school_budget,
                              "Per Student Budget": per_student_budget,
                              "Average Math Score": per_school_math,
                              "Average Reading Score": per_school_reading,
                              "% Passing Math": per_school_passing_math,
                              "% Passing Reading": per_school_passing_reading,
                              "% Overall Passing Rate": overall_passing_rate})

# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
per_school_summary


# In[124]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
top_schools = per_school_summary.sort_values(["% Overall Passing Rate"], ascending = False)
top_schools.head()


# In[125]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
top_schools = per_school_summary.sort_values(["% Overall Passing Rate"], ascending = True)
top_schools.head()


# In[126]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]


# In[127]:


# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]


# In[128]:


# Use the code to select only the `math_score`.
ninth_grade_math_scores = ninth_graders_scores["math_score"]
tenth_grader_math_scores = tenth_graders_scores["math_score"]
eleventh_grader_math_scores = eleventh_graders_scores["math_score"]
twelfth_grader_math_scores = twelfth_graders_scores["math_score"]


# In[130]:


# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = pd.DataFrame({"9th": ninth_grade_scores,
                                    "10th": tenth_grade_scores,
                                    "11th": eleventh_grade_scores,
                                    "12th": twelfth_grade_scores})
math_scores_by_grade.head()


# In[131]:


# Minor data wrangling
math_scores_by_grade.index.name = None


# In[132]:


# Display the DataFrame
math_scores_by_grade


# In[133]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]


# In[135]:


# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]


# In[136]:


# Use the code to select only the `reading_score`.
ninth_grade_reading_scores = ninth_graders_scores["reading_score"]
tenth_grader_reading_scores = tenth_graders_scores["reading_score"]
eleventh_grader_reading_scores = eleventh_graders_scores.mean()["reading_score"]
twelfth_grader_reading_scores = twelfth_graders_scores["reading_score"]


# In[137]:


# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame({"9th": ninth_grade_scores,
                                    "10th": tenth_grade_scores,
                                    "11th": eleventh_grade_scores,
                                    "12th": twelfth_grade_scores})


# In[138]:


# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None


# In[139]:


# Display the DataFrame
reading_scores_by_grade


# In[140]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[141]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()


# In[143]:


# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels = labels)


# In[145]:


#  Calculate averages for the desired columns. 
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing Rate"]


# In[146]:


# Assemble into DataFrame
spending_summary = pd.DataFrame({"Average Math Score": spending_math_scores,
                                 "Average Reading Score": spending_reading_scores,
                                 "% Passing Math": spending_passing_math,
                                 "% Passing Reading": spending_passing_reading,
                                 "% Overall Passing Rate": overall_passing_rate})


# In[147]:


# Display results
spending_summary


# In[148]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[150]:


# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], size_bins, labels = labels)


# In[152]:


# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"]).mean()["Average Math Score"]
size_reading_scores = per_school_summary.groupby(["School Size"]).mean()["Average Reading Score"]
size_passing_math = per_school_summary.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary.groupby(["School Size"]).mean()["% Overall Passing Rate"]


# In[153]:


# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = pd.DataFrame({"Average Math Score": size_math_scores,
                             "Average Reading Score": size_reading_scores,
                             "% Passing Math": size_passing_math,
                             "% Passing Reading": size_passing_reading,
                             "% Overall Passing Rate": overall_passing_rate})


# In[154]:


# Display results
size_summary


# In[155]:


# Group the per_school_summary DataFrame by "School Type" and average the results.
type_math_scores = per_school_summary.groupby(["School Type"]).mean()["Average Math Score"]
type_reading_scores = per_school_summary.groupby(["School Type"]).mean()["Average Reading Score"]
type_passing_math = per_school_summary.groupby(["School Type"]).mean()["% Passing Math"]
type_passing_reading = per_school_summary.groupby(["School Type"]).mean()["% Passing Reading"]
overall_passing_rate = (type_passing_math + type_passing_reading)/2


# In[157]:


# Use the code provided to select new column data
average_math_score_by_type = type_math_scores["Average Math Score"]
average_reading_score_by_type = type_reading_scores["Average Reading Score"]
average_percent_passing_math_by_type = type_passing_math["% Passing Math"]
average_percent_passing_reading_by_type = type_passing_reading["% Passing Reading"]
average_percent_overall_passing_by_type = type_overall_passing["% Overall Passing"]


# In[160]:


# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame({"Average Math Score": type_math_scores,
                             "Average Reading Score": type_reading_scores,
                             "% Passing Math": type_passing_math,
                             "% Passing Reading": type_passing_reading,
                             "% Overall Passing Rate": overall_passing_rate})


# In[161]:


# Display results
type_summary


# In[ ]:




