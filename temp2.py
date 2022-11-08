# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_classification
# df = np.genfromtxt(r"D:\02_Downloads\house-prices-advanced-regression-techniques\test.csv",delimiter=",")
# print(df.shape)
# print(df)

# # X = [[0, 1],
# #      [0, 2],
# #      [0, 3],
# #      [0, 4],
# #      [0, 5],
# #      [99, 1],
# #      [99, 2],
# #      [99, 3],
# #      [99, 4],
# #      [99, 5]]

# # y = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# # X = np.array(X)
# # y = np.array(y)
# # print("X.shape:", X.shape)
# # print("y.shape:", y.shape)

# # clf = RandomForestClassifier(max_depth=2, random_state=0)
# # clf.fit(X, y)

# # print(clf)
# # print(clf.predict([X[0]]))



import os
os.chdir(r"D:\04_File\16_Degrer_YR4_Sem1\02_CISC3024_Pattern Recognition\02_07_FinalProject\Satellite-Image-Classification\train\water")
i = 1
for x in os.listdir():
	os.rename(x, f"water{i}.jpg")
	i+=1