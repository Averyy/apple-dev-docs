# OSAllocatedUnfairLock.Ownership

**Framework**: os  
**Kind**: enum

An enumeration that represents the ownership status of an unfair lock.

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
@frozen
enum Ownership
```

## Topics

### Specifying ownership
- [OSAllocatedUnfairLock.Ownership.owner](osallocatedunfairlock/ownership/owner.md)
  Describes code that owns the lock.
- [OSAllocatedUnfairLock.Ownership.notOwner](osallocatedunfairlock/ownership/notowner.md)
  Describes code that doesn’t own the lock.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func precondition(OSAllocatedUnfairLock<State>.Ownership)](osallocatedunfairlock/precondition(_:).md)
  Asserts if the lock object fails to meet specified ownership requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/ownership)*