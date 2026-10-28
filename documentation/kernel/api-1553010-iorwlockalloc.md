# IORWLockAlloc

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Allocates and initializes a read/write lock.

**Availability**:
- DriverKit 24.4+
- macOS 10.0+

## Declaration

*DriverKit*

```c
struct IORWLock * IORWLockAlloc(void);
```

*macOS*

```c
IORWLock * IORWLockAlloc(void);
```

## Return Value

Pointer to the allocated lock, or zero on failure.

## Discussion

Allocates and initializes a read/write lock in general purpose memory. Read/write locks provide for multiple readers, one exclusive writer, and are supplied by libkern/locks.h. This function may block and so should not be called from interrupt level or while a spin lock is held. IORWLocks use the global IOKit lock group, IOLockGroup. To simplify kext debugging and lock-heat analysis, consider using lck_* locks with a per-driver lock group, as defined in kern/locks.h.

## See Also

### Read/Write Locks
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
- [IOWriteLock](./api-1552985-iowritelock.md)
- [IOReadLock](./api-1553022-ioreadlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553010-iorwlockalloc)*