# CIRenderDestination

**Framework**: Core Image  
**Kind**: class

A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIRenderDestination
```

#### Overview

The `CIRenderDestination` class provides an API for specifying a render task destination’s properties, such as buffer format, alpha mode, clamping behavior, blending, and color space, properties formerly tied to [`CIContext`](cicontext.md).

You can create a `CIRenderDestination` object for each surface or buffer to which you must render. You can also render multiple times to a single destination with different settings such as colorspace and blend mode by mutating a single `CIRenderDestination` object between renders.

Renders issued to a `CIRenderDestination` return to the caller as soon as the CPU has issued the task, rather than after the GPU has performed the task, so you can start render tasks on subsequent frames without waiting for previous renders to finish. If the render fails, a [`CIRenderTask`](cirendertask.md) will return immediately.

## Topics

### Creating a Render Destination
- [init(pixelBuffer: CVPixelBuffer)](cirenderdestination/init(pixelbuffer:).md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](cirenderdestination/init(iosurface:).md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](cirenderdestination/init(mtltexture:commandbuffer:).md)
  Creates a render destination based on a Metal texture.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:).md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](cirenderdestination/init(gltexture:target:width:height:).md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:).md)
  Creates a render destination based on a client-managed buffer.
### Customizing Rendering
- [var alphaMode: CIRenderDestinationAlphaMode](cirenderdestination/alphamode.md)
  The render destination’s representation of alpha (transparency) values.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.
- [var blendKernel: CIBlendKernel?](cirenderdestination/blendkernel.md)
  The destination’s blend kernel.
- [var blendsInDestinationColorSpace: Bool](cirenderdestination/blendsindestinationcolorspace.md)
  Indicator of whether to blend in the destination’s color space.
- [var colorSpace: CGColorSpace?](cirenderdestination/colorspace.md)
  The destination’s color space.
- [var width: Int](cirenderdestination/width.md)
  The render destination’s row width.
- [var height: Int](cirenderdestination/height.md)
  The render destination’s buffer height.
- [var isClamped: Bool](cirenderdestination/isclamped.md)
  Indicator of whether or not the destination clamps.
- [var isDithered: Bool](cirenderdestination/isdithered.md)
  Indicator of whether or not the destination dithers.
- [var isFlipped: Bool](cirenderdestination/isflipped.md)
  Indicator of whether the destination is flipped.
### Instance Properties
- [var captureTraceURL: URL?](cirenderdestination/capturetraceurl.md)
  Tell the next using this destination to capture a Metal trace.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task’s timing, passes, and pixels processed.
- [class CIRenderTask](cirendertask.md)
  A single render task.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination)*