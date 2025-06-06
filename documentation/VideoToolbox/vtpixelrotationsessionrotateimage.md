# VTPixelRotationSessionRotateImage(_:_:_:)

**Framework**: Videotoolbox  
**Kind**: func

Rotates a source pixel buffer and writes the output to the destination pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func VTPixelRotationSessionRotateImage(_ session: VTPixelRotationSession, _ sourceBuffer: CVPixelBuffer, _ destinationBuffer: CVPixelBuffer) -> OSStatus
```

#### Discussion

For 90 and 270 degree rotations, the width and height of destination must be the inverse of the source buffer.

For 180 degree rotations, the dimensions of the source and destination buffers must match.

By default, this operation removes all existing attachments on destination buffer and sets new attachments describing the transferred image. This function propagates unrecognized attachment on the source to the destination buffer.

## Parameters

- `session`: The pixel rotation session.
- `sourceBuffer`: A pixel buffer that contains the source image.
- `destinationBuffer`: A pixel buffer into which to write the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsessionrotateimage(_:_:_:))*