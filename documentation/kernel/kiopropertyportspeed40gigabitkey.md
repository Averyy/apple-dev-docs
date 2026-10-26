# kIOPropertyPortSpeed40GigabitKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.8+

## Declaration

```c
#define kIOPropertyPortSpeed40GigabitKey
```

#### Discussion

This key defines the value of 40 Gigabit for the key kIOPropertyPortSpeedKey. If the speed of the port is 40 Gigabits per second and is not automatically determined (i.e. the user configured the port to be exactly this speed), this key should be used.

Note: This value can change. It is not a static value.

Requirement: Optional for any interconnect.

Example:

```occ
 
 
 <dict>
 <key>Controller Characteristics</key>
 <dict>
 <key>Port Speed</key>
 <string>40 Gigabit</string>
 </dict>
 </dict>
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportspeed40gigabitkey)*