# kIOPropertySpecificationVersionKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPropertySpecificationVersionKey
```

#### Discussion

This key is used to indicate the card specification version.

Requirement: Mandatory.

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
   	<key>Specification Version</key>
   	<string>3.0</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertyspecificationversionkey)*