# VTCreateCGImageFromCVPixelBuffer(_:options:imageOut:)

**Framework**: Videotoolbox  
**Kind**: func

Creates a Core Graphics bitmap image or image mask using the provided pixel buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCreateCGImageFromCVPixelBuffer(_ pixelBuffer: CVPixelBuffer, options: CFDictionary?, imageOut: UnsafeMutablePointer<CGImage?>) -> OSStatus
```

#### Discussion

This routine creates a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) representation of the image data contained in the provided [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer). The source `CVPixelBuffer` may be retained for the lifetime of the `CGImage`. Changes to the `CVPixelBuffer` after making this call (other than releasing it) will have undefined results.

Not all `CVPixelBuffer` pixel formats support conversion into a `CGImage-`compatible pixel format.

## Parameters

- `pixelBuffer`: A pixel buffer to use as the image data source for the  .
- `options`: No options are currently supported. Pass   for this argument.
- `imageOut`: Pointer to an address to receive the newly created  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcreatecgimagefromcvpixelbuffer(_:options:imageout:))*