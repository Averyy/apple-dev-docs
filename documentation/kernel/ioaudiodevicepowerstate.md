# IOAudioDevicePowerState

**Framework**: Kernel  
**Kind**: enum  
**Role**: Enumeration

Identifies the power state of the audio device

**Availability**:
- macOS 10.1+

## Declaration

```c
typedef enum _IOAudioDevicePowerState : unsigned int {
    ...
} IOAudioDevicePowerState;
```

#### Overview

A newly created IOAudioDevices defaults to the idle state.

## Topics

### Constants
- [kIOAudioDeviceSleep](./ioaudiodevicepowerstate/kioaudiodevicesleep.md)
- [kIOAudioDeviceIdle](./ioaudiodevicepowerstate/kioaudiodeviceidle.md)
- [kIOAudioDeviceActive](./ioaudiodevicepowerstate/kioaudiodeviceactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevicepowerstate)*