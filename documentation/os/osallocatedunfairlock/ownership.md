# OSAllocatedUnfairLock.Ownership

**Framework**: os  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents the ownership status of an unfair lock.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@frozen
enum Ownership
```

## Topics

### Specifying ownership
- [OSAllocatedUnfairLock.Ownership.owner](./ownership/owner.md)
  Describes code that owns the lock.
- [OSAllocatedUnfairLock.Ownership.notOwner](./ownership/notowner.md)
  Describes code that doesn’t own the lock.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining lock ownership
- [func precondition(OSAllocatedUnfairLock<State>.Ownership)](./precondition%28_%29.md)
  Asserts if the lock object fails to meet specified ownership requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/ownership)*