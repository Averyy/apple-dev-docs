# workLoop

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```c
IOWorkLoop *workLoop;
```

#### Overview

The IOWorkLoop for the driver - this is shared with the other objects in the driver

## See Also

### Instance Variables
- [timerEventSource](./timereventsource.md)
- [timerEvents](./timerevents.md)
  The set of timer events in use by the device.
- [pendingPowerState](./pendingpowerstate.md)
- [numRunningAudioEngines](./numrunningaudioengines.md)
- [minimumInterval](./minimuminterval.md)
- [familyManagePower](./familymanagepower.md)
- [duringStartup](./duringstartup.md)
- [currentPowerState](./currentpowerstate.md)
- [commandGate](./commandgate.md)
- [audioPorts](./audioports.md)
- [audioEngines](./audioengines.md)
- [asyncPowerStateChangeInProgress](./asyncpowerstatechangeinprogress.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/workloop)*