# 醫療AI課

---

# 醫療AI的挑戰
![](https://i.imgur.com/Uv9IrfM.png)

----

# Class Imbalance
資料集樣本的分佈十分不均, 有疾病的樣本比正常的樣本少很多。由於大量正常樣本充斥於資料集中，這讓AI模型訓練效果很差。

----

## Imbalance使訓練變差的原因
![](https://i.imgur.com/StdYp87.png)

----

經過一次計算後，正常樣本貢獻的lost比疾病樣本貢獻的lost多出很多,因此模型被加強分辨正常樣本的能力,而不是疾病樣本

![](https://i.imgur.com/8wHRGBV.png)

----

## 方法1：加上權重
解決方法可以在lost function前面多加一個權重，而權重是該樣本的數量佔全部樣本數的比例
![](https://i.imgur.com/2VkDJ4x.png)

----

![](https://i.imgur.com/eYxzcyN.png)

----

![](https://i.imgur.com/HpPFpaM.png)

----

## 方法2：Resample
另一個方法是Resample,拿取部份比較多的樣本以及重複比較少的樣本
![](https://i.imgur.com/CuTqqQg.png)

----

# Multi-Task 一次識別多種症狀
對於每一個症狀我們都可以訓練一個模型來辨識，不過也可以訓練一個模型來辨識所有症狀
![](https://i.imgur.com/WvIA3dL.png)

----

![](https://i.imgur.com/ENDWrL0.png)

----

![](https://i.imgur.com/9O1zLTN.png)

----

# DataSet Size
捲積神經網路可以用於2D影像，也可以用於心電圖或是3D影像
![](https://i.imgur.com/H472BGE.png)

----

常用捲積神經網路如下，通常會嘗試使用下列網路並且挑出表現最好的
![](https://i.imgur.com/NX7r6r0.png)

----

這些模型都需要大量訓練資料才能訓練出好模型，可是醫療資料不像一般資料那麼大量，所以需要一些方法來解決這個挑戰
![](https://i.imgur.com/xORMFrO.png)

----

## 解法一：使用預訓練模型
我們可以用辨識其他物件（如貓,狗...）的預訓練模型，並且複製他的learning feature，來訓練我們的醫療模型
![](https://i.imgur.com/5cOesxh.png)

----

這個作法的概念在於訓練其他物件的模型和肺部X光片有一些共同的基礎feature,例如辨識邊緣的feature,如此一來我們就不用重新訓練這些基礎feature  
拿辨識其他物件的feature作為初始feature並訓練我們稱為fine-tuning
![](https://i.imgur.com/JKScL6c.png)

----

例如辨識企鵝的模型有一些General feature是用來尋找邊的，這些可以用在我們肺部x光模型，而後面的High level feature可能是用來尋找企鵝的頭，對我們來說並沒有用
![](https://i.imgur.com/cCIqjFm.png)

----

如此一來我們不必重頭訓練general feature,我們只需訓練High level feature,因而我們可以用較小的資料集來完成訓練
![](https://i.imgur.com/17rMm1i.png)

----

## 使用 Data Argumentation
我們可以藉由縮放,旋轉,或是調整對比度來增加資料量。這種方法稱為Data Argumentation

![](https://i.imgur.com/O1HMFrA.png)

----

使用 Data Argumentation我們有兩點要考量
* 第1點：轉換後的結果再真實世界中是否可能出現
Data Argumentation是為了讓模型更加通用化，所以轉換後的結果也必須是真實世界中可能出現的狀況，例如調整對比度就是可能的狀況. 
![](https://i.imgur.com/QQMGOez.png)



----
* 第2點：轉換後會不會讓label改變
將照片鏡射後,心臟的位置從左跑到右,如此一來照片的label改變(變成Dextrocardia),所以我們不應該選擇這種情況
![](https://i.imgur.com/6k2dZer.png)


----
Data Argumentation範例
![](https://i.imgur.com/NgfmZ6W.png)

----

# 確認模型判斷能力

----

## 使用training, validation, test 測試集
training set用於建立模型以及"選擇模型", test set用來產生最終報告和結果
![](https://i.imgur.com/7820R9L.png)

----

實際應用上我們會分成三組data set, training set用來建立model, validation set用來調整超參數以及模型的選擇, test set用來產生最終報告
![](https://i.imgur.com/Vwx0dwj.png)

----

![](https://i.imgur.com/vdRfj7p.png)

----

![Uploading file..._gg0b4l7m5]()

----

大家稱呼這些資料集的方式可能不一樣,不過我們維持稱呼他們為training set, validation set test set
![](https://i.imgur.com/V1yDH3Z.png)

----

建立這3個資料集也有3個挑戰
* Patient Overlap
* Set Sampling
* Ground Truth
![](https://i.imgur.com/VNYc9Tw.png)

----
例如有一個病人再不同時間拍攝x光兩次，這兩次都有戴項鍊
![](https://i.imgur.com/vrEyWM0.png)

----

如果這兩張照片分別規類到training set 和 test set, 我們的模型很有可能因為看到"相同的項鍊"而做出判斷
![](https://i.imgur.com/EOW0PnN.png)

----

要避免這個問題,我們要確保同一個病人不會出現在不同資料集
![](https://i.imgur.com/khWBoHM.png)

----

我們可以藉由使用病人名稱來做分類,而不是用照片來做分類
![](https://i.imgur.com/ukBO9dc.png)

----
## set sampling
test set 通常佔資料集的10%, 有時候test set會給人類專家做標註以便比較機器和人的表現. 而通常test set 適當的數量大約是百份,(如圖所示CT：120, 400-500XRays, 130 Whole Slides)

![](https://i.imgur.com/9azECJO.png)

----
我們的挑戰在於, 有疾病的樣本數本身就很少, 我們不希望某些種類的疾病完全沒有出現在test set, 因為這樣就沒辦法準確判斷機器對於這類疾病的分類能力. 通常我們希望每種類型的疾病的出現機率都是50%

![](https://i.imgur.com/UnzqOyW.png)

----

對於validation set,我們會希望他的資料分佈和test set是一樣的,也就是說跟test set一樣每個類型的疾病的異常出現機率都為50%，所以在建立資料集的時候, 先建立test set, 再來validation set, 最後training set
![](https://i.imgur.com/EUrHw4r.png)

----

## 決定Ground Truth（或是reference standard）
![](https://i.imgur.com/d9NcKZh.png)

----

在決定ground truth的時候常常會遇到專家意見不同，這稱為inter-observer disagreement
![](https://i.imgur.com/6FKQqYD.png)

----

我們可以藉由投票表決或是套論的方式決定ground truth
![](https://i.imgur.com/h869E1N.png)

----

令一種方法就是再多加一個檢驗方式來確認ground truth, 例如x光多加CT掃描, 皮膚癌多加皮膚採樣

![](https://i.imgur.com/8qfmCgP.png)

----

![](https://i.imgur.com/80EGLMI.jpg)

----



