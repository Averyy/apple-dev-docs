# IORecursiveLockHaveLock

**Framework**: Kernel  
**Kind**: func

Check if a recursive lock is held by the calling thread.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
boolean_t IORecursiveLockHaveLock(const IORecursiveLock *lock);
```

#### Return_value

True if the calling thread holds the lock otherwise false.

#### Discussion

If the lock is held by the calling thread, return true, otherwise the lock is unlocked, or held by another thread and false is returned.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

- [IORecursiveLockAlloc](1553013-iorecursivelockalloc.md)
  Allocates and initializes an recursive lock.
- [IORecursiveLockFree](1553031-iorecursivelockfree.md)
  Frees a recursive lock.
- [IORecursiveLockGetMachLock](1552988-iorecursivelockgetmachlock.md)
  Accessor to a Mach mutex.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552995-iorecursivelockhavelock)*