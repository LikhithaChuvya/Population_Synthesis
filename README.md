# Population_Synthesis
The objective of a population synthesizer is to generate household weights which satisfies the marginal control distributions. This is achieved by use of a data fitting technique. The most common fitting technique used by various population synthesizers is the Iterative Proportional Fitting (IPF) procedure.

Dataset:  https://drive.google.com/file/d/11GedB2pRmIpjMihPQfQhtroezpahFRB4/view?usp=sharing


Dataset contains a sample of 200 individuals, each characterized by three attributes: sex, age group,
and highest education level. The categories for each variable are outlined in Table 1.

# Table 1. 

Description of categories in variables
Variable Category Description
Sex 
1 Male
2 Female
Age_group
1 Below 22 years
2 22-60 years
3 Above 60 years

Highest_education_level
0 No formaleducation
1 Primary education
2 Secondary education
3 Graduation and above

The above sample is representative of a region whose population characteristics for the three
attributes are provided in Table 2. The table provides total number of individuals (frequencies) in
different categories of each of the three variables.

# Table 2: 

Population characteristics
Variable Description Frequency
Sex
Male 25324
Female 24676
Age_group 
Below 22 years 17955
22-60 years 29642
Above 60 years 2403
Highest_education_level 
No_formal education 7490
Primary education 5655
Secondary education 24400
Graduation and above 12455

Using the above seed sample dataset and synthesizing a population of 50,000 agents such that the generated population matches the actual population characteristics (from Table 2).
