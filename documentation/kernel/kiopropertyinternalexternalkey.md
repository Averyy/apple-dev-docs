# kIOPropertyInternalExternalKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOPropertyInternalExternalKey
```

## Discussion

This key defines the value of Internal/External for the key kIOPropertyPhysicalInterconnectLocationKey. If the device is connected to a bus and it is indeterminate whether it is internal or external, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SCSI Parallel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal/External</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyinternalexternalkey)*