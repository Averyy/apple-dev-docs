# VTPixelTransferSessionTransferImage(_:from:to:)

**Framework**: Videotoolbox  
**Kind**: func

Copies and/or converts an image from one pixel buffer to another.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.8+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func VTPixelTransferSessionTransferImage(_ session: VTPixelTransferSession, from sourceBuffer: CVPixelBuffer, to destinationBuffer: CVPixelBuffer) -> OSStatus
```

#### Return Value

`noErr` if successful or an error code, such as `kVTPixelTransferNotSupportedErr`, if the operation failed.

#### Discussion

By default, the full width and height of `sourceBuffer` are scaled to the full width and height of `destinationBuffer`.   By default, all existing attachments on `destinationBuffer` are removed and new attachments are set that describe the transferred image.  Unrecognized attachments on `sourceBuffer` are propagated to destinationBuffer. Some properties modify this behavior; see `VTPixelTransferProperties.h` for more details.

## Parameters

- `session`: The pixel transfer session.
- `sourceBuffer`: The source buffer.
- `destinationBuffer`: The destination buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixeltransfersessiontransferimage(_:from:to:))*