# kIOPropertyPortSpeedAutomatic4GigabitKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortSpeedAutomatic4GigabitKey
```

## Discussion

This key defines the value of Automatic (4 Gigabit) for the key kIOPropertyPortSpeedKey. If the speed of the port is 4 Gigabits per second and is automatically determined by host software, this key should be used. Note: This value can change. It is not a static value.

Requirement: Optional for any interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Speed</key>
   	<string>Automatic (4 Gigabit)</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportspeedautomatic4gigabitkey)*