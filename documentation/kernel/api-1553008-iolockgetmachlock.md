# IOLockGetMachLock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Accessor to a Mach mutex.

**Availability**:
- macOS 10.4+

## Declaration

```c
lck_mtx_t * IOLockGetMachLock(IOLock *lock);
```

#### Discussion

Accessor to the Mach mutex.

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
- [IOLockUnlock](./api-1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](./api-1553016-iolockwakeup.md)
- [IOLockSleep](./api-1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](./api-1553030-iolocksleepdeadline.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553008-iolockgetmachlock)*