# setPurgeableState(_:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

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

#### Return_value

Returns the prior purgeable state of the image’s underlying texture.

#### Discussion

This method behaves the same as the [`setPurgeableState(_:)`](https://developer.apple.com/documentation/metal/mtlresource/setpurgeablestate(_:)) method of the [`MTLResource`](https://developer.apple.com/documentation/metal/mtlresource) class, except that the state might be [`MPSPurgeableState.allocationDeferred`](mpspurgeablestate/allocationdeferred.md), which means there is no underlying texture to mark as volatile or non-volatile. Attempts to set a purgeable state on [`MTLTexture`](https://developer.apple.com/documentation/metal/mtltexture) objects that have not yet been allocated will be ignored.

## Parameters

- `state`: The desired purgeable state of the image’s underlying texture.

## See Also

- [enum MPSPurgeableState](mpspurgeablestate.md)
  The purgeable state of an image’s underlying texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648820-setpurgeablestate)*