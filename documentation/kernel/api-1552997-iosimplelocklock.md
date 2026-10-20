# IOSimpleLockLock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Lock a spin lock.

**Availability**:
- macOS 10.0+

## Declaration

```c
void IOSimpleLockLock(IOSimpleLock *lock);
```

#### Discussion

Lock the spin lock. If the lock is held, spin waiting for its unlock. Spin locks disable preemption, cannot be held across any blocking operation, and should be held for very short periods. When used to synchronize between interrupt context and thread context they should be locked with interrupts disabled - IOSimpleLockLockDisableInterrupt() will do both. Locking the lock recursively from one thread will result in deadlock.

## Parameters

- `lock`: Pointer to the lock.

## See Also

### Simple Locks
- [IOSimpleLockAlloc](./api-1553017-iosimplelockalloc.md)
  Allocates and initializes a spin lock.
- [IOSimpleLockInit](./api-1552990-iosimplelockinit.md)
  Initialize a spin lock.
- [IOSimpleLockDestroy](./api-3380136-iosimplelockdestroy.md)
- [IOSimpleLockFree](./api-1553035-iosimplelockfree.md)
  Frees a spin lock.
- [IOSimpleLockGetMachLock](./api-1553019-iosimplelockgetmachlock.md)
  Accessor to a Mach spin lock.
- [IOSimpleLockLockDisableInterrupt](./api-1553005-iosimplelocklockdisableinterrupt.md)
  Lock a spin lock.
- [IOSimpleLockTryLock](./api-1553029-iosimplelocktrylock.md)
  Attempt to lock a spin lock.
- [IOSimpleLockUnlock](./api-1553015-iosimplelockunlock.md)
  Unlock a spin lock.
- [IOSimpleLockUnlockEnableInterrupt](./api-1552998-iosimplelockunlockenableinterrup.md)
  Unlock a spin lock, and restore interrupt state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552997-iosimplelocklock)*