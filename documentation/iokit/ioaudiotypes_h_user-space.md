# IOAudioTypes.h User-Space

**Framework**: IOKit  
**Role**: API Collection

#### Overview

##### Included Headers

- <libkern/OSTypes.h>
- <mach/message.h>
- <device/device_types.h>

## Topics

### Data Types
- [IOAudioControlCalls](../kernel/ioaudiocontrolcalls.md)
  The set of constants passed to IOAudioControlUserClient::getExternalMethodForIndex() when making calls from the IOAudioFamily user client code.
- [IOAudioControlNotifications](../kernel/ioaudiocontrolnotifications.md)
  The set of constants passed in the type field of IOAudioControlUserClient::registerNotificaitonPort().
- [IOAudioEngineCalls](../kernel/ioaudioenginecalls.md)
  The set of constants passed to IOAudioEngineUserClient::getExternalMethodForIndex() when making calls from the IOAudioFamily user client code.
- [IOAudioEngineMemory](../kernel/ioaudioenginememory.md)
  Used to identify the type of memory requested by a client process to be mapped into its process space
- [IOAudioEngineState](../kernel/ioaudioenginestate.md)
  Represents the state of an IOAudioEngine
- [IOAudioEngineStatus](../kernel/ioaudioenginestatus.md)
  Shared-memory structure giving audio engine status
- [IOAudioNotificationMessage](../kernel/ioaudionotificationmessage.md)
  Used in the mach message for IOAudio notifications.
- [IOAudioSMPTETime](../kernel/ioaudiosmptetime.md)
  A structure for holding a SMPTE time.
- [IOAudioStreamDirection](../kernel/ioaudiostreamdirection.md)
  Represents the direction of an IOAudioStream
### Constants
- [Defines](./ioaudiotypes_h_user-space/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioaudiotypes_h_user-space)*