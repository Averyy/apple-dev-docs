# kIOPropertyFibreChannelAddressIdentifierKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyFibreChannelAddressIdentifierKey
```

## Discussion

This key is the 24-bit Address Identifier (S_ID or D_ID) as defined in the FC-FS specification. It contains the address identifier of the source or destination Nx_Port.

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
   	<key>Address Identifier</key>
   	<data>001122</data>
   </dict>
</dict>
```

Example2:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Address Identifier</key>
   	<data>001122</data>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyfibrechanneladdressidentifierkey)*