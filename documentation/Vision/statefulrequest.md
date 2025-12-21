# StatefulRequest

**Framework**: Vision  
**Kind**: protocol

The protocol for a type that builds evidence of a condition over time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
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
  Returns a Boolean value indicating whether two values are equal.
### Hashing the request
- [func hash(into: inout Hasher)](statefulrequest/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](statefulrequest/equatable-implementations.md)
- [Hashable Implementations](statefulrequest/hashable-implementations.md)

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [protocol TargetedRequest](targetedrequest.md)
  A type for analyzing two images together.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/statefulrequest)*