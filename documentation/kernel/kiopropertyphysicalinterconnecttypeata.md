# kIOPropertyPhysicalInterconnectTypeATA

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectTypeATA
```

## Discussion

This key defines the value of ATA for the key kIOPropertyPhysicalInterconnectTypeKey. If the device is connected to an ATA bus, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>ATA</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypeata)*