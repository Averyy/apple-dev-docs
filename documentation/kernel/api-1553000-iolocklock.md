# IOLockLock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Lock a mutex.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

*DriverKit*

```c
void IOLockLock(struct IOLock *lock);
```

*macOS*

```c
void IOLockLock(IOLock *lock);
```

## Discussion

Lock the mutex. If the lock is held by any thread, block waiting for its unlock. This function may block and so should not be called from interrupt level or while a spin lock is held. Locking the mutex recursively from one thread will result in deadlock.

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
- [IOUnlock](./api-1552994-iounlock.md)
- [IOLockTryLock](./api-1553018-iolocktrylock.md)
  Attempt to lock a mutex.
- [IOLockUnlock](./api-1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](./api-1553016-iolockwakeup.md)
- [IOLockSleep](./api-1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](./api-1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](./api-1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553000-iolocklock)*