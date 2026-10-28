# kIOPropertyPhysicalInterconnectTypeATAPI

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectTypeATAPI
```

## Discussion

This key defines the value of ATAPI for the key kIOPropertyPhysicalInterconnectTypeKey. If the device is connected to an ATA bus and follows the ATAPI command specification, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>ATAPI</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypeatapi)*