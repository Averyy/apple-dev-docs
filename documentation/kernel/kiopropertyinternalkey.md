# kIOPropertyInternalKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOPropertyInternalKey
```

## Discussion

This key defines the value of Internal for the key kIOPropertyPhysicalInterconnectLocationKey. If the device is connected to an internal bus, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>ATA</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyinternalkey)*