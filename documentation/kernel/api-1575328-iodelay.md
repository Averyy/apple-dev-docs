# IODelay

**Framework**: Kernel  
**Kind**: func

Spin delay for a number of microseconds.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void IODelay(unsigned int microseconds);
```

#### Discussion

This function spins to delay for at least the number of specified microseconds. Since the CPU is busy spinning no time is made available to other processes; this method of delay should be used only for short periods. Also, the AbsoluteTime based APIs of kern/clock.h provide finer grained and lower cost delays.

## Parameters

- `microseconds`: The integer number of microseconds to spin wait.

## See Also

- [IOPause](1575333-iopause.md)
  Spin delay for a number of nanoseconds.
- [IOSleep](1575320-iosleep.md)
  Sleep the calling thread for a number of milliseconds.
- [IOSleepWithLeeway](1575303-iosleepwithleeway.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575328-iodelay)*