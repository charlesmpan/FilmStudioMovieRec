# An Introspective Into Yielding the Highest ROI on Your First Movie

Featuring:
Abdulrahman Amer

E-Mail: abdulrahman@freeyoursoundinstitute.com

LinkedIn: https://www.linkedin.com/in/abdulrahman-amer-090557171/

GitHub: https://github.com/AbdulrahmanAmer-R



Benjamin Bai

E-Mail: benjaminybai@gmail.com

LinkedIn: https://www.linkedin.com/in/benjamin-y-bai

GitHub: https://github.com/benjaminybai



Charles Pan

E-Mail:     charlesmpan@gmail.com

LinkedIn: https://www.linkedin.com/in/charles-pan-/

GitHub:    https://github.com/charlesmpan



Kevin Rivera

E-Mail: riverakevin2009@gmail.com

LinkedIn: https://www.linkedin.com/in/kevin-rivera-kr06/

GitHub: https://github.com/icodepie




# Objective

Our group has been tasked to assist Microsoft in venturing into the Movie Industry. Our goal was first to analyze the different types of data from reliable credible sources such as The Numbers and IMDB  to have a better understanding of the industries; and to provide our findings to Microsoft executives on what we deem the most effective and profitable way to do so. We looked into films released since 2010 with larger production budgets than $2 million and have analyzed the most profitable months for movies as well as the most lucrative Genre to target in terms of profitability. We have also recommended three directors, actors, and actresses based on their participation in horror movies as well as the trajectory of those horror movies in terms of ratings over years. With our suggestions from the following report, we believe that Microsoft will have success by following the recommendation of producing a horror movie around July, with whoever casting they can contract.  


# Business Problem

Microsoft has decided to create a new movie studio but has no insight into the industry. With an already developed industry full of strong competitors, Microsoft has tasked us to find the best entry point to join the market and stand on equal grounds with the current industry players. To begin, we have decided that the best way to tackle the problem at hand is to analyze the different sorts of data such as net income, movie rating, release date, movie casting, and genres from reliable databases. We have chosen to look at data from the past 10 years to have an understanding of current trends as well as potential growth. As a result of our research, we have concluded that the main three factors that we should target to compile a larger picture would be.

    1) Movie Genre's Return on Investment: What are the most profitable genre groups in terms of percentages?
    
    2) Release Date: What is the most profitable month to release a movie?
    
    3) Casting Choices: What are the current trending or well-performing actors, actresses, and directors in the current industry?
    
    
# Data

We utilized three different data sources to conduct our research to have a better understanding of the industry.
    1) IMDB: One of the largest online databases for information regarding films, television series, and movies; generally used by the common populace for looking into shows or movies. The data we chose to utilize was the list of talent, such as actors, actresses, and directors and the movies they were associated with, movie names, genre, runtime, and rating. The data helped us analyze the performance of actors, actresses, and directors with the movies they participated in.
    
    2) The Numbers (TN): A premier provider of movie industry data and research services. They are primarily used by major financial institutions, media companies, investors, and data analysis companies. The data we chose to utilize were mostly the financial data such as production budget, worldwide gross, and release dates. The data helped us analyze the most profitable months as well as the most profitable genres.

# Methods

We imported the data from the sources above and went through all the data sources provided; through that, we dropped a lot of databases such as what movies talents were known for and what regions and languages movies were provided in. There was a lot of cleaning and dropping off more columns, removal of incomplete data, and duplicate data. We merged several databases to piece together an aggregate dataset with information that could correlate with each other. We sorted, filtered, and calculated new data within the aggregate data, to determine trends and correlations which we then visualized into several charts such as bar charts and line charts to assist in delivering our recommendations.
    
The repository includes the analysis of crucial data that supports our insights. You will see that we utilized Pandas and SQL as well as methods of cleaning and organizing the data in a way that allowed us to create insightful visualizations. This includes the calculation of ROI by analyzing numerous columns in different datasets for the genre as well as the release month. 


# Results

![GitHub Logo](/viz_images/ROI_combo_by_month.png)

The above demonstrates that movies with a July release date tend to yield a higher return on investment. Both the mean and the median for that month are well above the other months, thus showing the most profitable and least risk-adverse month to release in.

![GitHub Logo](/viz_images/roi_percent_visualization.png)

The above demonstrates the different genres' percentage return on investment. 

![GitHub Logo](/viz_images/directorsrelationtohorror.png)

The following data presents the top ten directors in terms of their average movie rating specific to the Horror genre on the X axis and the correlation of their movie rating to the last 10 years. With the data above, we chose three directors who stood out with a focus on correlation while also having decent movie ratings. Please note that the average rating for the horror movie is around 5.5, thus these directors were performing well above the average.

![GitHub Logo](/viz_images/director_rating.png)

The following data presents our three director candidate and their overall active movie ratings over the last ten years. The candidates we chose were Alper Mestci, James Wan, and Mike Flanagan.

![GitHub Logo](/viz_images/actors_rating.png)

The following data presents the top ten actors in terms of their average movie rating specific to the Horror genre on the X axis and the correlation of their movie rating to the last 10 years. With the data above, we chose three actors who stood out with a focus on correlation while also having decent movie ratings.

![GitHub Logo](/viz_images/actorsrelationtohorror.png)

The following data presents our three actor candidate and their overall active movie ratings over last ten years. The candidates we chose were Logan Miller, Patrick Wilson, and Joe Swanberg.

![GitHub Logo](/viz_images/actress_rating.png)

The following data presents the top ten actresses in terms of their average movie rating specific to the Horror genre on the X axis and the correlation of their movie rating to the last 10 years. With the data above, we chose three actresses who stood out with a focus on correlation while also decent average movie ratings.

![GitHub Logo](/viz_images/actressrelationtohorror_rating.png)

The following data presents our three actor candidate and their overall active movie ratings over last ten years. The candidates we chose were Amy Seimetz, Kate Bosworth, and Danielle Harris.

The results of over complete analysis are the following:
    Our recommendation if Microsoft wanted to step into the movie industry would be to release a horror movie genre around July. The directors we recommend would be Mike Flanagan, James Wan, or Alper Mestci. The three actors that we would recommend would be Logan Miller, Patrick Wilson, and Joe Swanberg. The actresses we recommend would be Amy Seimetz, Kate Bosworth, and Danielle Harris. We believe that casting is very important as profitability isn't the only goal in mind, but it is also crucial to build brand name recognition.  


# Questions?


If you have any questions you can message any of the members from any of the provided contacts above.


# Wanting to contribute?


If you are interested in contributing to our study:


1. Fork this repository

2. Clone your forked repository

3. Add your scripts

4. Commit and push

5. Create a pull request

6. Star this repository

7. Wait for pull request to merge

8. Allow us to review your contribution 

Repository Structure

├── README.md                        <- The README for reviewers of this project

├── Movie_Analysis_ProjectP6.ipynb   <- Documentation of the analysis process in Jupyter notebook

├── presentations.pdf                <- The presentation in PDF

├── zippedData                       <- Both sourced externally and generated from code

└── viz_images                       <- Storage for all images used
