# MPSPurgeableState

**Framework**: Metal Performance Shaders  
**Kind**: enum

The purgeable state of an image’s underlying texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MPSPurgeableState
```

## Topics

### Constants
- [MPSPurgeableState.allocationDeferred](mpspurgeablestate/allocationdeferred.md)
  The image’s underlying texture hasn’t been allocated yet. Attempts to set another purgeable state using the [`setPurgeableState(_:)`](mpsimage/setpurgeablestate(_:).md) method will be ignored.
- [MPSPurgeableState.keepCurrent](mpspurgeablestate/keepcurrent.md)
  The current state is queried but doesn’t change.
- [MPSPurgeableState.nonVolatile](mpspurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MPSPurgeableState.volatile](mpspurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.
- [MPSPurgeableState.empty](mpspurgeablestate/empty.md)
  The contents of the resource are or will be discarded.
### Initializers
- [init?(rawValue: UInt)](mpspurgeablestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setPurgeableState(MPSPurgeableState) -> MPSPurgeableState](mpsimage/setpurgeablestate(_:).md)
  Set (or query) the purgeable state of the image’s underlying texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate)*