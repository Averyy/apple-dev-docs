# takeDeformationUpdate(id:)

**Framework**: USDKit  
**Kind**: method

Consumes and returns the [`USDPlayer.DeformationData.Update`](usdplayer/deformationdata/update.md) for the given deformation delta update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func takeDeformationUpdate(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData.Update?
```

#### Discussion

Returns `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate/takedeformationupdate(id:))*