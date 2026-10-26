# kIOPropertyFibreChannelCableDescriptionCopperKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyFibreChannelCableDescriptionCopperKey
```

#### Discussion

This key defines the value of Copper for the key kIOPropertyFibreChannelCableDescriptionKey. If the cabling is Copper, this key should be used.

Requirement: Optional for Fibre Channel Interface interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Fibre Channel Cabling Type</key>
   	<string>Copper</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptioncopperkey)*