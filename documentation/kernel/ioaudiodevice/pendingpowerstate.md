# pendingPowerState

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```c
IOAudioDevicePowerState pendingPowerState;
```

## Overview

If a power state change is in progress, this represents the pending power state. All other times this is the same as the currentPowerState.

## See Also

### Instance Variables
- [workLoop](./workloop.md)
- [timerEventSource](./timereventsource.md)
- [timerEvents](./timerevents.md)
  The set of timer events in use by the device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/pendingpowerstate)*