# kIOPropertyInterconnectRAMKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOPropertyInterconnectRAMKey
```

## Discussion

This key defines the value of RAM for the key kIOPropertyPhysicalInterconnectLocationKey. If the device is system memory that is being represented as a storage device, this key should be set.

NOTE: This key should only be used when the Physical Interconnect is set to Virtual Interface.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Virtual Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>RAM</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyinterconnectramkey)*