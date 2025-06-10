# timerEvents

**Framework**: Kernel  
**Kind**: pseudo

The set of timer events in use by the device.

## Declaration

```swift
OSDictionary * timerEvents;
```

#### Overview

The key for the dictionary is the target of the event. This means that a single target may have only a single event associated with it.

## See Also

- [workLoop](ioaudiodevice/workloop.md)
- [timerEventSource](ioaudiodevice/timereventsource.md)
- [pendingPowerState](ioaudiodevice/pendingpowerstate.md)
- [numRunningAudioEngines](ioaudiodevice/numrunningaudioengines.md)
- [minimumInterval](ioaudiodevice/minimuminterval.md)
- [familyManagePower](ioaudiodevice/familymanagepower.md)
- [duringStartup](ioaudiodevice/duringstartup.md)
- [currentPowerState](ioaudiodevice/currentpowerstate.md)
- [commandGate](ioaudiodevice/commandgate.md)
- [audioPorts](ioaudiodevice/audioports.md)
- [audioEngines](ioaudiodevice/audioengines.md)
- [asyncPowerStateChangeInProgress](ioaudiodevice/asyncpowerstatechangeinprogress.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/timerevents)*