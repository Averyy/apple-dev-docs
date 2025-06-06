# CIRenderDestination

**Framework**: Core Image  
**Kind**: cl

A specification for configuring all attributes of a render task's destination and issuing asynchronous render tasks.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIRenderDestination : NSObject
```

#### Overview

The [`CIRenderDestination`](cirenderdestination.md) class provides an API for specifying a render task destination's properties, such as buffer format, alpha mode, clamping behavior, blending, and color space, properties formerly tied to [`CIContext`](cicontext.md).  

You can create a [`CIRenderDestination`](cirenderdestination.md) object for each surface or buffer to which you must render. You can also render multiple times to a single destination with different settings such as colorspace and blend mode by mutating a single [`CIRenderDestination`](cirenderdestination.md) object between renders.

Renders issued to a [`CIRenderDestination`](cirenderdestination.md) return to the caller as soon as the CPU has issued the task, rather than after the GPU has performed the task, so you can start render tasks on subsequent frames without waiting for previous renders to finish. If the render fails, a [`CIRenderTask`](cirendertask.md) will return immediately.

## Topics

### Creating a Render Destination
- [init(pixelBuffer: CVPixelBuffer)](cirenderdestination/2875436-init.md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](cirenderdestination/2876044-init.md)
  Creates a render destination based on an [`IOSurface`](https://developer.apple.com/documentation/iosurface/iosurface) object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](cirenderdestination/2880273-init.md)
  Creates a render destination based on a Metal texture.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](cirenderdestination/2880274-init.md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](cirenderdestination/2875438-init.md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](cirenderdestination/2875427-init.md)
  Creates a render destination based on a client-managed buffer.
### Customizing Rendering
- [var alphaMode: CIRenderDestinationAlphaMode](cirenderdestination/2875443-alphamode.md)
  The render destination's representation of alpha (transparency) values.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.
- [var blendKernel: CIBlendKernel?](cirenderdestination/2875452-blendkernel.md)
  The destination's blend kernel.
- [var blendsInDestinationColorSpace: Bool](cirenderdestination/2875437-blendsindestinationcolorspace.md)
  Indicator of whether to blend in the destination's color space.
- [var colorSpace: CGColorSpace?](cirenderdestination/2875439-colorspace.md)
  The destination's color space.
- [var width: Int](cirenderdestination/2875434-width.md)
  The render destination's row width.
- [var height: Int](cirenderdestination/2875433-height.md)
  The render destination's buffer height.
- [var isClamped: Bool](cirenderdestination/2875451-isclamped.md)
  Indicator of whether or not the destination clamps.
- [var isDithered: Bool](cirenderdestination/2875441-isdithered.md)
  Indicator of whether or not the destination dithers.
- [var isFlipped: Bool](cirenderdestination/2875442-isflipped.md)
  Indicator of whether the destination is flipped.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [Generating an animation with a Core Image Render Destination](generating_an_animation_with_a_core_image_render_destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task's timing, passes, and pixels processed.
- [class CIRenderTask](cirendertask.md)
  A single render task issued in conjunction with [`CIRenderDestination`](cirenderdestination.md).
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination)*