# kIOPropertyRigidDiskGeometryKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyRigidDiskGeometryKey
```

## Discussion

This key is used to define a dictionary containing rigid disk geometry information.

Requirement: Optional. If a device publishes this dictionary, it must publish all key/value pairs which are deemed Mandatory.

Example:

```occ
 
 
<dict>
   <key>Device Characteristics</key>
   <dict>
   	<key>Vendor Name</key>
   	<string>Apple</string>
   	<key>Product Name</key>
   	<string>iPod</string>
   	<key>Product Revision Level</key>
   	<string>1.0</string>
   	<key>Rigid Disk Geometry</key>
   	<dict>
   		<key>Sector Count per Track</key>
   		<integer>12345</integer>
   		<key>Head Count</key>
   		<integer>12</integer>
   		<key>Cylinder Count</key>
   		<integer>12345</integer>
   		<key>Bytes per Physical Sector</key>
   		<integer>512</integer>
   	</dict>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertyrigiddiskgeometrykey)*