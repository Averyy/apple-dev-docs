# TimerEvent

**Framework**: Kernel  
**Kind**: tdef

Generic timer event callback for IOAudioDevice timer targets

## Declaration

```swift
typedef void ( *TimerEvent)(
   OSObject *target,
   IOAudioDevice *audioDevice);
```

#### Overview

TimerEvent callback function takes two arguments; the target of the timer event and the IOAudioDevice sending the event.

## Parameters

- `target`: The target of the timer event - passed in when the timer event was registered
- `audioDevice`: The IOAudioDevice sending the event


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/timerevent)*