# kIOPropertySCSIDomainIdentifierKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.2+

## Declaration

```c
#define kIOPropertySCSIDomainIdentifierKey
```

#### Discussion

An identifier that will uniquely identify this SCSI Domain for the Physical Interconnect type. This identifier is only guaranteed to be unique for any given Physical Interconnect and is not guaranteed to be the same across restarts or shutdowns.

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
   	<key>SCSI Domain Identifier</key>
   	<integer>0</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsidomainidentifierkey)*