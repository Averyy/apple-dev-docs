# kIOPropertyPhysicalInterconnectTypeVirtual

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectTypeVirtual
```

## Discussion

This key defines the value of Virtual Interface for the key kIOPropertyPhysicalInterconnectTypeVirtual. If the device is being made to look like a storage device, but is not such in actuality, such as a File or RAM, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Virtual Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>File</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypevirtual)*