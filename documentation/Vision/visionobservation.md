# VisionObservation

**Framework**: Vision  
**Kind**: protocol

A type for objects produced by image-analysis requests.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol VisionObservation : CustomStringConvertible, Decodable, Encodable, Hashable, Sendable
```

## Topics

### Inspecting an observation
- [var uuid: UUID](visionobservation/uuid.md)
  A unique alphanumeric value that the framework assigns the observation.
- [var confidence: Float](visionobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [var description: String](visionobservation/description.md)
  A textual representation of this instance.
- [var originatingRequestDescriptor: RequestDescriptor?](visionobservation/originatingrequestdescriptor.md)
  The descriptor of the request that produces the observation.
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [var timeRange: CMTimeRange?](visionobservation/timerange.md)
  The time range of the reported observation.
### Hashing the observation
- [func hash(into: inout Hasher)](visionobservation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Hashable Implementations](visionobservation/hashable-implementations.md)

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AnimalBodyPoseObservation](animalbodyposeobservation.md)
- [BarcodeObservation](barcodeobservation.md)
- [ClassificationObservation](classificationobservation.md)
- [ContoursObservation](contoursobservation.md)
- [CoreMLFeatureValueObservation](coremlfeaturevalueobservation.md)
- [DetectedDocumentObservation](detecteddocumentobservation.md)
- [DetectedObjectObservation](detectedobjectobservation.md)
- [DocumentObservation](documentobservation.md)
- [FaceObservation](faceobservation.md)
- [FeaturePrintObservation](featureprintobservation.md)
- [HorizonObservation](horizonobservation.md)
- [HumanBodyPose3DObservation](humanbodypose3dobservation.md)
- [HumanBodyPoseObservation](humanbodyposeobservation.md)
- [HumanHandPoseObservation](humanhandposeobservation.md)
- [HumanObservation](humanobservation.md)
- [ImageAestheticsScoresObservation](imageaestheticsscoresobservation.md)
- [ImageHomographicAlignmentObservation](imagehomographicalignmentobservation.md)
- [ImageTranslationAlignmentObservation](imagetranslationalignmentobservation.md)
- [InstanceMaskObservation](instancemaskobservation.md)
- [OpticalFlowObservation](opticalflowobservation.md)
- [PixelBufferObservation](pixelbufferobservation.md)
- [RecognizedObjectObservation](recognizedobjectobservation.md)
- [RecognizedTextObservation](recognizedtextobservation.md)
- [RectangleObservation](rectangleobservation.md)
- [SaliencyImageObservation](saliencyimageobservation.md)
- [SmudgeObservation](smudgeobservation.md)
- [TextObservation](textobservation.md)
- [TrajectoryObservation](trajectoryobservation.md)

## See Also

- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [protocol StatefulRequest](statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.
- [protocol TargetedRequest](targetedrequest.md)
  A type for analyzing two images together.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionobservation)*