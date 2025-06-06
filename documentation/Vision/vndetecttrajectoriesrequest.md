# VNDetectTrajectoriesRequest

**Framework**: Vision  
**Kind**: class

A request that detects the trajectories of shapes moving along a parabolic path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectTrajectoriesRequest
```

## Mentions

- [Identifying Trajectories in Video](identifying-trajectories-in-video.md)

#### Overview

After the request detects a trajectory, it produces an observation that contains the shape’s detected points and an equation describing the parabola.

## Topics

### Creating a Request
- [init(frameAnalysisSpacing: CMTime, trajectoryLength: Int, completionHandler: VNRequestCompletionHandler?)](vndetecttrajectoriesrequest/init(frameanalysisspacing:trajectorylength:completionhandler:).md)
  Creates a new request to detect trajectories.
### Configuring the Request
- [var targetFrameTime: CMTime](vndetecttrajectoriesrequest/targetframetime.md)
  The requested target frame time for processing trajectory detection.
- [var trajectoryLength: Int](vndetecttrajectoriesrequest/trajectorylength.md)
  The number of points to detect before calculating a trajectory.
- [var objectMinimumNormalizedRadius: Float](vndetecttrajectoriesrequest/objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [var objectMaximumNormalizedRadius: Float](vndetecttrajectoriesrequest/objectmaximumnormalizedradius.md)
  The maximum radius of the bounding circle of the object to track.
- [var minimumObjectSize: Float](vndetecttrajectoriesrequest/minimumobjectsize.md)
  The minimum radius of the tracked shape’s bounding circle.
- [var maximumObjectSize: Float](vndetecttrajectoriesrequest/maximumobjectsize.md)
  The maximum radius of the tracked shape’s bounding circle.
### Inspecting the Results
- [var results: [VNTrajectoryObservation]?](vndetecttrajectoriesrequest/results.md)
  The array of detected trajectory observations.
- [class VNTrajectoryObservation](vntrajectoryobservation.md)
  An observation that describes a detected trajectory.
### Identifying Request Revisions
- [let VNDetectTrajectoriesRequestRevision1: Int](vndetecttrajectoriesrequestrevision1.md)
  A constant for specifying revision 1 of the trajectories detection request.

## Relationships

### Inherits From
- [VNStatefulRequest](vnstatefulrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying Trajectories in Video](identifying-trajectories-in-video.md)
  Gain new insights into your video data by using Vision to detect trajectories.
- [Detecting moving objects in a video](detecting-moving-objects-in-a-video.md)
  Identify the trajectory of a thrown object by using Vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttrajectoriesrequest)*