# IOSimpleLockGetMachLock

**Framework**: Kernel  
**Kind**: func

Accessor to a Mach spin lock.

**Availability**:
- macOS 10.4+

## Declaration

```swift
lck_spin_t * IOSimpleLockGetMachLock(IOSimpleLock *lock);
```

#### Discussion

Accessor to the Mach spin lock.

## Parameters

- `lock`: Pointer to the allocated lock.

## See Also

- [IOSimpleLockAlloc](1553017-iosimplelockalloc.md)
  Allocates and initializes a spin lock.
- [IOSimpleLockInit](1552990-iosimplelockinit.md)
  Initialize a spin lock.
- [IOSimpleLockDestroy](3380136-iosimplelockdestroy.md)
- [IOSimpleLockFree](1553035-iosimplelockfree.md)
  Frees a spin lock.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553019-iosimplelockgetmachlock)*