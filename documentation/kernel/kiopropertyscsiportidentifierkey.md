# kIOPropertySCSIPortIdentifierKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.7+

## Declaration

```c
#define kIOPropertySCSIPortIdentifierKey
```

## Discussion

This key is the unique port identifier for the device server node located at this port, or for the initiating host port. The format for this data is allowed to be vendor-specific, as long as it is guaranteed to be unique. Length is arbitrary, to allow for itnerfaces with non-standard identifier rules. It is recommended to have this be a copy of an existing standard unique identifier for this port, should one already exist for your interface type

Requirement: Mandatory.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Fibre Channel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   	<key>Node World Wide Name</key>
   	<data>0011223344556677</data>
   	<key>Unique SCSI Port Identifier</key>
   	<data>0011223344556677</data>
   </dict>
</dict>
```

Example2:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Unique SCSI Port Identifier</key>
   	<data>0011223344556677</data>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsiportidentifierkey)*