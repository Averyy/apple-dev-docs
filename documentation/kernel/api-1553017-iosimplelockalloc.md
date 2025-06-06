# IOSimpleLockAlloc

**Framework**: Kernel  
**Kind**: func

Allocates and initializes a spin lock.

**Availability**:
- macOS 10.0+

## Declaration

```swift
IOSimpleLock * IOSimpleLockAlloc(void);
```

#### Return_value

Pointer to the allocated lock, or zero on failure.

#### Discussion

Allocates and initializes a spin lock in general purpose memory. Spin locks provide non-blocking mutual exclusion for synchronization between thread context and interrupt context, or for multiprocessor synchronization, and are supplied by libkern/locks.h. This function may block and so should not be called from interrupt level or while a spin lock is held. IOSimpleLocks use the global IOKit lock group, IOLockGroup. To simplify kext debugging and lock-heat analysis, consider using lck_* locks with a per-driver lock group, as defined in kern/locks.h.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553017-iosimplelockalloc)*