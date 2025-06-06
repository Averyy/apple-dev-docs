# IOTakeLock

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
void IOTakeLock(IOLock *lock);
```

## See Also

- [IOLockAlloc](1553021-iolockalloc.md)
  Allocates and initializes a mutex.
- [IOLockInitWithState](1553028-iolockinitwithstate.md)
- [IOLockFree](1553034-iolockfree.md)
  Frees a mutex.
- [IOTryLock](1553012-iotrylock.md)
- [IOLockLock](1553000-iolocklock.md)
  Lock a mutex.
- [IOUnlock](1552994-iounlock.md)
- [IOLockTryLock](1553018-iolocktrylock.md)
  Attempt to lock a mutex.
- [IOLockUnlock](1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](1553016-iolockwakeup.md)
- [IOLockSleep](1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553007-iotakelock)*