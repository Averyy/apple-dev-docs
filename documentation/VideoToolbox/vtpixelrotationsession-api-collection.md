# VTPixelRotationSession

**Framework**: Video Toolbox  
**Role**: API Collection

An object that rotates source pixel buffers to destination pixel buffers.

## Overview

To create a rotation session, call [`VTPixelRotationSessionCreate(_:_:)`](./vtpixelrotationsessioncreate%28_,_%29.md). Optionally configure the session by calling [`VTSessionSetProperty(_:key:value:)`](./vtsessionsetproperty%28_,key,value%29.md).

To transfer pixels call [`VTPixelRotationSessionRotateImage(_:_:_:)`](./vtpixelrotationsessionrotateimage%28_,_,_%29.md).

When you’re done with the session, call [`CFRelease`](../CoreFoundation/cfrelease.md) to tear it down and release your object reference.

## Topics

### Managing a Session
- [func VTPixelRotationSessionCreate(CFAllocator?, UnsafeMutablePointer<VTPixelRotationSession?>) -> OSStatus](./vtpixelrotationsessioncreate%28_,_%29.md)
  Creates a session to rotate images between pixel buffers.
- [func VTPixelRotationSessionInvalidate(VTPixelRotationSession)](./vtpixelrotationsessioninvalidate%28_%29.md)
  Tears down a pixel rotation session.
### Configuring a Session
- [Pixel Rotation Properties](./pixel-rotation-properties.md)
  Properties used to configure a VideoToolbox pixel rotation session.
### Rotating an Image
- [func VTPixelRotationSessionRotateImage(VTPixelRotationSession, CVPixelBuffer, CVPixelBuffer) -> OSStatus](./vtpixelrotationsessionrotateimage%28_,_,_%29.md)
  Rotates a source pixel buffer and writes the output to the destination pixel buffer.
### Inspecting the Type Identifier
- [func VTPixelRotationSessionGetTypeID() -> CFTypeID](./vtpixelrotationsessiongettypeid%28%29.md)
  Returns the Core Foundation type identifier for the rotation session.
### Data Types
- [class VTPixelRotationSession](./vtpixelrotationsession.md)
  A reference to a pixel rotation session.

## See Also

### Transformation
- [VTPixelTransferSession](./vtpixeltransfersession-api-collection.md)
  An object converts video data from source pixel buffers to destination pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsession-api-collection)*