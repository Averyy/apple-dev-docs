# kIOPropertyPortSpeedAutomaticKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortSpeedAutomaticKey
```

#### Discussion

This key defines the value of Automatic for the key kIOPropertyPortSpeedKey. If the speed of the port is automatically adjusted by the host/device and a definitive speed is not known, this key should be used.

Note: This value can change. It is not a static value.

Requirement: Optional for any interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Speed</key>
   	<string>Automatic</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatickey)*