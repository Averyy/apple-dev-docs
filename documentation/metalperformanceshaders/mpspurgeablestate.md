# MPSPurgeableState

**Framework**: Metal Performance Shaders  
**Kind**: enum

The purgeable state of an image’s underlying texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSPurgeableState : UInt, @unchecked Sendable
```

## Topics

### Constants
- [MPSPurgeableState.allocationDeferred](mpspurgeablestate/allocationdeferred.md)
  The image’s underlying texture hasn’t been allocated yet. Attempts to set another purgeable state using the [`setPurgeableState(_:)`](mpsimage/1648820-setpurgeablestate.md) method will be ignored.
- [MPSPurgeableState.keepCurrent](mpspurgeablestate/keepcurrent.md)
  Equivalent to the [`MTLPurgeableState.keepCurrent`](https://developer.apple.com/documentation/metal/mtlpurgeablestate/keepcurrent) value.
- [MPSPurgeableState.nonVolatile](mpspurgeablestate/nonvolatile.md)
  Equivalent to the [`MTLPurgeableState.nonVolatile`](https://developer.apple.com/documentation/metal/mtlpurgeablestate/nonvolatile) value.
- [MPSPurgeableState.volatile](mpspurgeablestate/volatile.md)
  Equivalent to the [`MTLPurgeableState.volatile`](https://developer.apple.com/documentation/metal/mtlpurgeablestate/volatile) value.
- [MPSPurgeableState.empty](mpspurgeablestate/empty.md)
  Equivalent to the [`MTLPurgeableState.empty`](https://developer.apple.com/documentation/metal/mtlpurgeablestate/empty) value.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [func setPurgeableState(MPSPurgeableState) -> MPSPurgeableState](mpsimage/1648820-setpurgeablestate.md)
  Set (or query) the purgeable state of the image’s underlying texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate)*