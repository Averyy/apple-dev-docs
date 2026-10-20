# TargetedRequest

**Framework**: Vision  
**Kind**: protocol  
**Role**: Protocol

A type for analyzing two images together.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
protocol TargetedRequest : VisionRequest
```

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionRequest](./visionrequest.md)
### Conforming Types
- [TrackHomographicImageRegistrationRequest](./trackhomographicimageregistrationrequest.md)
- [TrackOpticalFlowRequest](./trackopticalflowrequest.md)
- [TrackTranslationalImageRegistrationRequest](./tracktranslationalimageregistrationrequest.md)

## See Also

### Protocols
- [protocol ImageProcessingRequest](./imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [protocol PoseProviding](./poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [protocol StatefulRequest](./statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.
- [protocol VisionObservation](./visionobservation.md)
  A type for objects produced by image-analysis requests.
- [protocol VisionRequest](./visionrequest.md)
  A type for image-analysis requests.
- [protocol DownloadableAssetsRequest](./downloadableassetsrequest.md)
  A request whose execution depends on assets that may need to be downloaded.
- [enum DownloadableAssetsRequestStatus](./downloadableassetsrequeststatus.md)
  The status of the assets required by a [`DownloadableAssetsRequest`](./downloadableassetsrequest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/targetedrequest)*