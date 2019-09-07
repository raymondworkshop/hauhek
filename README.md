#### hauhek - One Cantonese word segmentation, which has higher accuracy and faster than [jieba](https://github.com/fxsjy/jieba) for Cantonese

Usage:  
> python hauhek.py query="呢幾日天氣成日變，你要小心保重身體。"   
>    
> {       
> 'query': 'query=呢幾日天氣成日變，你要小心保重身體。',    
> 'output': 'query-=-呢-幾日-天氣-成日-變-，-你-要-小心-保重-身體-。'  
> }  
   
For example:       
query:   
>  '日前Amazon正式宣佈Kindle app 和電子書都加入繁體中文的支援，更開設了共有 20,000 本書籍的繁體中文電子書的專區，各大經典之作亦收錄其中。閱讀電子化方便了不少書生，即使出外想攜帶書本看看，也不怕厚重，而且一個程式更可收錄多本書籍，簡單方便。正所謂書中自有黃金屋，閱讀既可以增進知識，令人建立獨特的思維和見解，更可讓人放鬆心情。愛書的人家裡分分鐘可能擁有過百本書籍，但到最後一本本書脊泛黃滿佈塵埃，亦不知它們該何去何從。現時想隨時隨地看書可以很簡單，只需一機在手便可，無論坐巴士地鐵，或是等吃飯，只要打開電子工具便能翻閱書籍。閱讀外語書籍時亦想練習外語聆聽能力？有聲書便能幫助你。Audible是Amazon訂閱制的有聲電子書服務，讓你可以省卻很多時間，在你開車時﹑做運動等等的時候也可以利用時間聽書。不但可以省時可讀幾本書，更可同時練習你的專注能力和聆聽技巧，一舉多得。Audible採用月費計劃，會員每個月都會有特定的點數，可以購買不同價格的書籍。當點數用畢的時候，也可以直接選購，非常方便。Audible也可離線收聽，沒有互聯網的限制。有些Kindle電子書也有Audible版本，兩者可以一起購買，價錢可能更划算。'  
   
output by __hauhek__:  
>  '-日前-Amazon-正式-**宣佈**-**K-in-dle**- -app- -和-電子-書-都-加入-繁體-中文-的-支援-，-更-開設-了-共有- -20-,-000- -
本-書籍-的-繁體-中文-電子-書-的-專區-，-**各大-經典**-之作-亦-收錄-其中-。-閱讀-**電子-化**-方便-了-不少-書生-，-即使-出外-想-**攜帶**-書本-看看-，-也-不
怕-厚重-，-而且-一個-程式-更-**可收-錄**-多本-書籍**-，-簡單-方便-。-正所謂-**書中**-自有-黃-金屋-，-閱讀-既-可以-增進-知識-，-令人-建立-獨特-的-思維-
和-見解-，-更-可-讓-人-**放鬆**-心情-。-愛書-的-**人家-裡-分分鐘**-可能-擁有-**過-百本**-書籍-，-但-到-**最後**-一本-本書-脊泛-黃-滿-佈-塵埃-，-亦-不知-它們-該何-去-何-從-。-現時-想-隨時-隨地-看書-可以-很-簡單-，-只-需一機-在手-便-可-，-無論-坐-巴士-地鐵-，-或是-等-吃-飯-，-只要-打開-電子-工具-便-能-**翻閱-書籍**-。-閱讀-外語-書籍-**時亦想-練習**-外語-聆-聽-能力-？-有聲-書-便-能-幫助-你-。-Audible-是-Amazon-訂-閱制-的-有聲-電子-書-服務-，-讓-
你-可以-省-卻-很多-時間-，-在-你-開車-時-﹑-**做-運動**-等等-的-時候-也-可以-利用-時間-聽書-。-不但-可以-省時-可讀-幾本書-，-更-**可-同時-練習**-你-
的-專注-能力-和-聆-聽-技巧-，-一舉-多-得-。-Audible-採用-**月費-計劃**-，-會員-每個-月-都-會-有-特定-的-點數-，-可以-購買-不同-價格-的-書籍-。-當
點-數用-畢-的-時候-，-也-可以-直接-選購-，-非常-方便-。-Audible-也-可-離線-收-聽-，-沒有-互聯網-的-限制-。-有些-**K-in-dle**-電子-書-也-有-Audible-版本-，-兩者-可以-一起-購買-，-價錢-可能-更-划算-。'  

> 运行时间 ：**0.003183600000000064**  
   
>  
Output by __jieba__: 
>  '-日前-Amazon-正式-**宣-佈**-**Kindle**- -app- -和-電子-書-都-加入-繁體-中文-的-支援-，-更-開設-了-共有- -20-,-000- -本
書籍-的-繁體-中文-電子-書-的-專區-，-**各大經典**-之作-亦-收錄-其中-。-閱讀-**電子化**-方便-了-不少-書生-，-即使-出外-想-**攜-帶**書本-看看-，-也-不怕-厚
重-，-而且-一個-程式-更-**可-收錄-多-本書籍**-，-簡單-方便-。-正所謂-**書-中**-自有-黃-金屋-，-閱讀-既-可以-增進-知識-，-令人-建立-獨特-的-思維-和-見
解-，-更-可-讓-人-**放-鬆**-心情-。-愛書-的-**人家-裡分-分鐘**-可能-擁有-**過百本**-書籍-，-但-到-**最-後**-一本-本書-脊泛-黃-滿-佈-塵埃-，-亦-不知-它們-該何
-去-何-從-。-現時-想-隨時-隨地-看書-可以-很-簡單-，-只-需一機-在手-便-可-，-無論-坐-巴士-地鐵-，-或是-等-吃-飯-，-只要-打開-電子-工具-便-能-
**翻-閱書籍**-。-閱讀-外語-書籍-**時-亦-想練習**-外語-聆-聽-能力-？-有聲-書-便-能-幫助-你-。-Audible-是-Amazon-訂-閱制-的-有聲-電子-書-服務-，-讓-你-可以-省-卻-很多-時間-，-在-你-開車-時-﹑-**做運動**-等等-的-時候-也-可以-利用-時間-聽書-。-不但-可以-省時-可讀-幾本書-，-更-**可同-時練習**-你-的-專
注-能力-和-聆-聽-技巧-，-一舉-多-得-。-Audible-採用-**月-費計劃**-，-會員-每個-月-都-會-有-特定-的-點數-，-可以-購買-不同-價格-的-書籍-。-當點-數
用-畢-的-時候-，-也-可以-直接-選購-，-非常-方便-。-Audible-也-可-離線-收-聽-，-沒有-互聯網-的-限制-。-有些-**Kindle**-電子-書-也-有-Audible-版本-，-兩者-可以-一起-購買-，-價錢-可能-更-划算-。'  
    
> 运行时间： **0.8588442**  
   
####  Copyright (c) 2019 [HSUHK](https://dlc.hsu.edu.hk/)
