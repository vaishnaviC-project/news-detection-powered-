import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load CSV file
df = pd.read_csv('test.csv')
print(df.head())
# Convert columns to numeric (if needed), coerce errors
df['True'] = pd.to_numeric(df['True'], errors='coerce')
df['False'] = pd.to_numeric(df['False'], errors='coerce')
# Drop rows with missing values in these columns
df = df.dropna(subset=['True', 'False'])
# Calculate margin
df['Margin'] = df['True'] - df['False']
# Set plot style
sns.set(style="whitegrid")
# Create subplots
fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle('Visualizations of Truthfulness Data', fontsize=20)
# 1. Line Plot
axes[0, 0].plot(df['True'].reset_index(drop=True), label='True', color='green')
axes[0, 0].plot(df['False'].reset_index(drop=True), label='False', color='red')
axes[0, 0].set_title('Line Plot of True vs False Scores')
axes[0, 0].legend()
# 2. Box Plot
sns.boxplot(data=df[['True', 'False']], ax=axes[0, 1])
axes[0, 1].set_title('Box Plot of True and False Scores')


# 3. Heatmap
sns.heatmap(df[['True', 'False']].corr(), annot=True, cmap='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Heatmap of Correlation')

# 4. Margin Plot
sns.histplot(df['Margin'], kde=True, ax=axes[1, 1], color='purple')
axes[1, 1].set_title('Histogram and KDE of Margin (True - False)')

# 5. KDE Plot
sns.kdeplot(x=df['True'], fill=True, label='True', ax=axes[2, 0], color='green')
sns.kdeplot(x=df['False'], fill=True, label='False', ax=axes[2, 0], color='red')
axes[2, 0].set_title('KDE Plot of True and False Scores'

axes[2, 0].legend()

# Hide unused subplot
axes[2, 1].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()