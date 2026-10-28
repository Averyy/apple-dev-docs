# kIOPropertyProductSerialNumberKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOPropertyProductSerialNumberKey
```

## Discussion

This key is used to indicate the card serial number ID.

Requirement: Mandatory

Example:

```occ
 
 
 <dict>
    <key>Card Characteristics</key>
    <dict>
   	 <key>Product Name</key>
   	 <string>SD32G</string>
   	 <key>Product Revision Level</key>
   	 <string>1.0</string>
   	 <key>Card Type</key>
   	 <string>SDHC</string>
   	 <key>Serial Number</key>
   	 <data>0045ff</data>
    </dict>
 </dict>
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertyproductserialnumberkey)*