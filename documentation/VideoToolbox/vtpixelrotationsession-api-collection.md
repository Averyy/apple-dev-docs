# VTPixelRotationSession

**Framework**: Videotoolbox

An object that rotates source pixel buffers to destination pixel buffers.

#### Overview

To create a rotation session, call [`VTPixelRotationSessionCreate(_:_:)`](vtpixelrotationsessioncreate(_:_:).md). Optionally configure the session by calling [`VTSessionSetProperty(_:key:value:)`](vtsessionsetproperty(_:key:value:).md).

To transfer pixels call [`VTPixelRotationSessionRotateImage(_:_:_:)`](vtpixelrotationsessionrotateimage(_:_:_:).md).

When you’re done with the session, call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to tear it down and release your object reference.

## Topics

### Managing a Session
- [func VTPixelRotationSessionCreate(CFAllocator?, UnsafeMutablePointer<VTPixelRotationSession?>) -> OSStatus](vtpixelrotationsessioncreate(_:_:).md)
  Creates a session to rotate images between pixel buffers.
- [func VTPixelRotationSessionInvalidate(VTPixelRotationSession)](vtpixelrotationsessioninvalidate(_:).md)
  Tears down a pixel rotation session.
### Configuring a Session
- [Pixel Rotation Properties](pixel-rotation-properties.md)
  Properties used to configure a VideoToolbox pixel rotation session.
### Rotating an Image
- [func VTPixelRotationSessionRotateImage(VTPixelRotationSession, CVPixelBuffer, CVPixelBuffer) -> OSStatus](vtpixelrotationsessionrotateimage(_:_:_:).md)
  Rotates a source pixel buffer and writes the output to the destination pixel buffer.
### Inspecting the Type Identifier
- [func VTPixelRotationSessionGetTypeID() -> CFTypeID](vtpixelrotationsessiongettypeid().md)
  Returns the Core Foundation type identifier for the rotation session.
### Data Types
- [class VTPixelRotationSession](vtpixelrotationsession.md)
  A reference to a pixel rotation session.

## See Also

- [VTPixelTransferSession](vtpixeltransfersession-api-collection.md)
  An object converts video data from source pixel buffers to destination pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsession-api-collection)*