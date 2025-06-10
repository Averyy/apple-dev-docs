# pendingPowerState

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```swift
IOAudioDevicePowerState pendingPowerState;
```

#### Overview

If a power state change is in progress, this represents the pending power state. All other times this is the same as the currentPowerState.

## See Also

- [workLoop](ioaudiodevice/workloop.md)
- [timerEventSource](ioaudiodevice/timereventsource.md)
- [timerEvents](ioaudiodevice/timerevents.md)
  The set of timer events in use by the device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/pendingpowerstate)*