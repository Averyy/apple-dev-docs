# IOLockUnlock

**Framework**: Kernel  
**Kind**: func

Unlock a mutex.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
void IOLockUnlock(IOLock *lock);
```

#### Discussion

Unlock the mutex and wake any blocked waiters. Results are undefined if the caller has not locked the mutex. This function may block and so should not be called from interrupt level or while a spin lock is held.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

- [IOLockAlloc](1553021-iolockalloc.md)
  Allocates and initializes a mutex.
- [IOLockInitWithState](1553028-iolockinitwithstate.md)
- [IOLockFree](1553034-iolockfree.md)
  Frees a mutex.
- [IOTryLock](1553012-iotrylock.md)
- [IOTakeLock](1553007-iotakelock.md)
- [IOLockLock](1553000-iolocklock.md)
  Lock a mutex.
- [IOUnlock](1552994-iounlock.md)
- [IOLockTryLock](1553018-iolocktrylock.md)
  Attempt to lock a mutex.
- [IOLockWakeup](1553016-iolockwakeup.md)
- [IOLockSleep](1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553006-iolockunlock)*