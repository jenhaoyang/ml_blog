###### tags: `機器學習` `醫療AI` `課程`

# 醫療AI課W2

----

# Sensitivity, Specificity, and Evaluation Metrics

----

## 用Accuracy計算準確率的盲點

----
一般來說計算準確率我們會用以下公式
![](https://i.imgur.com/iYYYVpu.png)

----

假設一個只會輸出Normal的模型，用剛剛的公式計算出來準確率是0.8
![](https://i.imgur.com/p6nVJ6Y.png)

----

而令一個模型有正確預測出兩個異常樣本但是也預測錯兩個正常樣本，用準確率來看也是0.8, 但實際上有正確去預測異常樣本的模型是比較好的, 因此單純用準確率去判斷模型好會壞有問題
![](https://i.imgur.com/IdfmQiE.png)

----

## 用機率的概念看Accuracy
![](https://i.imgur.com/ATNwGU5.png)

----

由Accuracy的機率可以沿伸出兩個概念，Sensitivity, Specificity
![](https://i.imgur.com/SVhtTNw.png)

----

Seneitivity代表一個有疾病的病人模型正確判斷出有疾病的機率
Specificity代表一個正常的人模型正確判斷為正常的機率
![](https://i.imgur.com/piK4ewe.png)

----

![](https://i.imgur.com/dWwRBkG.png)

----

經過推導後我們了解到Seneitivity, Specificity, Prevalence之間的關係
![](https://i.imgur.com/bS34AyS.png)

----

# PPV, NPV
在實際應用上，我們可能會在意下面兩個指標
PPV： 模型判斷一個人有疾病的狀態下,這個人真的有疾病的機率是多少
NPV： 模型判斷一個人正常的情況下, 這個人為正常的機率為多少
![](https://i.imgur.com/rMBSQlE.png)

----
