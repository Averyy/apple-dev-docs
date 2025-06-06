# IOLockLock

**Framework**: Kernel  
**Kind**: func

Lock a mutex.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
void IOLockLock(IOLock *lock);
```

#### Discussion

Lock the mutex. If the lock is held by any thread, block waiting for its unlock. This function may block and so should not be called from interrupt level or while a spin lock is held. Locking the mutex recursively from one thread will result in deadlock.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553000-iolocklock)*