# IOLockUnlock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Unlock a mutex.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

*DriverKit*

```c
void IOLockUnlock(struct IOLock *lock);
```

*macOS*

```c
void IOLockUnlock(IOLock *lock);
```

## Discussion

Unlock the mutex and wake any blocked waiters. Results are undefined if the caller has not locked the mutex. This function may block and so should not be called from interrupt level or while a spin lock is held.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

### Mutexes
- [IOLockAlloc](./api-1553021-iolockalloc.md)
  Allocates and initializes a mutex.
- [IOLockInitWithState](./api-1553028-iolockinitwithstate.md)
- [IOLockFree](./api-1553034-iolockfree.md)
  Frees a mutex.
- [IOTryLock](./api-1553012-iotrylock.md)
- [IOTakeLock](./api-1553007-iotakelock.md)
- [IOLockLock](./api-1553000-iolocklock.md)
  Lock a mutex.
- [IOUnlock](./api-1552994-iounlock.md)
- [IOLockTryLock](./api-1553018-iolocktrylock.md)
  Attempt to lock a mutex.
- [IOLockWakeup](./api-1553016-iolockwakeup.md)
- [IOLockSleep](./api-1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](./api-1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](./api-1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553006-iolockunlock)*