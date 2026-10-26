# kIOPropertyExternalKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOPropertyExternalKey
```

#### Discussion

This key defines the value of External for the key kIOPropertyPhysicalInterconnectLocationKey. If the device is connected to an external bus, this key should be set.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Fibre Channel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyexternalkey)*