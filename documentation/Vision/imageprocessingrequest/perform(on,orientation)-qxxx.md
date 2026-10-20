# perform(on:orientation:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Performs the request on a Core Graphics image and produces observations.

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
func perform(on image: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result
```

#### Return Value

The observation — or list of observations — the request produces.

## Parameters

- `image`: The input [`CGImage`](../../CoreGraphics/cgimage.md) on which to perform the request.
- `orientation`: The orientation of the input image. Default is `nil`.

## Default Implementations

### ImageProcessingRequest Implementations
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-1mquz.md)
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-2q3hx.md)
- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-6hrxe.md)
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-82mjf.md)
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-8wluq.md)
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-967mr.md)

## See Also

### Performing a request
- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./perform%28on,orientation%29-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imageprocessingrequest/perform(on:orientation:)-qxxx)*