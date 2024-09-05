#Importing Liberaries
import pandas as pd
import matplotlib.pyplot as plt

#Read The Files
hotel_details=pd.read_csv(r'C:\Users\Mohamed Samy\Desktop\New folder (5)\Hotel_details.csv')
hotel_attributes=pd.read_csv(r'C:\Users\Mohamed Samy\Desktop\New folder (5)\hotels_RoomPrice.csv')

#Select Specific Columns
selected_columns1=['hotelid', 'hotelname','city','starrating']
selected_columns2=['hotelcode', 'roomtype','price','maxoccupancy','closed','dtcollected']
updated_hotel_details=hotel_details[selected_columns1]

updated_hotel_attributes=hotel_attributes[selected_columns2]

#Merge Tables & Remove Duplicate Column & Conver Column To Date Type
merged_table=pd.merge(updated_hotel_details,updated_hotel_attributes,left_on='hotelid',right_on='hotelcode',how='inner')
merged_table=merged_table.drop(columns=['hotelcode'])
merged_table['dtcollected']=pd.to_datetime(merged_table['dtcollected']).dt.date

#Plot DashBoard


fig, ax = plt.subplots(2,2)

#Bar

grouped_data=merged_table.groupby('hotelname')['price'].mean()
grouped_data=grouped_data.reset_index()
grouped_data.columns=['Hotel Name', 'Average Price']

colors = ['#2CA02C', '#1F77B4', '#FF7F0E']
labels = ['Hotel 1', 'Hotel 2', 'Hotel 3'] 
ax[0, 0].bar(grouped_data['Hotel Name'].tail(3),grouped_data['Average Price'].tail(3),label=labels,color=colors)

ax[0,0].set_title('Rooms Prices',fontsize='13',color='black',fontweight='bold')
ax[0, 0].set_xlabel('Hotels',fontsize='7',color='black',fontweight='bold')
ax[0, 0].set_ylabel('Average Price',fontsize='7',color='black',fontweight='bold')
ax[0,0].tick_params(axis='x',labelsize=5)
ax[0,0].tick_params(axis='y',labelsize=5)
ax[0,0].spines['top'].set_visible(False)
ax[0,0].spines['right'].set_visible(False)

#Bie

bie_grouped=merged_table.groupby('city')['price'].mean()
bie_grouped=bie_grouped.reset_index()
bie_grouped.columns=['City', 'Price']

ax[0,1].pie(bie_grouped['Price'].tail(3),labels=bie_grouped['City'].tail(3),autopct='%1.1f%%',shadow=True,startangle=90,textprops={'fontsize': 5, 'color': 'black', 'fontweight': 'bold'})
ax[0,1].set_title("Price Comparsion",fontsize=13,fontweight='bold',color='black')

#Bar
bar2_group=merged_table.groupby(['hotelname','roomtype','closed'])['maxoccupancy'].max()
bar2_group=bar2_group.reset_index()
bar2_group.columns=['Hotel Name', 'roomtype','Closed','MaxOccupancy']
bar2_group=bar2_group[bar2_group['Closed']!='N']
ax[1,0].bar(bar2_group['roomtype'].tail(3),bar2_group['MaxOccupancy'].tail(3),label=labels,color=colors)
ax[1,0].set_title("Room Occupancy",fontsize=13,fontweight='bold',color='black')
ax[1, 0].set_xlabel('RoomType',fontsize='7',color='black',fontweight='bold')
ax[1, 0].set_ylabel('Number Of Occupancy',fontsize='7',color='black',fontweight='bold')
ax[1,0].spines['top'].set_visible(False)
ax[1,0].spines['right'].set_visible(False)
ax[1,0].tick_params(axis='x',labelsize=5)
ax[1,0].tick_params(axis='y',labelsize=5)
fig.tight_layout(pad=2.0)

#Bar
bar3_group=merged_table.groupby(['hotelname','roomtype'])['starrating'].max()
bar3_group=bar3_group.reset_index()
bar3_group.columns=['Hotel Name', 'roomtype','Starrating']
ax[1,1].bar(bar3_group['roomtype'].tail(3),bar3_group['Starrating'].tail(3),label=labels,color=colors)
ax[1,1].spines['top'].set_visible(False)
ax[1,1].spines['right'].set_visible(False)
ax[1,1].tick_params(axis='x',labelsize=5)
ax[1,1].tick_params(axis='y',labelsize=5)
ax[1,1].set_title("Room Rating",fontsize=13,fontweight='bold',color='black')
ax[1, 1].set_xlabel('RoomType',fontsize='7',color='black',fontweight='bold')
ax[1, 1].set_ylabel('Room Rating',fontsize='7',color='black',fontweight='bold')

#Show
plt.suptitle("Hotel Analysis DashBoard", fontsize=16, fontweight='bold', color='darkblue')
fig.tight_layout(pad=2.0)

plt.show()
