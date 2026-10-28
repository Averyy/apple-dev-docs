# kIOPropertyPhysicalInterconnectTypeSCSIParallel

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectTypeSCSIParallel
```

## Discussion

This key defines the value of SCSI Parallel Interface for the key kIOPropertyPhysicalInterconnectTypeKey. If the device is connected to a SCSI Parallel port, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SCSI Parallel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypescsiparallel)*