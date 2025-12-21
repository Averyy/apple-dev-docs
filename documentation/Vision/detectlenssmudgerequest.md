# DetectLensSmudgeRequest

**Framework**: Vision  
**Kind**: struct

A request that detects a smudge on a lens from an image or video frame capture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DetectLensSmudgeRequest
```

#### Overview

Use this request to detect whether an image or video is captured with a smudged lens. A smudge is anything that obscures a lens, like a fingerprint or raindrops, resulting in a hazy or blurry capture. Use this capability to find the best frame from a video or set of images.

Perform this request when detecting a smudge within an image or video frame. The request returns a [`SmudgeObservation`](smudgeobservation.md). This observation contains a floating-point [`confidence`](smudgeobservation/confidence.md) value in the range of  `0.0` to `1.0` indicating the probability that a capture has an impaired or smudged lens at capture time. A score of `1.0` represents a high probability the lens is smudged at capture time.

Running [`DetectLensSmudgeRequest`](detectlenssmudgerequest.md) requires a device with A14 Bionic and later or device with M1 and later.

> **Note**: Certain types of content may be categorized as a smudge, such as naturally-blurred objects, long exposure, and motion blur while taking a photo. Make sure that you are using a request on a fixed capture where the device is stable when taking the image.

To use the properties of the request, add a [`ImageProcessingRequest`](imageprocessingrequest.md) to your chosen capture type.

```swift
func isGoodCapture(imageURL:URL) async throws -> Bool {
   
   // Set an optional threshold from 0.0 to 1.0 to flag a maximum level of smudge in your capture.
    let smudgeThreshold: Float = 0.9;
    let request = DetectLensSmudgeRequest(.revision1)
    let smudgeObservation = try await request.perform(on: imageURL)
    
    return (smudgeObservation.confidence < smudgeThreshold)
}
```

## Topics

### Creating a request
- [init(DetectLensSmudgeRequest.Revision?)](detectlenssmudgerequest/init(_:).md)
  Creates a request to detect whether the camera lens has a smudge.
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
### Understanding the result
- [struct SmudgeObservation](smudgeobservation.md)
  An observation that provides an overall score of the presence of a smudge in an image or video frame capture.
### Configuring a request
- [var cropAndScaleAction: ImageCropAndScaleAction](detectlenssmudgerequest/cropandscaleaction.md)
  An optional setting that tells the algorithm how to scale an input image before generating the result.
- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.
### Getting the revision
- [let revision: DetectLensSmudgeRequest.Revision](detectlenssmudgerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static var supportedRevisions: [DetectLensSmudgeRequest.Revision]](detectlenssmudgerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectLensSmudgeRequest.Revision](detectlenssmudgerequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionRequest](visionrequest.md)

## See Also

- [Generating high-quality thumbnails from videos](generating-thumbnails-from-videos.md)
  Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.
- [struct CalculateImageAestheticsScoresRequest](calculateimageaestheticsscoresrequest.md)
  A request that analyzes an image for aesthetically pleasing attributes.
- [struct GenerateAttentionBasedSaliencyImageRequest](generateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [struct GenerateObjectnessBasedSaliencyImageRequest](generateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectlenssmudgerequest)*