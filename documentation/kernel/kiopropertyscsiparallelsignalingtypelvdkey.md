# kIOPropertySCSIParallelSignalingTypeLVDKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertySCSIParallelSignalingTypeLVDKey
```

## Discussion

This key defines the value of Low Voltage Differential for the key kIOPropertySCSIParallelSignalingTypeKey. If the signaling type of the port is Low Voltage Differential, this key should be used.

Requirement: Optional for SCSI Parallel Interface interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>SCSI Parallel Signaling Type</key>
   	<string>Low Voltage Differential</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypelvdkey)*