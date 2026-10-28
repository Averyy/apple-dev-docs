# kIOPropertyLogicalBlockSizeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOPropertyLogicalBlockSizeKey
```

## Discussion

This key is used to define the logical block size of a hard disk drive.

Requirement: Mandatory for hard disk drives with logical block size other than 512 bytes or that does not match its physical block size.

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
   	<key>Physical Block Size</key>
   	<integer>4096</integer>
   	<key>Logical Block Size</key>
   	<integer>512</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertylogicalblocksizekey)*