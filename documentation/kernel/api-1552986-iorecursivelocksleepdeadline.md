# IORecursiveLockSleepDeadline

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.6+

## Declaration

```swift
int IORecursiveLockSleepDeadline(IORecursiveLock *_lock, void *event, AbsoluteTime deadline, UInt32 interType);
```

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
- [IORecursiveLockTryLock](1552993-iorecursivelocktrylock.md)
  Attempt to lock a recursive lock.
- [IORecursiveLockUnlock](1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552986-iorecursivelocksleepdeadline)*