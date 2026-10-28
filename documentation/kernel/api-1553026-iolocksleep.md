# IOLockSleep

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Sleep with mutex unlock and relock

**Availability**:
- macOS 10.2+

## Declaration

```c
int IOLockSleep(IOLock *lock, void *event, UInt32 interType);
```

## Return Value

The wait-result value indicating how the thread was awakened.

## Discussion

Prepare to sleep,unlock the mutex, and re-acquire it on wakeup. Results are undefined if the caller has not locked the mutex. This function may block and so should not be called from interrupt level or while a spin lock is held.

## Parameters

- `lock`: Pointer to the locked lock.
- `event`: The event to sleep on.
- `interType`: How can the sleep be interrupted.

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
- [IOLockUnlock](./api-1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](./api-1553016-iolockwakeup.md)
- [IOLockSleepDeadline](./api-1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](./api-1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553026-iolocksleep)*