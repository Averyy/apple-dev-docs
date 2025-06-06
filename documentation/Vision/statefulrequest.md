# StatefulRequest

**Framework**: Vision  
**Kind**: protocol

The protocol for a type that builds evidence of a condition over time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol StatefulRequest : VisionRequest
```

## Topics

### Inspecting the request
- [var frameAnalysisSpacing: CMTime](statefulrequest/frameanalysisspacing.md)
  The reciprocal of the maximum rate to process buffers.
- [var minimumLatencyFrameCount: Int](statefulrequest/minimumlatencyframecount.md)
  The minimum number of frames that the request has to process before reporting any observations.
### Comparing the request
- [static func == (Self, Self) -> Bool](statefulrequest/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Hashing the request
- [func hash(into: inout Hasher)](statefulrequest/hash(into:).md)
  Hashes the essential components of the value by passing them into the hasher.
### Default Implementations
- [Equatable Implementations](statefulrequest/equatable-implementations.md)
- [Hashable Implementations](statefulrequest/hashable-implementations.md)

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [VisionRequest](visionrequest.md)
### Conforming Types
- [DetectHumanBodyPose3DRequest](detecthumanbodypose3drequest.md)
- [DetectTrajectoriesRequest](detecttrajectoriesrequest.md)
- [GeneratePersonSegmentationRequest](generatepersonsegmentationrequest.md)
- [TrackHomographicImageRegistrationRequest](trackhomographicimageregistrationrequest.md)
- [TrackObjectRequest](trackobjectrequest.md)
- [TrackOpticalFlowRequest](trackopticalflowrequest.md)
- [TrackRectangleRequest](trackrectanglerequest.md)
- [TrackTranslationalImageRegistrationRequest](tracktranslationalimageregistrationrequest.md)

## See Also

- [class GeneratePersonSegmentationRequest](generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.
- [struct GeneratePersonInstanceMaskRequest](generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [struct DetectDocumentSegmentationRequest](detectdocumentsegmentationrequest.md)
  A request that detects rectangular regions that contain text in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/statefulrequest)*