# IOAudioControlCalls

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

The set of constants passed to IOAudioControlUserClient::getExternalMethodForIndex() when making calls from the IOAudioFamily user client code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
typedef enum _IOAudioControlCalls : unsigned int {
    ...
} IOAudioControlCalls;
```

## Topics

### Constants
- [kIOAudioControlCallSetValue](./ioaudiocontrolcalls/kioaudiocontrolcallsetvalue.md)
- [kIOAudioControlCallGetValue](./ioaudiocontrolcalls/kioaudiocontrolcallgetvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioaudiocontrolcalls)*