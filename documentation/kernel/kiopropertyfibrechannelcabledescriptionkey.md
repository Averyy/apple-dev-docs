# kIOPropertyFibreChannelCableDescriptionKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyFibreChannelCableDescriptionKey
```

#### Discussion

This key is associated with the cabling type used for this Fibre Channel port. Valid values include "Copper" and "Fiber Optic".

Requirement: Optional for Fibre Channel Interface. Not defined for any other physical interconnect.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionkey)*