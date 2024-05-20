import pandas as pd
import matplotlib.pyplot as plt
hr_data = pd.read_csv('Attrition data.csv')
# Create a bar chart for attrition rate
attrition_rate = hr_data['Attrition'].value_counts(normalize=True) * 100
attrition_rate.plot(kind='bar', color=['green', 'red'])
plt.title('Attrition Rate')
plt.xlabel('Attrition')
plt.ylabel('Percentage')
plt.show()