# kIOAudioEngineStateKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

The key in the IORegistry for the IOAudioEngine state atrribute

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOAudioEngineStateKey
```

## Discussion

The value for this key may be one of: "Running", "Stopped" or "Paused". Currently the "Paused" state is unimplemented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioaudioenginestatekey)*