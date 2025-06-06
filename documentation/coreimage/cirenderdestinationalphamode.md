# CIRenderDestinationAlphaMode

**Framework**: Core Image  
**Kind**: enum

Different ways of representing alpha.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum CIRenderDestinationAlphaMode : UInt, @unchecked Sendable
```

## Topics

### Enumeration Cases
- [CIRenderDestinationAlphaMode.none](cirenderdestinationalphamode/none.md)
  Designates a destination with no alpha compositing.
- [CIRenderDestinationAlphaMode.premultiplied](cirenderdestinationalphamode/premultiplied.md)
  Designates a destination that expects premultiplied alpha values.
- [CIRenderDestinationAlphaMode.unpremultiplied](cirenderdestinationalphamode/unpremultiplied.md)
  Designates a destination that expects non-premultiplied alpha values.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [Generating an animation with a Core Image Render Destination](generating_an_animation_with_a_core_image_render_destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task's destination and issuing asynchronous render tasks.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task's timing, passes, and pixels processed.
- [class CIRenderTask](cirendertask.md)
  A single render task issued in conjunction with [`CIRenderDestination`](cirenderdestination.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestinationalphamode)*