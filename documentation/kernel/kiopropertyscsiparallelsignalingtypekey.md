# kIOPropertySCSIParallelSignalingTypeKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertySCSIParallelSignalingTypeKey
```

## Discussion

This key is associated with the signaling type used for this SCSI Parallel bus. Valid values include "High Voltage Differential", "Low Voltage Differential", and "Single Ended".

Requirement: Optional for SCSI Parallel Interface. Not defined for any other physical interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>SCSI Parallel Signaling Type</key>
   	<string>High Voltage Differential</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsiparallelsignalingtypekey)*