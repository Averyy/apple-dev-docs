# IORecursiveLockTryLock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Attempt to lock a recursive lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

*DriverKit*

```c
bool IORecursiveLockTryLock(struct IORecursiveLock *lock);
```

*macOS*

```c
boolean_t IORecursiveLockTryLock(IORecursiveLock *lock);
```

#### Return Value

True if the lock is now locked by the caller, otherwise false.

#### Discussion

Lock the lock if it is currently unlocked, or held by the calling thread, and return true. If the lock is held by another thread, return false. Successful calls to IORecursiveLockTryLock should be balanced with calls to IORecursiveLockUnlock.

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
- [IORecursiveLockUnlock](./api-1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](./api-1553014-iorecursivelockwakeup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552993-iorecursivelocktrylock)*