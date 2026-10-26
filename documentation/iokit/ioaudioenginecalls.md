# IOAudioEngineCalls

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

The set of constants passed to IOAudioEngineUserClient::getExternalMethodForIndex() when making calls from the IOAudioFamily user client code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
typedef enum _IOAudioEngineCalls : unsigned int {
    ...
} IOAudioEngineCalls;
```

## Topics

### Constants
- [kIOAudioEngineCallGetConnectionID](./ioaudioenginecalls/kioaudioenginecallgetconnectionid.md)
- [kIOAudioEngineCallGetNearestStartTime](./ioaudioenginecalls/kioaudioenginecallgetneareststarttime.md)
- [kIOAudioEngineCallRegisterClientBuffer](./ioaudioenginecalls/kioaudioenginecallregisterclientbuffer.md)
- [kIOAudioEngineCallStart](./ioaudioenginecalls/kioaudioenginecallstart.md)
- [kIOAudioEngineCallStop](./ioaudioenginecalls/kioaudioenginecallstop.md)
- [kIOAudioEngineCallUnregisterClientBuffer](./ioaudioenginecalls/kioaudioenginecallunregisterclientbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioaudioenginecalls)*