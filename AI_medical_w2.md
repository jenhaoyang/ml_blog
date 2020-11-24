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

![](https://i.imgur.com/wesX7Qs.png)

----

![](https://i.imgur.com/kO7PXC5.png)

----

## Confusion matrix
利用Confusion matrix我們可以尋找PPV, NPV, 和Seneitivity,Specificity
![](https://i.imgur.com/RGjIMLM.png)

-----

![](https://i.imgur.com/HoUjVWB.png)

----

## ROC curve
讓我們可以視覺化的畫出再不同threhole下sensitivity對specificity的圖形

![](https://i.imgur.com/0ujYTJy.png)

----

threhole 會影響sensitivity, specificity  
如果threshold為0則,則全部判斷的結果都是positive,因此sensitivity=1  
反之threshold為1則,則全部判斷為normal, 因此specificity=1  
![](https://i.imgur.com/bvAmJCt.png)

----

![](https://i.imgur.com/egtMOYa.png)

----

![](https://i.imgur.com/xvnS700.png)

----

![](https://i.imgur.com/D71ExHJ.png)

----

## 模型預測的信心驅煎
假如我們想知道模型在一間醫院的預測準確度，一種方法是醫院全部的人都用模型進行預測並且計算出準確率,我們稱為 population accuracy, 以p表示
![](https://i.imgur.com/Uo2AO3y.png)

----

但是實際上我們不可能真的去預測每一個人，那在有限樣本中得到的準確率和全體樣本的準確率的關係是我們想要知道的
![](https://i.imgur.com/Ajtlkh5.png)

----

![](https://i.imgur.com/JlrFi3T.png)

----

95信心區間例子  
例如我們從醫院取得多次不同的資料集, 每份樣本都會得到不同的準確率,因此95%信心區間的範圍也都不一樣
![](https://i.imgur.com/AmuQkKa.png)

----

將得到的信心區間畫成圖，我們可以看到95%的信心區間確實有包含到p（0.78），而這就是95%信心區間真正的意義
![](https://i.imgur.com/RP1fA9n.png)

----

影響信心區間的因子有樣本數量, 樣本數量愈大信心區間的範圍會愈小, 因為愈多樣本會愈準確
![](https://i.imgur.com/nu3WMTA.png)

----






