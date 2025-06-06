# IOPause

**Framework**: Kernel  
**Kind**: func

Spin delay for a number of nanoseconds.

**Availability**:
- macOS 10.5+

## Declaration

```swift
void IOPause(unsigned int nanoseconds);
```

#### Discussion

This function spins to delay for at least the number of specified nanoseconds. Since the CPU is busy spinning no time is made available to other processes; this method of delay should be used only for short periods.

## Parameters

- `microseconds`: The integer number of nanoseconds to spin wait.

## See Also

- [IODelay](1575328-iodelay.md)
  Spin delay for a number of microseconds.
- [IOSleep](1575320-iosleep.md)
  Sleep the calling thread for a number of milliseconds.
- [IOSleepWithLeeway](1575303-iosleepwithleeway.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575333-iopause)*