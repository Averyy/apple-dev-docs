# kIOPropertySCSIInitiatorIdentifierKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertySCSIInitiatorIdentifierKey
```

## Discussion

An identifier that will uniquely identify this SCSI Initiator for the SCSI Domain.

Requirement: Mandatory for SCSI Parallel Interface, SAS, and Fibre Channel Interface.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SCSI Parallel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   	<key>SCSI Initiator Identifier</key>
   	<integer>7</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsiinitiatoridentifierkey)*