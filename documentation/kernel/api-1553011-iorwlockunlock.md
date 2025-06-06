# IORWLockUnlock

**Framework**: Kernel  
**Kind**: func

Unlock a read/write lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
void IORWLockUnlock(IORWLock *lock);
```

#### Discussion

Undo one call to IORWLockRead or IORWLockWrite. Results are undefined if the caller has not locked the lock. This function may block and so should not be called from interrupt level or while a spin lock is held.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

- [IORWLockAlloc](1553010-iorwlockalloc.md)
  Allocates and initializes a read/write lock.
- [IORWLockFree](1553003-iorwlockfree.md)
  Frees a read/write lock.
- [IORWLockGetMachLock](1553033-iorwlockgetmachlock.md)
  Accessor to a Mach read/write lock.
- [IORWLockRead](1553004-iorwlockread.md)
  Lock a read/write lock for read.
- [IORWLockWrite](1552996-iorwlockwrite.md)
  Lock a read/write lock for write.
- [IORWUnlock](1553027-iorwunlock.md)
- [IOWriteLock](1552985-iowritelock.md)
- [IOReadLock](1553022-ioreadlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553011-iorwlockunlock)*