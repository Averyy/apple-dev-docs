# IORecursiveLockUnlock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Unlock a recursive lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

*DriverKit*

```c
void IORecursiveLockUnlock(struct IORecursiveLock *lock);
```

*macOS*

```c
void IORecursiveLockUnlock(IORecursiveLock *lock);
```

## Discussion

Undo one call to IORecursiveLockLock, if the lock is now unlocked wake any blocked waiters. Results are undefined if the caller does not balance calls to IORecursiveLockLock with IORecursiveLockUnlock. This function may block and so should not be called from interrupt level or while a spin lock is held.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

### Recursive Locks
- [IORecursiveLockAlloc](./api-1553013-iorecursivelockalloc.md)
  Allocates and initializes an recursive lock.
- [IORecursiveLockFree](./api-1553031-iorecursivelockfree.md)
  Frees a recursive lock.
- [IORecursiveLockGetMachLock](./api-1552988-iorecursivelockgetmachlock.md)
  Accessor to a Mach mutex.
- [IORecursiveLockHaveLock](./api-1552995-iorecursivelockhavelock.md)
  Check if a recursive lock is held by the calling thread.
- [IORecursiveLockLock](./api-1553020-iorecursivelocklock.md)
  Lock a recursive lock.
- [IORecursiveLockSleep](./api-1553001-iorecursivelocksleep.md)
- [IORecursiveLockSleepDeadline](./api-1552986-iorecursivelocksleepdeadline.md)
- [IORecursiveLockTryLock](./api-1552993-iorecursivelocktrylock.md)
  Attempt to lock a recursive lock.
- [IORecursiveLockWakeup](./api-1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553032-iorecursivelockunlock)*