# kIOPropertyInterconnectFileKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyInterconnectFileKey
```

#### Discussion

This key defines the value of File for the key kIOPropertyPhysicalInterconnectLocationKey. If the device is a file that is being represented as a storage device, this key should be set.

NOTE: This key should only be used when the Physical Interconnect is set to Virtual Interface.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyinterconnectfilekey)*