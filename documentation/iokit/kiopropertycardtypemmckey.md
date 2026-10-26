# kIOPropertyCardTypeMMCKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPropertyCardTypeMMCKey
```

#### Discussion

This key is used to indicate the card type is MMC.

Requirement: Optional.

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
   	 <string>MMC</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertycardtypemmckey)*