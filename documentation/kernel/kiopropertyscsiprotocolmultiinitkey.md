# kIOPropertySCSIProtocolMultiInitKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.2+

## Declaration

```c
#define kIOPropertySCSIProtocolMultiInitKey
```

#### Discussion

This protocol characteristics key is used to inform the system that the protocol supports having multiple devices that act as initiators.

Requirement: Optional.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Fibre Channel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   	<key>Multiple Initiators</key>
   	<string>True</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyscsiprotocolmultiinitkey)*