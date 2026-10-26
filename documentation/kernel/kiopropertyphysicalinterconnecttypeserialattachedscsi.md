# kIOPropertyPhysicalInterconnectTypeSerialAttachedSCSI

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectTypeSerialAttachedSCSI
```

#### Discussion

This key defines the value of SAS for the key kIOPropertyPhysicalInterconnectTypeKey. If the device is connected to a SAS bus, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SAS</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypeserialattachedscsi)*