# kIOPropertyPortSpeedKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortSpeedKey
```

#### Discussion

This key is associated with the current port speed. The port speed can be any valid speed for the interconnect.

Note: This value can change. It is not a static value.

Requirement: Optional for any interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Speed</key>
   	<string>Automatic (1 Gigabit)</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportspeedkey)*