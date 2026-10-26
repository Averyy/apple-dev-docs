# kIOPropertyPortDescriptionKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortDescriptionKey
```

#### Discussion

This key is associated with an human readable port description. Examples include "Channel A", "Port 1", etc.

Requirement: Optional for all interconnects.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Description</key>
   	<string>Channel A</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportdescriptionkey)*