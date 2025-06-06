# precondition(_:)

**Framework**: os  
**Kind**: method

Asserts if the lock object fails to meet specified ownership requirements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func precondition(_ condition: OSAllocatedUnfairLock<State>.Ownership)
```

#### Discussion

Call this function to ensure the ownership state of the lock is what your code requires. For example, if you call this function and pass [`OSAllocatedUnfairLock.Ownership.owner`](osallocatedunfairlock/ownership/owner.md), the app terminates if the object is locked, but the calling code doesn’t own the lock. Similarly, if you call it and pass [`OSAllocatedUnfairLock.Ownership.notOwner`](osallocatedunfairlock/ownership/notowner.md), the app terminates if the calling code doesn’t own the lock, or if the object isn’t locked.

## Parameters

- `condition`: The ownership status to check.

## See Also

- [OSAllocatedUnfairLock.Ownership](osallocatedunfairlock/ownership.md)
  An enumeration that represents the ownership status of an unfair lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/precondition(_:))*