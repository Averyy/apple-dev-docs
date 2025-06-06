# CIRenderInfo

**Framework**: Core Image  
**Kind**: cl

An encapsulation of a render task's timing, passes, and pixels processed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIRenderInfo : NSObject
```

#### Overview

A [`CIRenderInfo`](cirenderinfo.md) object allows Xcode Quick Look to visualize the render graph with detailed timing information.

## Topics

### Instance Properties
- [var kernelExecutionTime: TimeInterval](cirenderinfo/2875453-kernelexecutiontime.md)
  The amount of time a render spent executing kernels.
- [var passCount: Int](cirenderinfo/2875446-passcount.md)
  The number of passes the render took.
- [var pixelsProcessed: Int](cirenderinfo/2919725-pixelsprocessed.md)
  The number of pixels the render produced executing kernels.
- [var kernelCompileTime: TimeInterval](cirenderinfo/4155584-kernelcompiletime.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [Generating an animation with a Core Image Render Destination](generating_an_animation_with_a_core_image_render_destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task's destination and issuing asynchronous render tasks.
- [class CIRenderTask](cirendertask.md)
  A single render task issued in conjunction with [`CIRenderDestination`](cirenderdestination.md).
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderinfo)*