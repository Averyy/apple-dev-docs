# takeDeformationUpdate(id:)

**Framework**: USDKit  
**Kind**: method

Consumes and returns the [`USDPlayer.DeformationData.Update`](usdplayer/deformationdata/update.md) for the given deformation delta update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func takeDeformationUpdate(id: USDPlayer.DeformationID) -> USDPlayer.DeformationData.Update?
```

#### Discussion

Returns `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate/takedeformationupdate(id:))*