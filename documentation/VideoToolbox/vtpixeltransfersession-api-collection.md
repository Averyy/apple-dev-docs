# VTPixelTransferSession

**Framework**: Video Toolbox

An object converts video data from source pixel buffers to destination pixel buffers.

#### Overview

A pixel transfer session supports the copying and/or conversion of images from source pixel buffers to destination pixel buffers. The basic workflow used when working with a pixel transfer session is as follows:

1. Create a pixel transfer session by calling [`VTPixelTransferSessionCreate(allocator:pixelTransferSessionOut:)`](vtpixeltransfersessioncreate(allocator:pixeltransfersessionout:).md).
2. Optionally, configure the session with your desired [`Pixel Transfer Properties`](pixel-transfer-properties.md) by calling [`VTSessionSetProperty(_:key:value:)`](vtsessionsetproperty(_:key:value:).md) or [`VTSessionSetProperties(_:propertyDictionary:)`](vtsessionsetproperties(_:propertydictionary:).md).
3. Transfer images by calling [`VTPixelTransferSessionTransferImage(_:from:to:)`](vtpixeltransfersessiontransferimage(_:from:to:).md).
4. When you finish with the pixel transfer session, call [`VTPixelTransferSessionInvalidate(_:)`](vtpixeltransfersessioninvalidate(_:).md) to tear it down, and [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to free its memory.

## Topics

### Creating Sessions
- [func VTPixelTransferSessionCreate(allocator: CFAllocator?, pixelTransferSessionOut: UnsafeMutablePointer<VTPixelTransferSession?>) -> OSStatus](vtpixeltransfersessioncreate(allocator:pixeltransfersessionout:).md)
  Creates a session for transferring images between Core Video image buffers that hold pixels in main memory.
### Configuring Sessions
- [Pixel Transfer Properties](pixel-transfer-properties.md)
  Properties used to configure a VideoToolbox pixel transfer session.
### Converting Image Data
- [func VTPixelTransferSessionTransferImage(VTPixelTransferSession, from: CVPixelBuffer, to: CVPixelBuffer) -> OSStatus](vtpixeltransfersessiontransferimage(_:from:to:).md)
  Copies and/or converts an image from one pixel buffer to another.
### Inspecting Sessions
- [func VTPixelTransferSessionGetTypeID() -> CFTypeID](vtpixeltransfersessiongettypeid().md)
  Retrieves the Core Foundation type identifier for the pixel transfer session.
### Ending Sessions
- [func VTPixelTransferSessionInvalidate(VTPixelTransferSession)](vtpixeltransfersessioninvalidate(_:).md)
  Tears down a pixel transfer session.
### Data Types
- [class VTPixelTransferSession](vtpixeltransfersession.md)
  A reference to a VideoToolbox pixel transfer session.

## See Also

- [VTPixelRotationSession](vtpixelrotationsession-api-collection.md)
  An object that rotates source pixel buffers to destination pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixeltransfersession-api-collection)*