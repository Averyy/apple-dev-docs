# VNStatefulRequest

**Framework**: Vision  
**Kind**: class

An abstract request type that builds evidence of a condition over time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNStatefulRequest
```

## Topics

### Initializing a Request
- [init(frameAnalysisSpacing: CMTime, completionHandler: VNRequestCompletionHandler?)](vnstatefulrequest/init(frameanalysisspacing:completionhandler:).md)
  Initializes a video-based request.
### Configuring the Request
- [var minimumLatencyFrameCount: Int](vnstatefulrequest/minimumlatencyframecount.md)
  The minimum number of frames a request processes before reporting an observation.
- [var frameAnalysisSpacing: CMTime](vnstatefulrequest/frameanalysisspacing.md)
  A time value that indicates the interval between analysis operations.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Inherited By
- [VNDetectHumanBodyPose3DRequest](vndetecthumanbodypose3drequest.md)
- [VNDetectTrajectoriesRequest](vndetecttrajectoriesrequest.md)
- [VNGeneratePersonSegmentationRequest](vngeneratepersonsegmentationrequest.md)
- [VNTrackHomographicImageRegistrationRequest](vntrackhomographicimageregistrationrequest.md)
- [VNTrackOpticalFlowRequest](vntrackopticalflowrequest.md)
- [VNTrackTranslationalImageRegistrationRequest](vntracktranslationalimageregistrationrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Applying Matte Effects to People in Images and Video](applying-matte-effects-to-people-in-images-and-video.md)
  Generate image masks for people automatically by using semantic person-segmentation.
- [Detecting human actions in a live video feed](../CreateML/detecting-human-actions-in-a-live-video-feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [Segmenting and colorizing individuals from a surrounding scene](segmenting-and-colorizing-individuals-from-a-surrounding-scene.md)
  Use the Vision framework to isolate and apply colors to people in an image.
- [class VNGeneratePersonSegmentationRequest](vngeneratepersonsegmentationrequest.md)
  An object that produces a matte image for a person it finds in the input image.
- [class VNGeneratePersonInstanceMaskRequest](vngeneratepersoninstancemaskrequest.md)
  An object that produces a mask of individual people it finds in the input image.
- [class VNDetectDocumentSegmentationRequest](vndetectdocumentsegmentationrequest.md)
  An object that detects rectangular regions that contain text in the input image.
- [class VNSequenceRequestHandler](vnsequencerequesthandler.md)
  An object that processes image-analysis requests for each frame in a sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnstatefulrequest)*