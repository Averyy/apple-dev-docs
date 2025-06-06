# CIRenderTask

**Framework**: Core Image  
**Kind**: cl

A single render task issued in conjunction with [`CIRenderDestination`](cirenderdestination.md).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIRenderTask : NSObject
```

#### Overview

A [`CIRenderTask`](cirendertask.md) object appears in Xcode Quick Look as a graph.

## Topics

### Instance Methods
- [func waitUntilCompleted() -> CIRenderInfo](cirendertask/2881294-waituntilcompleted.md)
  Waits until the [`CIRenderTask`](cirendertask.md) finishes and returns.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [Generating an animation with a Core Image Render Destination](generating_an_animation_with_a_core_image_render_destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task's destination and issuing asynchronous render tasks.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task's timing, passes, and pixels processed.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirendertask)*