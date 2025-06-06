# IORecursiveLockUnlock

**Framework**: Kernel  
**Kind**: func

Unlock a recursive lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
void IORecursiveLockUnlock(IORecursiveLock *lock);
```

#### Discussion

Undo one call to IORecursiveLockLock, if the lock is now unlocked wake any blocked waiters. Results are undefined if the caller does not balance calls to IORecursiveLockLock with IORecursiveLockUnlock. This function may block and so should not be called from interrupt level or while a spin lock is held.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

- [IORecursiveLockAlloc](1553013-iorecursivelockalloc.md)
  Allocates and initializes an recursive lock.
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
- [IORecursiveLockWakeup](1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553032-iorecursivelockunlock)*