# kIOPropertyFibreChannelALPAKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyFibreChannelALPAKey
```

## Discussion

This key is the 8-bit Arbitrated Loop Physical Address (AL_PA) value as defined in the FC-AL-2 specification.

Note: This value can change. It is not a static value.

Requirement: Optional (only necessary for Fibre Channel Interface).

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Fibre Channel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   	<key>AL_PA</key>
   	<data>04</data>
   </dict>
</dict>
```

Example2:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>AL_PA</key>
   	<data>04</data>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelalpakey)*