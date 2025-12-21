# App Neural Footprint

**Framework**: Analytics Reports

Analyze how much memory your process induces the Apple Neural Engine to wire down on your process’s behalf.

#### Overview

This report contains data that indicates how much Apple Neural Engine memory your application uses, sampled randomly across the fleet.

- Territories: Worldwide
- Platforms: iOS, iPadOS.  For more information about iOS and iPadOS, see the Platforms section in [`Data Completeness and Corrections`](data-completeness-corrections.md).
- Availability: - Daily: Every day.
- History: On request, data is available beginning with iOS 17.4 and iPadOS 17.4.
- Completeness: Data from devices that contribute to this report can arrive as late as 8 days after the date it generates on device. You can download recent data daily, but it might be incomplete, and data updates incrementally daily, until all late-arriving events are available.
- Privacy: - Includes data from users who have opted to share their data with Apple and developers.
- Individual rows will only appear if they have a value of 5 or more.
- Data Context: You can analyze your data with additional context by comparing it with the data in the [`App Sessions Context`](app-sessions-context.md) report, which provides a count of unique devices that use your app on a specific day. For example, if your app performed an action detailed in this report on 10 unique devices on a specific day, and the App Sessions Context report shows there were 100 unique devices running your app that day, then you can approximate that 10% of the devices running your app performed that action.

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Count | Number of times the event occurred | `integer` |
| Territory | Country or region in which the event occurred | `string` |
| Date | Date when the event occurred | `string` |
| Platform | OS version on the device on which the event occurred | `string` |
| Device | Type of device on which the event occurred | `string` |
| Build | Build of device on which event occurred | `string` |
| Unique Devices | The count of unique devices | `integer` |
| Release Type | Type of software release | `string` |
| App Version | Version of the app associated with the event | `string` |
| App Jetsam Priority | The current jetsam priority for the process | `integer` |
| App Neural Footprint KB | The current Apple Neural Engine memory footprint for the process | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| App Version | 102.1 | Bundle version of app |
| App Neural Footprint KB | 0.0 | Represents range from -Infinity to 100 |
| App Neural Footprint KB | 1.0 | Represents range from 100 to 200 |
| App Neural Footprint KB | 2.0 | Represents range from 200 to 300 |
| App Neural Footprint KB | 3.0 | Represents range from 300 to 400 |
| App Neural Footprint KB | 4.0 | Represents range from 400 to 500 |
| App Neural Footprint KB | 5.0 | Represents range from 500 to 600 |
| App Neural Footprint KB | 6.0 | Represents range from 600 to 700 |
| App Neural Footprint KB | 7.0 | Represents range from 700 to 800 |
| App Neural Footprint KB | 8.0 | Represents range from 800 to 900 |
| App Neural Footprint KB | 9.0 | Represents range from 900 to 1000 |
| App Neural Footprint KB | 10.0 | Represents range from 1000 to 1100 |
| App Neural Footprint KB | 11.0 | Represents range from 1100 to 1200 |
| App Neural Footprint KB | 12.0 | Represents range from 1200 to 1300 |
| App Neural Footprint KB | 13.0 | Represents range from 1300 to 1400 |
| App Neural Footprint KB | 14.0 | Represents range from 1400 to 1500 |
| App Neural Footprint KB | 15.0 | Represents range from 1500 to 1600 |
| App Neural Footprint KB | 16.0 | Represents range from 1600 to 1700 |
| App Neural Footprint KB | 17.0 | Represents range from 1700 to 1800 |
| App Neural Footprint KB | 18.0 | Represents range from 1800 to 1900 |
| App Neural Footprint KB | 19.0 | Represents range from 1900 to 2000 |
| App Neural Footprint KB | 20.0 | Represents range from 2000 to 2100 |
| App Neural Footprint KB | 21.0 | Represents range from 2100 to 2200 |
| App Neural Footprint KB | 22.0 | Represents range from 2200 to 2300 |
| App Neural Footprint KB | 23.0 | Represents range from 2300 to 2400 |
| App Neural Footprint KB | 24.0 | Represents range from 2400 to 2500 |
| App Neural Footprint KB | 25.0 | Represents range from 2500 to 2600 |
| App Neural Footprint KB | 26.0 | Represents range from 2600 to 2700 |
| App Neural Footprint KB | 27.0 | Represents range from 2700 to 2800 |
| App Neural Footprint KB | 28.0 | Represents range from 2800 to 2900 |
| App Neural Footprint KB | 29.0 | Represents range from 2900 to 3000 |
| App Neural Footprint KB | 30.0 | Represents range from 3000 to 3100 |
| App Neural Footprint KB | 31.0 | Represents range from 3100 to 3200 |
| App Neural Footprint KB | 32.0 | Represents range from 3200 to 3300 |
| App Neural Footprint KB | 33.0 | Represents range from 3300 to 3400 |
| App Neural Footprint KB | 34.0 | Represents range from 3400 to 3500 |
| App Neural Footprint KB | 35.0 | Represents range from 3500 to 3600 |
| App Neural Footprint KB | 36.0 | Represents range from 3600 to 3700 |
| App Neural Footprint KB | 37.0 | Represents range from 3700 to 3800 |
| App Neural Footprint KB | 38.0 | Represents range from 3800 to 3900 |
| App Neural Footprint KB | 39.0 | Represents range from 3900 to 4000 |
| App Neural Footprint KB | 40.0 | Represents range from 4000 to 4100 |
| App Neural Footprint KB | 41.0 | Represents range from 4100 to 4200 |
| App Neural Footprint KB | 42.0 | Represents range from 4200 to 4300 |
| App Neural Footprint KB | 43.0 | Represents range from 4300 to 4400 |
| App Neural Footprint KB | 44.0 | Represents range from 4400 to 4500 |
| App Neural Footprint KB | 45.0 | Represents range from 4500 to 4600 |
| App Neural Footprint KB | 46.0 | Represents range from 4600 to 4700 |
| App Neural Footprint KB | 47.0 | Represents range from 4700 to 4800 |
| App Neural Footprint KB | 48.0 | Represents range from 4800 to 4900 |
| App Neural Footprint KB | 49.0 | Represents range from 4900 to 5000 |
| App Neural Footprint KB | 50.0 | Represents range from 5000 to 5100 |
| App Neural Footprint KB | 51.0 | Represents range from 5100 to 5200 |
| App Neural Footprint KB | 52.0 | Represents range from 5200 to 5300 |
| App Neural Footprint KB | 53.0 | Represents range from 5300 to 5400 |
| App Neural Footprint KB | 54.0 | Represents range from 5400 to 5500 |
| App Neural Footprint KB | 55.0 | Represents range from 5500 to 5600 |
| App Neural Footprint KB | 56.0 | Represents range from 5600 to 5700 |
| App Neural Footprint KB | 57.0 | Represents range from 5700 to 5800 |
| App Neural Footprint KB | 58.0 | Represents range from 5800 to 5900 |
| App Neural Footprint KB | 59.0 | Represents range from 5900 to 6000 |
| App Neural Footprint KB | 60.0 | Represents range from 6000 to 6100 |
| App Neural Footprint KB | 61.0 | Represents range from 6100 to 6200 |
| App Neural Footprint KB | 62.0 | Represents range from 6200 to 6300 |
| App Neural Footprint KB | 63.0 | Represents range from 6300 to 6400 |
| App Neural Footprint KB | 64.0 | Represents range from 6400 to 6500 |
| App Neural Footprint KB | 65.0 | Represents range from 6500 to 6600 |
| App Neural Footprint KB | 66.0 | Represents range from 6600 to 6700 |
| App Neural Footprint KB | 67.0 | Represents range from 6700 to 6800 |
| App Neural Footprint KB | 68.0 | Represents range from 6800 to 6900 |
| App Neural Footprint KB | 69.0 | Represents range from 6900 to 7000 |
| App Neural Footprint KB | 70.0 | Represents range from 7000 to 7100 |
| App Neural Footprint KB | 71.0 | Represents range from 7100 to 7200 |
| App Neural Footprint KB | 72.0 | Represents range from 7200 to 7300 |
| App Neural Footprint KB | 73.0 | Represents range from 7300 to 7400 |
| App Neural Footprint KB | 74.0 | Represents range from 7400 to 7500 |
| App Neural Footprint KB | 75.0 | Represents range from 7500 to 7600 |
| App Neural Footprint KB | 76.0 | Represents range from 7600 to 7700 |
| App Neural Footprint KB | 77.0 | Represents range from 7700 to 7800 |
| App Neural Footprint KB | 78.0 | Represents range from 7800 to 7900 |
| App Neural Footprint KB | 79.0 | Represents range from 7900 to 8000 |
| App Neural Footprint KB | 80.0 | Represents range from 8000 to 8100 |
| App Neural Footprint KB | 81.0 | Represents range from 8100 to 8200 |
| App Neural Footprint KB | 82.0 | Represents range from 8200 to 8300 |
| App Neural Footprint KB | 83.0 | Represents range from 8300 to 8400 |
| App Neural Footprint KB | 84.0 | Represents range from 8400 to 8500 |
| App Neural Footprint KB | 85.0 | Represents range from 8500 to 8600 |
| App Neural Footprint KB | 86.0 | Represents range from 8600 to 8700 |
| App Neural Footprint KB | 87.0 | Represents range from 8700 to 8800 |
| App Neural Footprint KB | 88.0 | Represents range from 8800 to 8900 |
| App Neural Footprint KB | 89.0 | Represents range from 8900 to 9000 |
| App Neural Footprint KB | 90.0 | Represents range from 9000 to 9100 |
| App Neural Footprint KB | 91.0 | Represents range from 9100 to 9200 |
| App Neural Footprint KB | 92.0 | Represents range from 9200 to 9300 |
| App Neural Footprint KB | 93.0 | Represents range from 9300 to 9400 |
| App Neural Footprint KB | 94.0 | Represents range from 9400 to 9500 |
| App Neural Footprint KB | 95.0 | Represents range from 9500 to 9600 |
| App Neural Footprint KB | 96.0 | Represents range from 9600 to 9700 |
| App Neural Footprint KB | 97.0 | Represents range from 9700 to 9800 |
| App Neural Footprint KB | 98.0 | Represents range from 9800 to 9900 |
| App Neural Footprint KB | 99.0 | Represents range from 9900 to 10000 |
| App Neural Footprint KB | 100.0 | Represents range from 10000 to 11000 |
| App Neural Footprint KB | 101.0 | Represents range from 11000 to 12000 |
| App Neural Footprint KB | 102.0 | Represents range from 12000 to 13000 |
| App Neural Footprint KB | 103.0 | Represents range from 13000 to 14000 |
| App Neural Footprint KB | 104.0 | Represents range from 14000 to 15000 |
| App Neural Footprint KB | 105.0 | Represents range from 15000 to 16000 |
| App Neural Footprint KB | 106.0 | Represents range from 16000 to 17000 |
| App Neural Footprint KB | 107.0 | Represents range from 17000 to 18000 |
| App Neural Footprint KB | 108.0 | Represents range from 18000 to 19000 |
| App Neural Footprint KB | 109.0 | Represents range from 19000 to 20000 |
| App Neural Footprint KB | 110.0 | Represents range from 20000 to 21000 |
| App Neural Footprint KB | 111.0 | Represents range from 21000 to 22000 |
| App Neural Footprint KB | 112.0 | Represents range from 22000 to 23000 |
| App Neural Footprint KB | 113.0 | Represents range from 23000 to 24000 |
| App Neural Footprint KB | 114.0 | Represents range from 24000 to 25000 |
| App Neural Footprint KB | 115.0 | Represents range from 25000 to 26000 |
| App Neural Footprint KB | 116.0 | Represents range from 26000 to 27000 |
| App Neural Footprint KB | 117.0 | Represents range from 27000 to 28000 |
| App Neural Footprint KB | 118.0 | Represents range from 28000 to 29000 |
| App Neural Footprint KB | 119.0 | Represents range from 29000 to 30000 |
| App Neural Footprint KB | 120.0 | Represents range from 30000 to 31000 |
| App Neural Footprint KB | 121.0 | Represents range from 31000 to 32000 |
| App Neural Footprint KB | 122.0 | Represents range from 32000 to 33000 |
| App Neural Footprint KB | 123.0 | Represents range from 33000 to 34000 |
| App Neural Footprint KB | 124.0 | Represents range from 34000 to 35000 |
| App Neural Footprint KB | 125.0 | Represents range from 35000 to 36000 |
| App Neural Footprint KB | 126.0 | Represents range from 36000 to 37000 |
| App Neural Footprint KB | 127.0 | Represents range from 37000 to 38000 |
| App Neural Footprint KB | 128.0 | Represents range from 38000 to 39000 |
| App Neural Footprint KB | 129.0 | Represents range from 39000 to 40000 |
| App Neural Footprint KB | 130.0 | Represents range from 40000 to 41000 |
| App Neural Footprint KB | 131.0 | Represents range from 41000 to 42000 |
| App Neural Footprint KB | 132.0 | Represents range from 42000 to 43000 |
| App Neural Footprint KB | 133.0 | Represents range from 43000 to 44000 |
| App Neural Footprint KB | 134.0 | Represents range from 44000 to 45000 |
| App Neural Footprint KB | 135.0 | Represents range from 45000 to 46000 |
| App Neural Footprint KB | 136.0 | Represents range from 46000 to 47000 |
| App Neural Footprint KB | 137.0 | Represents range from 47000 to 48000 |
| App Neural Footprint KB | 138.0 | Represents range from 48000 to 49000 |
| App Neural Footprint KB | 139.0 | Represents range from 49000 to 50000 |
| App Neural Footprint KB | 140.0 | Represents range from 50000 to 51000 |
| App Neural Footprint KB | 141.0 | Represents range from 51000 to 52000 |
| App Neural Footprint KB | 142.0 | Represents range from 52000 to 53000 |
| App Neural Footprint KB | 143.0 | Represents range from 53000 to 54000 |
| App Neural Footprint KB | 144.0 | Represents range from 54000 to 55000 |
| App Neural Footprint KB | 145.0 | Represents range from 55000 to 56000 |
| App Neural Footprint KB | 146.0 | Represents range from 56000 to 57000 |
| App Neural Footprint KB | 147.0 | Represents range from 57000 to 58000 |
| App Neural Footprint KB | 148.0 | Represents range from 58000 to 59000 |
| App Neural Footprint KB | 149.0 | Represents range from 59000 to 60000 |
| App Neural Footprint KB | 150.0 | Represents range from 60000 to 61000 |
| App Neural Footprint KB | 151.0 | Represents range from 61000 to 62000 |
| App Neural Footprint KB | 152.0 | Represents range from 62000 to 63000 |
| App Neural Footprint KB | 153.0 | Represents range from 63000 to 64000 |
| App Neural Footprint KB | 154.0 | Represents range from 64000 to 65000 |
| App Neural Footprint KB | 155.0 | Represents range from 65000 to 66000 |
| App Neural Footprint KB | 156.0 | Represents range from 66000 to 67000 |
| App Neural Footprint KB | 157.0 | Represents range from 67000 to 68000 |
| App Neural Footprint KB | 158.0 | Represents range from 68000 to 69000 |
| App Neural Footprint KB | 159.0 | Represents range from 69000 to 70000 |
| App Neural Footprint KB | 160.0 | Represents range from 70000 to 71000 |
| App Neural Footprint KB | 161.0 | Represents range from 71000 to 72000 |
| App Neural Footprint KB | 162.0 | Represents range from 72000 to 73000 |
| App Neural Footprint KB | 163.0 | Represents range from 73000 to 74000 |
| App Neural Footprint KB | 164.0 | Represents range from 74000 to 75000 |
| App Neural Footprint KB | 165.0 | Represents range from 75000 to 76000 |
| App Neural Footprint KB | 166.0 | Represents range from 76000 to 77000 |
| App Neural Footprint KB | 167.0 | Represents range from 77000 to 78000 |
| App Neural Footprint KB | 168.0 | Represents range from 78000 to 79000 |
| App Neural Footprint KB | 169.0 | Represents range from 79000 to 80000 |
| App Neural Footprint KB | 170.0 | Represents range from 80000 to 81000 |
| App Neural Footprint KB | 171.0 | Represents range from 81000 to 82000 |
| App Neural Footprint KB | 172.0 | Represents range from 82000 to 83000 |
| App Neural Footprint KB | 173.0 | Represents range from 83000 to 84000 |
| App Neural Footprint KB | 174.0 | Represents range from 84000 to 85000 |
| App Neural Footprint KB | 175.0 | Represents range from 85000 to 86000 |
| App Neural Footprint KB | 176.0 | Represents range from 86000 to 87000 |
| App Neural Footprint KB | 177.0 | Represents range from 87000 to 88000 |
| App Neural Footprint KB | 178.0 | Represents range from 88000 to 89000 |
| App Neural Footprint KB | 179.0 | Represents range from 89000 to 90000 |
| App Neural Footprint KB | 180.0 | Represents range from 90000 to 91000 |
| App Neural Footprint KB | 181.0 | Represents range from 91000 to 92000 |
| App Neural Footprint KB | 182.0 | Represents range from 92000 to 93000 |
| App Neural Footprint KB | 183.0 | Represents range from 93000 to 94000 |
| App Neural Footprint KB | 184.0 | Represents range from 94000 to 95000 |
| App Neural Footprint KB | 185.0 | Represents range from 95000 to 96000 |
| App Neural Footprint KB | 186.0 | Represents range from 96000 to 97000 |
| App Neural Footprint KB | 187.0 | Represents range from 97000 to 98000 |
| App Neural Footprint KB | 188.0 | Represents range from 98000 to 99000 |
| App Neural Footprint KB | 189.0 | Represents range from 99000 to 100000 |
| App Neural Footprint KB | 190.0 | Represents range from 100000 to 110000 |
| App Neural Footprint KB | 191.0 | Represents range from 110000 to 120000 |
| App Neural Footprint KB | 192.0 | Represents range from 120000 to 130000 |
| App Neural Footprint KB | 193.0 | Represents range from 130000 to 140000 |
| App Neural Footprint KB | 194.0 | Represents range from 140000 to 150000 |
| App Neural Footprint KB | 195.0 | Represents range from 150000 to 160000 |
| App Neural Footprint KB | 196.0 | Represents range from 160000 to 170000 |
| App Neural Footprint KB | 197.0 | Represents range from 170000 to 180000 |
| App Neural Footprint KB | 198.0 | Represents range from 180000 to 190000 |
| App Neural Footprint KB | 199.0 | Represents range from 190000 to 200000 |
| App Neural Footprint KB | 200.0 | Represents range from 200000 to 210000 |
| App Neural Footprint KB | 201.0 | Represents range from 210000 to 220000 |
| App Neural Footprint KB | 202.0 | Represents range from 220000 to 230000 |
| App Neural Footprint KB | 203.0 | Represents range from 230000 to 240000 |
| App Neural Footprint KB | 204.0 | Represents range from 240000 to 250000 |
| App Neural Footprint KB | 205.0 | Represents range from 250000 to 260000 |
| App Neural Footprint KB | 206.0 | Represents range from 260000 to 270000 |
| App Neural Footprint KB | 207.0 | Represents range from 270000 to 280000 |
| App Neural Footprint KB | 208.0 | Represents range from 280000 to 290000 |
| App Neural Footprint KB | 209.0 | Represents range from 290000 to 300000 |
| App Neural Footprint KB | 210.0 | Represents range from 300000 to 310000 |
| App Neural Footprint KB | 211.0 | Represents range from 310000 to 320000 |
| App Neural Footprint KB | 212.0 | Represents range from 320000 to 330000 |
| App Neural Footprint KB | 213.0 | Represents range from 330000 to 340000 |
| App Neural Footprint KB | 214.0 | Represents range from 340000 to 350000 |
| App Neural Footprint KB | 215.0 | Represents range from 350000 to 360000 |
| App Neural Footprint KB | 216.0 | Represents range from 360000 to 370000 |
| App Neural Footprint KB | 217.0 | Represents range from 370000 to 380000 |
| App Neural Footprint KB | 218.0 | Represents range from 380000 to 390000 |
| App Neural Footprint KB | 219.0 | Represents range from 390000 to 400000 |
| App Neural Footprint KB | 220.0 | Represents range from 400000 to 410000 |
| App Neural Footprint KB | 221.0 | Represents range from 410000 to 420000 |
| App Neural Footprint KB | 222.0 | Represents range from 420000 to 430000 |
| App Neural Footprint KB | 223.0 | Represents range from 430000 to 440000 |
| App Neural Footprint KB | 224.0 | Represents range from 440000 to 450000 |
| App Neural Footprint KB | 225.0 | Represents range from 450000 to 460000 |
| App Neural Footprint KB | 226.0 | Represents range from 460000 to 470000 |
| App Neural Footprint KB | 227.0 | Represents range from 470000 to 480000 |
| App Neural Footprint KB | 228.0 | Represents range from 480000 to 490000 |
| App Neural Footprint KB | 229.0 | Represents range from 490000 to 500000 |
| App Neural Footprint KB | 230.0 | Represents range from 500000 to 510000 |
| App Neural Footprint KB | 231.0 | Represents range from 510000 to 520000 |
| App Neural Footprint KB | 232.0 | Represents range from 520000 to 530000 |
| App Neural Footprint KB | 233.0 | Represents range from 530000 to 540000 |
| App Neural Footprint KB | 234.0 | Represents range from 540000 to 550000 |
| App Neural Footprint KB | 235.0 | Represents range from 550000 to 560000 |
| App Neural Footprint KB | 236.0 | Represents range from 560000 to 570000 |
| App Neural Footprint KB | 237.0 | Represents range from 570000 to 580000 |
| App Neural Footprint KB | 238.0 | Represents range from 580000 to 590000 |
| App Neural Footprint KB | 239.0 | Represents range from 590000 to 600000 |
| App Neural Footprint KB | 240.0 | Represents range from 600000 to 610000 |
| App Neural Footprint KB | 241.0 | Represents range from 610000 to 620000 |
| App Neural Footprint KB | 242.0 | Represents range from 620000 to 630000 |
| App Neural Footprint KB | 243.0 | Represents range from 630000 to 640000 |
| App Neural Footprint KB | 244.0 | Represents range from 640000 to 650000 |
| App Neural Footprint KB | 245.0 | Represents range from 650000 to 660000 |
| App Neural Footprint KB | 246.0 | Represents range from 660000 to 670000 |
| App Neural Footprint KB | 247.0 | Represents range from 670000 to 680000 |
| App Neural Footprint KB | 248.0 | Represents range from 680000 to 690000 |
| App Neural Footprint KB | 249.0 | Represents range from 690000 to 700000 |
| App Neural Footprint KB | 250.0 | Represents range from 700000 to 710000 |
| App Neural Footprint KB | 251.0 | Represents range from 710000 to 720000 |
| App Neural Footprint KB | 252.0 | Represents range from 720000 to 730000 |
| App Neural Footprint KB | 253.0 | Represents range from 730000 to 740000 |
| App Neural Footprint KB | 254.0 | Represents range from 740000 to 750000 |
| App Neural Footprint KB | 255.0 | Represents range from 750000 to 760000 |
| App Neural Footprint KB | 256.0 | Represents range from 760000 to 770000 |
| App Neural Footprint KB | 257.0 | Represents range from 770000 to 780000 |
| App Neural Footprint KB | 258.0 | Represents range from 780000 to 790000 |
| App Neural Footprint KB | 259.0 | Represents range from 790000 to 800000 |
| App Neural Footprint KB | 260.0 | Represents range from 800000 to 810000 |
| App Neural Footprint KB | 261.0 | Represents range from 810000 to 820000 |
| App Neural Footprint KB | 262.0 | Represents range from 820000 to 830000 |
| App Neural Footprint KB | 263.0 | Represents range from 830000 to 840000 |
| App Neural Footprint KB | 264.0 | Represents range from 840000 to 850000 |
| App Neural Footprint KB | 265.0 | Represents range from 850000 to 860000 |
| App Neural Footprint KB | 266.0 | Represents range from 860000 to 870000 |
| App Neural Footprint KB | 267.0 | Represents range from 870000 to 880000 |
| App Neural Footprint KB | 268.0 | Represents range from 880000 to 890000 |
| App Neural Footprint KB | 269.0 | Represents range from 890000 to 900000 |
| App Neural Footprint KB | 270.0 | Represents range from 900000 to 910000 |
| App Neural Footprint KB | 271.0 | Represents range from 910000 to 920000 |
| App Neural Footprint KB | 272.0 | Represents range from 920000 to 930000 |
| App Neural Footprint KB | 273.0 | Represents range from 930000 to 940000 |
| App Neural Footprint KB | 274.0 | Represents range from 940000 to 950000 |
| App Neural Footprint KB | 275.0 | Represents range from 950000 to 960000 |
| App Neural Footprint KB | 276.0 | Represents range from 960000 to 970000 |
| App Neural Footprint KB | 277.0 | Represents range from 970000 to 980000 |
| App Neural Footprint KB | 278.0 | Represents range from 980000 to 990000 |
| App Neural Footprint KB | 279.0 | Represents range from 990000 to 1000000 |
| App Neural Footprint KB | 280.0 | Represents range from 1000000 to 1100000 |
| App Neural Footprint KB | 281.0 | Represents range from 1100000 to 1200000 |
| App Neural Footprint KB | 282.0 | Represents range from 1200000 to 1300000 |
| App Neural Footprint KB | 283.0 | Represents range from 1300000 to 1400000 |
| App Neural Footprint KB | 284.0 | Represents range from 1400000 to 1500000 |
| App Neural Footprint KB | 285.0 | Represents range from 1500000 to 1600000 |
| App Neural Footprint KB | 286.0 | Represents range from 1600000 to 1700000 |
| App Neural Footprint KB | 287.0 | Represents range from 1700000 to 1800000 |
| App Neural Footprint KB | 288.0 | Represents range from 1800000 to 1900000 |
| App Neural Footprint KB | 289.0 | Represents range from 1900000 to 2000000 |
| App Neural Footprint KB | 290.0 | Represents range from 2000000 to 2100000 |
| App Neural Footprint KB | 291.0 | Represents range from 2100000 to 2200000 |
| App Neural Footprint KB | 292.0 | Represents range from 2200000 to 2300000 |
| App Neural Footprint KB | 293.0 | Represents range from 2300000 to 2400000 |
| App Neural Footprint KB | 294.0 | Represents range from 2400000 to 2500000 |
| App Neural Footprint KB | 295.0 | Represents range from 2500000 to 2600000 |
| App Neural Footprint KB | 296.0 | Represents range from 2600000 to 2700000 |
| App Neural Footprint KB | 297.0 | Represents range from 2700000 to 2800000 |
| App Neural Footprint KB | 298.0 | Represents range from 2800000 to 2900000 |
| App Neural Footprint KB | 299.0 | Represents range from 2900000 to 3000000 |
| App Neural Footprint KB | 300.0 | Represents range from 3000000 to 3100000 |
| App Neural Footprint KB | 301.0 | Represents range from 3100000 to 3200000 |
| App Neural Footprint KB | 302.0 | Represents range from 3200000 to 3300000 |
| App Neural Footprint KB | 303.0 | Represents range from 3300000 to 3400000 |
| App Neural Footprint KB | 304.0 | Represents range from 3400000 to 3500000 |
| App Neural Footprint KB | 305.0 | Represents range from 3500000 to 3600000 |
| App Neural Footprint KB | 306.0 | Represents range from 3600000 to 3700000 |
| App Neural Footprint KB | 307.0 | Represents range from 3700000 to 3800000 |
| App Neural Footprint KB | 308.0 | Represents range from 3800000 to 3900000 |
| App Neural Footprint KB | 309.0 | Represents range from 3900000 to 4000000 |
| App Neural Footprint KB | 310.0 | Represents range from 4000000 to 4100000 |
| App Neural Footprint KB | 311.0 | Represents range from 4100000 to 4200000 |
| App Neural Footprint KB | 312.0 | Represents range from 4200000 to 4300000 |
| App Neural Footprint KB | 313.0 | Represents range from 4300000 to 4400000 |
| App Neural Footprint KB | 314.0 | Represents range from 4400000 to 4500000 |
| App Neural Footprint KB | 315.0 | Represents range from 4500000 to 4600000 |
| App Neural Footprint KB | 316.0 | Represents range from 4600000 to 4700000 |
| App Neural Footprint KB | 317.0 | Represents range from 4700000 to 4800000 |
| App Neural Footprint KB | 318.0 | Represents range from 4800000 to 4900000 |
| App Neural Footprint KB | 319.0 | Represents range from 4900000 to 5000000 |
| App Neural Footprint KB | 320.0 | Represents range from 5000000 to 5100000 |
| App Neural Footprint KB | 321.0 | Represents range from 5100000 to 5200000 |
| App Neural Footprint KB | 322.0 | Represents range from 5200000 to 5300000 |
| App Neural Footprint KB | 323.0 | Represents range from 5300000 to 5400000 |
| App Neural Footprint KB | 324.0 | Represents range from 5400000 to 5500000 |
| App Neural Footprint KB | 325.0 | Represents range from 5500000 to 5600000 |
| App Neural Footprint KB | 326.0 | Represents range from 5600000 to 5700000 |
| App Neural Footprint KB | 327.0 | Represents range from 5700000 to 5800000 |
| App Neural Footprint KB | 328.0 | Represents range from 5800000 to 5900000 |
| App Neural Footprint KB | 329.0 | Represents range from 5900000 to 6000000 |
| App Neural Footprint KB | 330.0 | Represents range from 6000000 to 6100000 |
| App Neural Footprint KB | 331.0 | Represents range from 6100000 to 6200000 |
| App Neural Footprint KB | 332.0 | Represents range from 6200000 to 6300000 |
| App Neural Footprint KB | 333.0 | Represents range from 6300000 to 6400000 |
| App Neural Footprint KB | 334.0 | Represents range from 6400000 to 6500000 |
| App Neural Footprint KB | 335.0 | Represents range from 6500000 to 6600000 |
| App Neural Footprint KB | 336.0 | Represents range from 6600000 to 6700000 |
| App Neural Footprint KB | 337.0 | Represents range from 6700000 to 6800000 |
| App Neural Footprint KB | 338.0 | Represents range from 6800000 to 6900000 |
| App Neural Footprint KB | 339.0 | Represents range from 6900000 to 7000000 |
| App Neural Footprint KB | 340.0 | Represents range from 7000000 to 7100000 |
| App Neural Footprint KB | 341.0 | Represents range from 7100000 to 7200000 |
| App Neural Footprint KB | 342.0 | Represents range from 7200000 to 7300000 |
| App Neural Footprint KB | 343.0 | Represents range from 7300000 to 7400000 |
| App Neural Footprint KB | 344.0 | Represents range from 7400000 to 7500000 |
| App Neural Footprint KB | 345.0 | Represents range from 7500000 to 7600000 |
| App Neural Footprint KB | 346.0 | Represents range from 7600000 to 7700000 |
| App Neural Footprint KB | 347.0 | Represents range from 7700000 to 7800000 |
| App Neural Footprint KB | 348.0 | Represents range from 7800000 to 7900000 |
| App Neural Footprint KB | 349.0 | Represents range from 7900000 to 8000000 |
| App Neural Footprint KB | 350.0 | Represents range from 8000000 to 8100000 |
| App Neural Footprint KB | 351.0 | Represents range from 8100000 to 8200000 |
| App Neural Footprint KB | 352.0 | Represents range from 8200000 to 8300000 |
| App Neural Footprint KB | 353.0 | Represents range from 8300000 to 8400000 |
| App Neural Footprint KB | 354.0 | Represents range from 8400000 to 8500000 |
| App Neural Footprint KB | 355.0 | Represents range from 8500000 to 8600000 |
| App Neural Footprint KB | 356.0 | Represents range from 8600000 to 8700000 |
| App Neural Footprint KB | 357.0 | Represents range from 8700000 to 8800000 |
| App Neural Footprint KB | 358.0 | Represents range from 8800000 to 8900000 |
| App Neural Footprint KB | 359.0 | Represents range from 8900000 to 9000000 |
| App Neural Footprint KB | 360.0 | Represents range from 9000000 to 9100000 |
| App Neural Footprint KB | 361.0 | Represents range from 9100000 to 9200000 |
| App Neural Footprint KB | 362.0 | Represents range from 9200000 to 9300000 |
| App Neural Footprint KB | 363.0 | Represents range from 9300000 to 9400000 |
| App Neural Footprint KB | 364.0 | Represents range from 9400000 to 9500000 |
| App Neural Footprint KB | 365.0 | Represents range from 9500000 to 9600000 |
| App Neural Footprint KB | 366.0 | Represents range from 9600000 to 9700000 |
| App Neural Footprint KB | 367.0 | Represents range from 9700000 to 9800000 |
| App Neural Footprint KB | 368.0 | Represents range from 9800000 to 9900000 |
| App Neural Footprint KB | 369.0 | Represents range from 9900000 to 10000000 |
| App Neural Footprint KB | 370.0 | Represents range from 10000000 to 11000000 |
| App Neural Footprint KB | 371.0 | Represents range from 11000000 to 12000000 |
| App Neural Footprint KB | 372.0 | Represents range from 12000000 to 13000000 |
| App Neural Footprint KB | 373.0 | Represents range from 13000000 to 14000000 |
| App Neural Footprint KB | 374.0 | Represents range from 14000000 to 15000000 |
| App Neural Footprint KB | 375.0 | Represents range from 15000000 to 16000000 |
| App Neural Footprint KB | 376.0 | Represents range from 16000000 to 17000000 |
| App Neural Footprint KB | 377.0 | Represents range from 17000000 to 18000000 |
| App Neural Footprint KB | 378.0 | Represents range from 18000000 to 19000000 |
| App Neural Footprint KB | 379.0 | Represents range from 19000000 to 20000000 |
| App Neural Footprint KB | 380.0 | Represents range from 20000000 to 21000000 |
| App Neural Footprint KB | 381.0 | Represents range from 21000000 to 22000000 |
| App Neural Footprint KB | 382.0 | Represents range from 22000000 to 23000000 |
| App Neural Footprint KB | 383.0 | Represents range from 23000000 to 24000000 |
| App Neural Footprint KB | 384.0 | Represents range from 24000000 to 25000000 |
| App Neural Footprint KB | 385.0 | Represents range from 25000000 to 26000000 |
| App Neural Footprint KB | 386.0 | Represents range from 26000000 to 27000000 |
| App Neural Footprint KB | 387.0 | Represents range from 27000000 to 28000000 |
| App Neural Footprint KB | 388.0 | Represents range from 28000000 to 29000000 |
| App Neural Footprint KB | 389.0 | Represents range from 29000000 to 30000000 |
| App Neural Footprint KB | 390.0 | Represents range from 30000000 to 31000000 |
| App Neural Footprint KB | 391.0 | Represents range from 31000000 to 32000000 |
| App Neural Footprint KB | 392.0 | Represents range from 32000000 to +Infinity |

## See Also

- [AirPlay Errors](airplay-errors.md)
  Analyze AirPlay errors in your apps.
- [AirPlay Performance](airplay-performance.md)
  Review AirPlay performance in your apps.
- [App Crashes Expanded](app-crashes-expanded.md)
  Analyze the rate at which your app crashes.
- [App Installs Performance](app-installs-performance.md)
  Analyze details about installation success and failure rates for your apps.
- [App Storage Reads and Writes](app-storage-reads-and-writes.md)
  Analyze how often your app uses disk reads and writes.
- [Audio Overloads](audio-overloads.md)
  Analyze how many audio glitches people experience in your app.
- [Bluetooth LE Session Duration](bluetooth-le-session-duration.md)
  Analyze how long your app uses Bluetooth Low Energy (LE) connections.
- [Bluetooth System Wakes](bluetooth-system-wakes.md)
  Analyze details about bluetooth system wakes that your app causes.
- [CAMetalLayer Performance](cametallayer-performance.md)
  Review CAMetalLayer metadata and performance in your app.
- [Custom Language Model Builds Failed](custom-language-model-builds-failed.md)
  Analyze how often your app-triggered rebuild of a custom language model failed.
- [Display Power Information](display-power-information.md)
  Review your app’s impact on display pixel attributes.
- [HTTP Live Streaming Playback Errors](http-live-streaming-playback-errors.md)
  Analyze playback errors that your app receives.
- [Launch Image Over Memory Limit](launch-image-over-memory-limit.md)
  Analyze how often your app fails to load because it’s over the memory limit.
- [Networking Connection Activity](networking-connection-activity.md)
  Review how your app uses network connections.
- [Spotlight Query Performance](spotlight-query-performance.md)
  Review how your app uses Spotlight queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-neural-footprint)*