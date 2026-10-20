# IOWriteLock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
void IOWriteLock(IORWLock *lock);
```

## See Also

### Read/Write Locks
- [IORWLockAlloc](./api-1553010-iorwlockalloc.md)
  Allocates and initializes a read/write lock.
- [IORWLockFree](./api-1553003-iorwlockfree.md)
  Frees a read/write lock.
- [IORWLockGetMachLock](./api-1553033-iorwlockgetmachlock.md)
  Accessor to a Mach read/write lock.
- [IORWLockRead](./api-1553004-iorwlockread.md)
  Lock a read/write lock for read.
- [IORWLockUnlock](./api-1553011-iorwlockunlock.md)
  Unlock a read/write lock.
- [IORWLockWrite](./api-1552996-iorwlockwrite.md)
  Lock a read/write lock for write.
- [IORWUnlock](./api-1553027-iorwunlock.md)
- [IOReadLock](./api-1553022-ioreadlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552985-iowritelock)*