# setPurgeableState(_:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Set (or query) the purgeable state of the image’s underlying texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setPurgeableState(_ state: MPSPurgeableState) -> MPSPurgeableState
```

#### Return Value

Returns the prior purgeable state of the image’s underlying texture.

#### Discussion

This method behaves the same as the [`setPurgeableState(_:)`](https://developer.apple.com/documentation/Metal/MTLResource/setPurgeableState(_:)) method of the [`MTLResource`](https://developer.apple.com/documentation/Metal/MTLResource) class, except that the state might be [`MPSPurgeableState.allocationDeferred`](mpspurgeablestate/allocationdeferred.md), which means there is no underlying texture to mark as volatile or non-volatile. Attempts to set a purgeable state on [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) objects that have not yet been allocated will be ignored.

## Parameters

- `state`: The desired purgeable state of the image’s underlying texture.

## See Also

- [enum MPSPurgeableState](mpspurgeablestate.md)
  The purgeable state of an image’s underlying texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/setpurgeablestate(_:))*