# kIOPropertyFibreChannelPortWorldWideNameKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyFibreChannelPortWorldWideNameKey
```

## Discussion

This key is the unique 64-bit World Wide Name for the port.

Requirement: Mandatory for Fibre Channel Interface.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>Fibre Channel Interface</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   	<key>Port World Wide Name</key>
   	<data>0011223344556677</data>
   </dict>
</dict>
```

Example2:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port World Wide Name</key>
   	<data>0011223344556677</data>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelportworldwidenamekey)*