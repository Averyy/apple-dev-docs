# TrackOpticalFlowRequest

**Framework**: Vision  
**Kind**: class

A request that determines the direction change of vectors for each pixel from a previous to current image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class TrackOpticalFlowRequest
```

#### Overview

This request generates an [`OpticalFlowObservation`](opticalflowobservation.md) object that describes the directional change from image to image. The request works at the pixel level, so both images needs to have the same dimensions to successfully perform the request.

> ❗ **Important**:  Optical flow requests are very resource intensive, so perform only one request at a time. Release memory immediately after generating an optical flow.

## Topics

### Creating a request
- [init(TrackOpticalFlowRequest.Revision?, frameAnalysisSpacing: CMTime?)](trackopticalflowrequest/init(_:frameanalysisspacing:).md)
  Creates an optical-flow tracking request.
### Getting the revision
- [let revision: TrackOpticalFlowRequest.Revision](trackopticalflowrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [TrackOpticalFlowRequest.Revision]](trackopticalflowrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [TrackOpticalFlowRequest.Revision](trackopticalflowrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var computationAccuracy: TrackOpticalFlowRequest.ComputationAccuracy](trackopticalflowrequest/computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [TrackOpticalFlowRequest.ComputationAccuracy](trackopticalflowrequest/computationaccuracy-swift.enum.md)
  A type that describes the computational accuracy.
- [var outputPixelFormatType: OSType](trackopticalflowrequest/outputpixelformattype.md)
  The desired pixel format type of the observation.
- [var supportedOutputPixelFormatTypes: [OSType]](trackopticalflowrequest/supportedoutputpixelformattypes.md)
  The collection of supported pixel format types.
### Performing a request
- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.
- [struct OpticalFlowObservation](opticalflowobservation.md)
  An object that represents an optical flow that an image-analysis request produces.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StatefulRequest](statefulrequest.md)
- [TargetedRequest](targetedrequest.md)
- [VisionRequest](visionrequest.md)

## See Also

- [struct DetectRectanglesRequest](detectrectanglesrequest.md)
  An image-analysis request that finds projected rectangular regions in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackopticalflowrequest)*