# kIOPropertyMediumRotationRateKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPropertyMediumRotationRateKey
```

#### Discussion

This key is used to indicate the medium rotation rate in RPM of the device.

Requirement: Optional.

Example:

```occ
 
 
<dict>
   <key>Device Characteristics</key>
   <dict>
   	<key>Vendor Name</key>
   	<string>AAPL</string>
   	<key>Product Name</key>
   	<string>FireWire Target</string>
   	<key>Product Revision Level</key>
   	<string>0000</string>
   	<key>Rotation Rate</key>
   	<integer>7200</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertymediumrotationratekey)*