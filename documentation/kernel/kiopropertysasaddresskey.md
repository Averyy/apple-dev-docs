# kIOPropertySASAddressKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.4+

## Declaration

```c
#define kIOPropertySASAddressKey
```

#### Discussion

This key is the unique 64-bit SAS Address for the device server node located at this port, or for the initiating host port.

Requirement: Mandatory for SAS.

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>SAS</string>
   	<key>Physical Interconnect Location</key>
   	<string>External</string>
   	<key>SAS Address</key>
   	<data>0011223344556677</data>
   </dict>
</dict>
```

Example2:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>SAS Address</key>
   	<data>0011223344556677</data>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertysasaddresskey)*