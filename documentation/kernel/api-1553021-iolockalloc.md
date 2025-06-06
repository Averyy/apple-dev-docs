# IOLockAlloc

**Framework**: Kernel  
**Kind**: func

Allocates and initializes a mutex.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
IOLock * IOLockAlloc(void);
```

#### Return_value

Pointer to the allocated lock, or zero on failure.

#### Discussion

Allocates a mutex in general purpose memory, and initializes it. Mutexes are general purpose blocking mutual exclusion locks, supplied by libkern/locks.h. This function may block and so should not be called from interrupt level or while a spin lock is held. IOLocks use the global IOKit lock group, IOLockGroup. To simplify kext debugging and lock-heat analysis, consider using lck_* locks with a per-driver lock group, as defined in kern/locks.h.

## See Also

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
- [IOLockUnlock](1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](1553016-iolockwakeup.md)
- [IOLockSleep](1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553021-iolockalloc)*