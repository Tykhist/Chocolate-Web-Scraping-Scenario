import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Add context for each code block!!!!
# Print comments were for checking my work

web_info = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(web_info.content, 'html.parser')
#print(soup)

rating_tags = soup.find_all(attrs={"class": "Rating"})
ratings = []
for i in range(1, len(rating_tags)):
  temp1 = rating_tags[i].get_text()
  ratings.append(float(temp1))
#print(ratings)

rating_plot = plt.hist(ratings)
plt.show(rating_plot)

company_tags = soup.find_all(attrs={"class": "Company"})
companies = []
for i in range(1, len(company_tags)):
  temp2 = company_tags[i].get_text()
  companies.append(temp2)
#print(companies)

cpercent_tags = soup.find_all(attrs={"class": "CocoaPercent"})
cpercent = []
for i in range(1, len(cpercent_tags)):
  temp3 = cpercent_tags[i].get_text().strip('%')
  cpercent.append(float(temp3))
#print(cpercent)

df = pd.DataFrame({'Company': companies, 'Rating': ratings, 'CocoaPercentage': cpercent})
#print(df)

comp_group = df.groupby('Company').Rating.mean()
top_ten = comp_group.nlargest(10)
#print(top_ten)

plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
plt.clf()
