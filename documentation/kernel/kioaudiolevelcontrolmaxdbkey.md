# kIOAudioLevelControlMaxDBKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

The key in the IORgistry for the IOAudioControl maximum db value attribute.

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOAudioLevelControlMaxDBKey
```

#### Discussion

The value returned by this key is a fixed point value in 16.16 format represented as a 32-bit integer. It represents the maximum value in db for the IOAudioControl. This value matches the maximum value attribute. This is currently valid for Level controls or other driver-defined controls that have a minimum and maximum db value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioaudiolevelcontrolmaxdbkey)*