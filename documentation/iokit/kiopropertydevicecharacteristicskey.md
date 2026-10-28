# kIOPropertyDeviceCharacteristicsKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define kIOPropertyDeviceCharacteristicsKey
```

## Discussion

This key is used to define Device Characteristics for a particular device and it has an associated dictionary which lists the device characteristics. The device characteristics are Command Set specific and are listed in the header files for each command set.

Requirement: Mandatory

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
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertydevicecharacteristicskey)*