# IOSimpleLockTryLock

**Framework**: Kernel  
**Kind**: func

Attempt to lock a spin lock.

**Availability**:
- macOS 10.0+

## Declaration

```swift
boolean_t IOSimpleLockTryLock(IOSimpleLock *lock);
```

#### Discussion

Lock the spin lock if it is currently unlocked, and return true. If the lock is held, return false. Successful calls to IOSimpleLockTryLock should be balanced with calls to IOSimpleLockUnlock.

## Parameters

- `lock`: Pointer to the lock.

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
- [IOSimpleLockUnlock](1553015-iosimplelockunlock.md)
  Unlock a spin lock.
- [IOSimpleLockUnlockEnableInterrupt](1552998-iosimplelockunlockenableinterrup.md)
  Unlock a spin lock, and restore interrupt state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553029-iosimplelocktrylock)*