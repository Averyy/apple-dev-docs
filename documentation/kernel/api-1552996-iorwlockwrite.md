# IORWLockWrite

**Framework**: Kernel  
**Kind**: func

Lock a read/write lock for write.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
void IORWLockWrite(IORWLock *lock);
```

#### Discussion

Lock the lock for write, allowing one writer exlusive access. If the lock is held for read or write, block waiting for its unlock. This function may block and so should not be called from interrupt level or while a spin lock is held. Locking the lock recursively from one thread, for read or write, can result in deadlock.

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
- [IORWLockUnlock](1553011-iorwlockunlock.md)
  Unlock a read/write lock.
- [IORWUnlock](1553027-iorwunlock.md)
- [IOWriteLock](1552985-iowritelock.md)
- [IOReadLock](1553022-ioreadlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552996-iorwlockwrite)*