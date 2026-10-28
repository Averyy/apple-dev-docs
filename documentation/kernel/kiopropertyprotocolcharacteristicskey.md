# kIOPropertyProtocolCharacteristicsKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOPropertyProtocolCharacteristicsKey
```

## Discussion

This key is used to define Protocol Characteristics for a particular protocol and it has an associated dictionary which lists the protocol characteristics.

Requirement: Mandatory

Example:

```occ
 
 
<dict>
   <key>Protocol Characteristics</key>
   <dict>
   	<key>Physical Interconnect</key>
   	<string>ATAPI</string>
   	<key>Physical Interconnect Location</key>
   	<string>Internal</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyprotocolcharacteristicskey)*