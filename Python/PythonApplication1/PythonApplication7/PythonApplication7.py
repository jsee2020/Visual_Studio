import pandas as pd
import matplotlib.pyplot as plt

#idx=pd.date_range('2021-09-01','2021-12-31')
tmp_File='C:\\Users\\jseek\\Downloads\\거래내역조회20210901 (1).xls'
tmp_DB = pd.read_excel(tmp_File, sheet_name='sheet')

tmp_group=tmp_DB.groupby(by=['거래일시']).count()
#tmp_DB.index=pd.DatetimeIndex(tmp_DB.index)
#tmp_DB=tmp_DB.reindex(idx,fill_value='NA')
#tmp_DB=tmp_DB.reindex(idx, fill_value=" ")

plt.title('test')
plt.xlabel('Date')
plt.ylabel('Count')

#tmp_DB['찾으신금액'].plot(kind='line', color='green', marker='o', linestyle='')
tmp_group['No.'].plot(kind='line', color='green', marker='o', linestyle='')
plt.show(block=True)
#fig=plt.figure()
#plt.close(fig)
#plt.savefig('test.jpg')
print(tmp_group)
