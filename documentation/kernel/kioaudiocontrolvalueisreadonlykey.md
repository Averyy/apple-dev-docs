# kIOAudioControlValueIsReadOnlyKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

The key in the IORegistry for the IOAudioControl value-is-read-only attribute.

**Availability**:
- macOS 10.2+

## Declaration

```c
#define kIOAudioControlValueIsReadOnlyKey
```

#### Discussion

The value returned by this key is a 32-bit integer but the value doesn't have any direct meaning. Instead, the presence of this key indicates that the value for the control is read-only


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioaudiocontrolvalueisreadonlykey)*