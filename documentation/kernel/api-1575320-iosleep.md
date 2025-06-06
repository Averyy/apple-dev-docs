# IOSleep

**Framework**: Kernel  
**Kind**: func

Sleep the calling thread for a number of milliseconds.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void IOSleep(unsigned int milliseconds);
```

#### Discussion

This function blocks the calling thread for at least the number of specified milliseconds, giving time to other processes.

## Parameters

- `milliseconds`: The integer number of milliseconds to wait.

## See Also

- [IODelay](1575328-iodelay.md)
  Spin delay for a number of microseconds.
- [IOPause](1575333-iopause.md)
  Spin delay for a number of nanoseconds.
- [IOSleepWithLeeway](1575303-iosleepwithleeway.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575320-iosleep)*