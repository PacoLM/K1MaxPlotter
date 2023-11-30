""" 
Creality K1 Max LiDAR files 3D Plotter by pacolm@gmail.com 231130

The Creality K1 Max 3D printer has a LiDAR sensor that scans the part to check its measurements
The files are stored in the path: /usr/data/creality/tmp/pointCloud
scan_flow_table_point.temp -> scan before printing calibration pattern 
scan_flow_line_point.temp -> scan after zig zag calibration pattern is printed
scan_table_point.temp -> scan table before printing first layer
scan_first_layer_point.temp -> scan after printing first layer

"""
import json
import matplotlib.pyplot as plt

#K1Max calibration zigzag (1st)
file1_path = r'C:\temp\K1logs\scan1\scan_flow_table_point.temp'
file2_path = r'C:\temp\K1logs\scan1\scan_flow_line_point.temp'

#K1Max calibration zigzag (2nd)
file1_path = r'C:\temp\K1logs\scan2\scan_flow_table_point.temp'
file2_path = r'C:\temp\K1logs\scan2\scan_flow_line_point.temp'

# Open and read the JSON files
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Iterate through all tables in the JSON data to extract the data
for table_name1, table_data1 in data1.items():
    X1 = [row[0]/1000.0 for row in table_data1]
    Y1 = [row[1]/1000.0 for row in table_data1]
    Z1 = [row[2]/1000.0 for row in table_data1]
for table_name2, table_data2 in data2.items():
    X2 = [row[0]/1000.0 for row in table_data2]
    Y2 = [row[1]/1000.0 for row in table_data2]
    Z2 = [row[2]/1000.0 for row in table_data2]
    minLen=(len(Z1), len(Z2))[len(Z1)>len(Z2)] #find list with less data
    invertX= [-x for x in X2] #invert X Axis
    resultZ = [a - b for a, b in zip(Z2[0:minLen], Z1[0:minLen])] #substract printed data from empty bed data
    ax.plot(invertX[0:minLen], Y2[0:minLen], resultZ[0:minLen], c='blue', label=table_name2)
    
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
ax.set_title('LiDAR data')
plt.ylim([5, 75])
ax.view_init(elev=75, azim=-76) # set initial view
plt.tight_layout()
plt.show() 