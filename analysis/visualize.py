import os
import matplotlib.pyplot as plt

## directory setup
os.makedirs('visualization', exist_ok = True)

#Chart 1: return_rate_by_payment.png(Bar Chart)
payment_returns =(
    merged_df.groupby('payment_method')['returned']
    .mean()
    .sort_values(ascending = False) * 100
)

plt.figure(figsize=(8,5))
bars = plt.bar(payment_returns.index,payment_returns.values,color =['#e74c3c','#3498db','#2ecc71'])

## Add percentage labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1, f'{height:.1f}%', ha='center',va='bottom',fontsize = 10,fontweight ='bold')

plt.title('COD Returns at 44.4% - 3x Card',fontsize=12, fontweight='bold')
plt.xlabel('Payment ,Method',fontsize=10)
plt.ylabel('Return Rate (%)',fontsize=10)
plt.ylim(0,55)
plt.tight_layout()
plt.savefig('visualization/return_rate_by_payment.png',dpi=300)
plt.close()

## chart - 2 monthly_revenue_trend.png(Line Chart)
monthly_rev = merged_df[~merged_df['is_outlier']].groupby('year_month')['order_value'].sum()
x_labels = [str(period) for period in monthly_rev.index]

plt.figure(figsize=(9,5))
plt.plot(x_labels,monthly_rev.values, marker='o',color='#2b5c8f',linewidth=2.5,markersize=6)

plt.title('Outlier-Corrected Monthly Revenue Trend(Actual Peak: 2026-03)',fontsize=12,fontweight='bold')
plt.xlabel('Year-Month',fontsize=10)
plt.ylabel('Revenue ($)',fontsize=10)
plt.grid(True,linestyle='--',alpha=0.6)
plt.tight_layout()
plt.savefig('visualization/monthly_revenue_trend.png',dpi=300)
plt.close()
print("Both PNG plots successfully created and saved in 'visualization/' folder!")
