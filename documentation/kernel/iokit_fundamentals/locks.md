# Locks

**Framework**: Kernel

## Topics

### Simple Locks
- [IOSimpleLockAlloc](1553017-iosimplelockalloc.md)
  Allocates and initializes a spin lock.
- [IOSimpleLockInit](1552990-iosimplelockinit.md)
  Initialize a spin lock.
- [IOSimpleLockDestroy](3380136-iosimplelockdestroy.md)
- [IOSimpleLockFree](1553035-iosimplelockfree.md)
  Frees a spin lock.
- [IOSimpleLockGetMachLock](1553019-iosimplelockgetmachlock.md)
  Accessor to a Mach spin lock.
- [IOSimpleLockLock](1552997-iosimplelocklock.md)
  Lock a spin lock.
- [IOSimpleLockLockDisableInterrupt](1553005-iosimplelocklockdisableinterrupt.md)
  Lock a spin lock.
- [IOSimpleLockTryLock](1553029-iosimplelocktrylock.md)
  Attempt to lock a spin lock.
- [IOSimpleLockUnlock](1553015-iosimplelockunlock.md)
  Unlock a spin lock.
- [IOSimpleLockUnlockEnableInterrupt](1552998-iosimplelockunlockenableinterrup.md)
  Unlock a spin lock, and restore interrupt state.
### Mutexes
- [IOLockAlloc](1553021-iolockalloc.md)
  Allocates and initializes a mutex.
- [IOLockInitWithState](1553028-iolockinitwithstate.md)
- [IOLockFree](1553034-iolockfree.md)
  Frees a mutex.
- [IOTryLock](1553012-iotrylock.md)
- [IOTakeLock](1553007-iotakelock.md)
- [IOLockLock](1553000-iolocklock.md)
  Lock a mutex.
- [IOUnlock](1552994-iounlock.md)
- [IOLockTryLock](1553018-iolocktrylock.md)
  Attempt to lock a mutex.
- [IOLockUnlock](1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](1553016-iolockwakeup.md)
- [IOLockSleep](1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.
### Read/Write Locks
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
- [IORWLockWrite](1552996-iorwlockwrite.md)
  Lock a read/write lock for write.
- [IORWUnlock](1553027-iorwunlock.md)
- [IOWriteLock](1552985-iowritelock.md)
- [IOReadLock](1553022-ioreadlock.md)
### Recursive Locks
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
- [IORecursiveLockUnlock](1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](1553014-iorecursivelockwakeup.md)
### Condition Lock
- [IOConditionLock](ioconditionlock.md)

## See Also

- [Memory](iokit_fundamentals/memory.md)
  Allocate, map, free, and manage memory in the kernel. 
- [Workflow and Control](iokit_fundamentals/workflow_and_control.md)
- [Data Types](libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokit_fundamentals/locks)*