clear
cap mkdir E:/爬虫/python推文
cd E:/爬虫/python推文
copy "https://mp.weixin.qq.com/s/u9FeqoBaA3Mr0fPCUMbpqA" temp1.txt, replace
set obs 1
gen v = fileread("temp1.txt")
replace v = ustrregexra(v,"\r\n","")
replace v = ustrregexs(1) if ustrregexm(v,"基础语法：(.+)</a></p><p><br  />")
split v,parse(`"href=""')
drop v v1
sxpose,clear
split _var1,parse(`"" target="_blank""')
drop _var1
replace _var12 = ustrregexrf(_var12,".*?>","")
replace _var12 = ustrregexra(_var12,"<.*?>","")
replace _var12 = ustrregexra(_var12,"<.*","")
rename (_var11 _var12) (网址 推文名称)
compress
save python推文
