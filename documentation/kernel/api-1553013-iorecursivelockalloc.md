# IORecursiveLockAlloc

**Framework**: Kernel  
**Kind**: func

Allocates and initializes an recursive lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
IORecursiveLock * IORecursiveLockAlloc(void);
```

#### Return_value

Pointer to the allocated lock, or zero on failure.

#### Discussion

Allocates a recursive lock in general purpose memory, and initializes it. Recursive locks function identically to mutexes but allow one thread to lock more than once, with balanced unlocks. IORecursiveLocks use the global IOKit lock group, IOLockGroup. To simplify kext debugging and lock-heat analysis, consider using lck_* locks with a per-driver lock group, as defined in kern/locks.h.

## See Also

- [IORecursiveLockFree](1553031-iorecursivelockfree.md)
  Frees a recursive lock.
- [IORecursiveLockGetMachLock](1552988-iorecursivelockgetmachlock.md)
  Accessor to a Mach mutex.
- [IORecursiveLockHaveLock](1552995-iorecursivelockhavelock.md)
  Check if a recursive lock is held by the calling thread.
- [IORecursiveLockLock](1553020-iorecursivelocklock.md)
  Lock a recursive lock.
- [IORecursiveLockSleep](1553001-iorecursivelocksleep.md)
- [IORecursiveLockSleepDeadline](1552986-iorecursivelocksleepdeadline.md)
- [IORecursiveLockTryLock](1552993-iorecursivelocktrylock.md)
  Attempt to lock a recursive lock.
- [IORecursiveLockUnlock](1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553013-iorecursivelockalloc)*