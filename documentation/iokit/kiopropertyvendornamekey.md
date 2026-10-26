# kIOPropertyVendorNameKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define kIOPropertyVendorNameKey
```

#### Discussion

This key is used to define the Vendor Name for a particular device and it has an associated string.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertyvendornamekey)*