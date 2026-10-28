# kIOPropertyMediumTypeRotationalKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPropertyMediumTypeRotationalKey
```

## Discussion

This key is used to indicate the medium type of the device is rotational.

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
   	<key>Medium Type</key>
   	<string>Rotational</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertymediumtyperotationalkey)*