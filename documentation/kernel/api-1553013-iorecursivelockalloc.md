# IORecursiveLockAlloc

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Allocates and initializes an recursive lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

*DriverKit*

```c
struct IORecursiveLock * IORecursiveLockAlloc(void);
```

*macOS*

```c
IORecursiveLock * IORecursiveLockAlloc(void);
```

## Return Value

Pointer to the allocated lock, or zero on failure.

## Discussion

Allocates a recursive lock in general purpose memory, and initializes it. Recursive locks function identically to mutexes but allow one thread to lock more than once, with balanced unlocks. IORecursiveLocks use the global IOKit lock group, IOLockGroup. To simplify kext debugging and lock-heat analysis, consider using lck_* locks with a per-driver lock group, as defined in kern/locks.h.

## See Also

### Recursive Locks
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
- [IORecursiveLockUnlock](./api-1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](./api-1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553013-iorecursivelockalloc)*