# kIOPropertyFibreChannelCableDescriptionFiberOpticKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyFibreChannelCableDescriptionFiberOpticKey
```

#### Discussion

This key defines the value of Fiber Optic for the key kIOPropertyFibreChannelCableDescriptionKey. If the cabling is Fiber Optic, this key should be used.

Requirement: Optional for Fibre Channel Interface interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Fibre Channel Cabling Type</key>
   	<string>Fiber Optic</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelcabledescriptionfiberoptickey)*