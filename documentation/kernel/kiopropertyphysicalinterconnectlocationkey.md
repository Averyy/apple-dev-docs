# kIOPropertyPhysicalInterconnectLocationKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectLocationKey
```

#### Discussion

This key is used to define the Physical Interconnect Location.

Requirement: Mandatory.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SCSI Parallel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnectlocationkey)*