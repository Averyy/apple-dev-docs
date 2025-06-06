# IORWLockRead

**Framework**: Kernel  
**Kind**: func

Lock a read/write lock for read.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

```swift
void IORWLockRead(IORWLock *lock);
```

#### Discussion

Lock the lock for read, allowing multiple readers when there are no writers. If the lock is held for write, block waiting for its unlock. This function may block and so should not be called from interrupt level or while a spin lock is held. Locking the lock recursively from one thread, for read or write, can result in deadlock.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

- [IORWLockAlloc](1553010-iorwlockalloc.md)
  Allocates and initializes a read/write lock.
- [IORWLockFree](1553003-iorwlockfree.md)
  Frees a read/write lock.
- [IORWLockGetMachLock](1553033-iorwlockgetmachlock.md)
  Accessor to a Mach read/write lock.
- [IORWLockUnlock](1553011-iorwlockunlock.md)
  Unlock a read/write lock.
- [IORWLockWrite](1552996-iorwlockwrite.md)
  Lock a read/write lock for write.
- [IORWUnlock](1553027-iorwunlock.md)
- [IOWriteLock](1552985-iowritelock.md)
- [IOReadLock](1553022-ioreadlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553004-iorwlockread)*