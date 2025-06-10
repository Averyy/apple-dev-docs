# CIRenderInfo

**Framework**: Core Image  
**Kind**: class

An encapsulation of a render task’s timing, passes, and pixels processed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIRenderInfo
```

#### Overview

A `CIRenderInfo` object allows Xcode Quick Look to visualize the render graph with detailed timing information.

## Topics

### Instance Properties
- [var kernelExecutionTime: TimeInterval](cirenderinfo/kernelexecutiontime.md)
  The amount of time a render spent executing kernels.
- [var passCount: Int](cirenderinfo/passcount.md)
  The number of passes the render took.
- [var pixelsProcessed: Int](cirenderinfo/pixelsprocessed.md)
  The number of pixels the render produced executing kernels.
- [var kernelCompileTime: TimeInterval](cirenderinfo/kernelcompiletime.md)

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
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [class CIRenderTask](cirendertask.md)
  A single render task.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderinfo)*