# Locks

**Framework**: Kernel  
**Role**: API Collection

## Topics

### Simple Locks
- [IOSimpleLockAlloc](../api-1553017-iosimplelockalloc.md)
  Allocates and initializes a spin lock.
- [IOSimpleLockInit](../api-1552990-iosimplelockinit.md)
  Initialize a spin lock.
- [IOSimpleLockDestroy](../api-3380136-iosimplelockdestroy.md)
- [IOSimpleLockFree](../api-1553035-iosimplelockfree.md)
  Frees a spin lock.
- [IOSimpleLockGetMachLock](../api-1553019-iosimplelockgetmachlock.md)
  Accessor to a Mach spin lock.
- [IOSimpleLockLock](../api-1552997-iosimplelocklock.md)
  Lock a spin lock.
- [IOSimpleLockLockDisableInterrupt](../api-1553005-iosimplelocklockdisableinterrupt.md)
  Lock a spin lock.
- [IOSimpleLockTryLock](../api-1553029-iosimplelocktrylock.md)
  Attempt to lock a spin lock.
- [IOSimpleLockUnlock](../api-1553015-iosimplelockunlock.md)
  Unlock a spin lock.
- [IOSimpleLockUnlockEnableInterrupt](../api-1552998-iosimplelockunlockenableinterrup.md)
  Unlock a spin lock, and restore interrupt state.
### Mutexes
- [IOLockAlloc](../api-1553021-iolockalloc.md)
  Allocates and initializes a mutex.
- [IOLockInitWithState](../api-1553028-iolockinitwithstate.md)
- [IOLockFree](../api-1553034-iolockfree.md)
  Frees a mutex.
- [IOTryLock](../api-1553012-iotrylock.md)
- [IOTakeLock](../api-1553007-iotakelock.md)
- [IOLockLock](../api-1553000-iolocklock.md)
  Lock a mutex.
- [IOUnlock](../api-1552994-iounlock.md)
- [IOLockTryLock](../api-1553018-iolocktrylock.md)
  Attempt to lock a mutex.
- [IOLockUnlock](../api-1553006-iolockunlock.md)
  Unlock a mutex.
- [IOLockWakeup](../api-1553016-iolockwakeup.md)
- [IOLockSleep](../api-1553026-iolocksleep.md)
  Sleep with mutex unlock and relock
- [IOLockSleepDeadline](../api-1553030-iolocksleepdeadline.md)
- [IOLockGetMachLock](../api-1553008-iolockgetmachlock.md)
  Accessor to a Mach mutex.
### Read/Write Locks
- [IORWLockAlloc](../api-1553010-iorwlockalloc.md)
  Allocates and initializes a read/write lock.
- [IORWLockFree](../api-1553003-iorwlockfree.md)
  Frees a read/write lock.
- [IORWLockGetMachLock](../api-1553033-iorwlockgetmachlock.md)
  Accessor to a Mach read/write lock.
- [IORWLockRead](../api-1553004-iorwlockread.md)
  Lock a read/write lock for read.
- [IORWLockUnlock](../api-1553011-iorwlockunlock.md)
  Unlock a read/write lock.
- [IORWLockWrite](../api-1552996-iorwlockwrite.md)
  Lock a read/write lock for write.
- [IORWUnlock](../api-1553027-iorwunlock.md)
- [IOWriteLock](../api-1552985-iowritelock.md)
- [IOReadLock](../api-1553022-ioreadlock.md)
### Recursive Locks
- [IORecursiveLockAlloc](../api-1553013-iorecursivelockalloc.md)
  Allocates and initializes an recursive lock.
- [IORecursiveLockFree](../api-1553031-iorecursivelockfree.md)
  Frees a recursive lock.
- [IORecursiveLockGetMachLock](../api-1552988-iorecursivelockgetmachlock.md)
  Accessor to a Mach mutex.
- [IORecursiveLockHaveLock](../api-1552995-iorecursivelockhavelock.md)
  Check if a recursive lock is held by the calling thread.
- [IORecursiveLockLock](../api-1553020-iorecursivelocklock.md)
  Lock a recursive lock.
- [IORecursiveLockSleep](../api-1553001-iorecursivelocksleep.md)
- [IORecursiveLockSleepDeadline](../api-1552986-iorecursivelocksleepdeadline.md)
- [IORecursiveLockTryLock](../api-1552993-iorecursivelocktrylock.md)
  Attempt to lock a recursive lock.
- [IORecursiveLockUnlock](../api-1553032-iorecursivelockunlock.md)
  Unlock a recursive lock.
- [IORecursiveLockWakeup](../api-1553014-iorecursivelockwakeup.md)
### Condition Lock
- [IOConditionLock](../ioconditionlock.md)

## See Also

### Resources
- [Memory](./memory.md)
  Allocate, map, free, and manage memory in the kernel. 
- [Workflow and Control](./workflow_and_control.md)
- [Data Types](../libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokit_fundamentals/locks)*