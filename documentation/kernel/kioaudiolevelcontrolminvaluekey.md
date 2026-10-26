# kIOAudioLevelControlMinValueKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

The key in the IORegistry for the IOAudioControl minimum value attribute.

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOAudioLevelControlMinValueKey
```

#### Discussion

The value returned by this key is a 32-bit integer representing the minimum value for the IOAudioControl. This is currently only valid for Level controls or other driver-defined controls that have a minimum and maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioaudiolevelcontrolminvaluekey)*