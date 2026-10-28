# kIOPropertyBridgeCharacteristicsKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOPropertyBridgeCharacteristicsKey
```

## Discussion

This key is used to define Bridge Characteristics for a particular devices's bridge chipset. It has an associated dictionary which lists the bridge characteristics.

Requirement: Optional

Example:

```occ
 
 
<dict>
   <key>Bridge Characteristics</key>
   <dict>
   	<key>Bridge Vendor Name</key>
   	<string>Oxford Semiconductor</string>
   	<key>Bridge Model Name</key>
   	<string>FW911</string>
   	<key>Bridge Revision Level</key>
   	<string>3.7</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertybridgecharacteristicskey)*