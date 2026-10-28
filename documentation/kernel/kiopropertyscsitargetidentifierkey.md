# kIOPropertySCSITargetIdentifierKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.2+

## Declaration

```c
#define kIOPropertySCSITargetIdentifierKey
```

## Discussion

This is the SCSI Target Identifier for a given SCSI Target Device.

Requirement: Mandatory for SCSI Parallel Interface and Fibre Channel Interface.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SCSI Parallel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   	<key>SCSI Target Identifier</key>
   	<integer>3</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsitargetidentifierkey)*