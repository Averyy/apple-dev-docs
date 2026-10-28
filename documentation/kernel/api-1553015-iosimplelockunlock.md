# IOSimpleLockUnlock

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Unlock a spin lock.

**Availability**:
- macOS 10.0+

## Declaration

```c
void IOSimpleLockUnlock(IOSimpleLock *lock);
```

## Discussion

Unlock the lock, and restore preemption. Results are undefined if the caller has not locked the lock.

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
- [IOSimpleLockLock](./api-1552997-iosimplelocklock.md)
  Lock a spin lock.
- [IOSimpleLockLockDisableInterrupt](./api-1553005-iosimplelocklockdisableinterrupt.md)
  Lock a spin lock.
- [IOSimpleLockTryLock](./api-1553029-iosimplelocktrylock.md)
  Attempt to lock a spin lock.
- [IOSimpleLockUnlockEnableInterrupt](./api-1552998-iosimplelockunlockenableinterrup.md)
  Unlock a spin lock, and restore interrupt state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553015-iosimplelockunlock)*