# IOSimpleLockUnlockEnableInterrupt

**Framework**: Kernel  
**Kind**: func

Unlock a spin lock, and restore interrupt state.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void IOSimpleLockUnlockEnableInterrupt(IOSimpleLock *lock, IOInterruptState state);
```

#### Discussion

Unlock the lock, and restore preemption and interrupts to the state as they were when the lock was taken. Results are undefined if the caller has not locked the lock.

## Parameters

- `lock`: Pointer to the lock.
- `state`: The interrupt state returned by IOSimpleLockLockDisableInterrupt()

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1552998-iosimplelockunlockenableinterrup)*