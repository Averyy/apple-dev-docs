# kIOPropertyPhysicalInterconnectTypeSecureDigital

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.7+

## Declaration

```c
#define kIOPropertyPhysicalInterconnectTypeSecureDigital
```

#### Discussion

This key defines the value of Secure Digital for the key kIOPropertyPhysicalInterconnectTypeSecureDigital. If the device is connected to a Secure Digital port and follows the Secure Digital specification, this key should be set.

Example:

```occ
 
 
 <dict>
    <key>Protocol Characteristics</key>
    <dict>
        <key>Physical Interconnect</key>
        <string>Secure Digital</string>
        <key>Physical Interconnect Location</key>
        <string>Internal</string>
    </dict>
 </dict>
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypesecuredigital)*