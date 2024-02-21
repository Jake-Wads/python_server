import numpy as np
import math

df1 = pd.DataFrame({'hours_studied': np.random.normal(7, 2, 20), 'study_strategy': 'flashcards'})
df2 = pd.DataFrame({'hours_studied': np.random.normal(4, 2, 20), 'study_strategy': 'NA'})

df = pd.concat([df1, df2])
df['handedness'] = np.random.choice(['left', 'right'], 40)
df = df.sample(40)

df['exam_score'] = df.hours_studied * 10 + np.random.normal(0, 15, 40)
df.exam_score = np.where(df.exam_score < 0, 0, df.exam_score)

df['coffee_consumed'] = math.floor((df.exam_score / 10).max()) - (df.exam_score / 10).apply(math.floor)
df['hours_slept'] = 11 - df.coffee_consumed
df = df[['exam_score', 'hours_studied', 'study_strategy', 'handedness', 'coffee_consumed', 'hours_slept']]

print(df.groupby('handedness').mean())
print(df.groupby('study_strategy').mean())
print('\nr = ', df.corr().iloc[1, 0])

df.plot.scatter('hours_studied', 'exam_score')