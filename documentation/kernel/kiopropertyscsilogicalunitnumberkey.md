# kIOPropertySCSILogicalUnitNumberKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.2+

## Declaration

```c
#define kIOPropertySCSILogicalUnitNumberKey
```

## Discussion

This key is the SCSI Logical Unit Number for the device server controlled by the driver.

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
   	<key>SCSI Logical Unit Number</key>
   	<integer>2</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsilogicalunitnumberkey)*