# TargetedRequest

**Framework**: Vision  
**Kind**: protocol

A type for analyzing two images together.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol TargetedRequest : VisionRequest
```

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [VisionRequest](visionrequest.md)
### Conforming Types
- [TrackHomographicImageRegistrationRequest](trackhomographicimageregistrationrequest.md)
- [TrackOpticalFlowRequest](trackopticalflowrequest.md)
- [TrackTranslationalImageRegistrationRequest](tracktranslationalimageregistrationrequest.md)

## See Also

- [class TrackTranslationalImageRegistrationRequest](tracktranslationalimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the affine transform necessary to align the content of two images.
- [class TrackHomographicImageRegistrationRequest](trackhomographicimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the perspective warp matrix necessary to align the content of two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/targetedrequest)*