# IORecursiveLockGetMachLock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Accessor to a Mach mutex.

**Availability**:
- macOS 10.4+

## Declaration

```c
lck_mtx_t * IORecursiveLockGetMachLock(IORecursiveLock *lock);
```

#### Discussion

Accessor to the Mach mutex.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

### Recursive Locks
- [IORecursiveLockAlloc](./api-1553013-iorecursivelockalloc.md)
  Allocates and initializes an recursive lock.
- [IORecursiveLockFree](./api-1553031-iorecursivelockfree.md)
  Frees a recursive lock.
- [IORecursiveLockHaveLock](./api-1552995-iorecursivelockhavelock.md)
  Check if a recursive lock is held by the calling thread.
- [IORecursiveLockLock](./api-1553020-iorecursivelocklock.md)
  Lock a recursive lock.
- [IORecursiveLockSleep](./api-1553001-iorecursivelocksleep.md)
- [IORecursiveLockSleepDeadline](./api-1552986-iorecursivelocksleepdeadline.md)
- [IORecursiveLockTryLock](./api-1552993-iorecursivelocktrylock.md)
  Attempt to lock a recursive lock.
- [IORecursiveLockUnlock](./api-1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](./api-1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552988-iorecursivelockgetmachlock)*