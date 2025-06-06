# startTask(toClear:)

**Framework**: Core Image  
**Kind**: instm

Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/2875443-alphamode.md).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startTask(toClear destination: CIRenderDestination) throws -> CIRenderTask
```

#### Return_value

The asynchronous [`CIRenderTask`](cirendertask.md) for clearing the destination.

#### Discussion

If the destination's [`alphaMode`](cirenderdestination/2875443-alphamode.md) is [`CIRenderDestinationAlphaMode.none`](cirenderdestinationalphamode/none.md), this command fills the entire destination with black `(0, 0, 0, 1)`.

If the destination's [`alphaMode`](cirenderdestination/2875443-alphamode.md) is [`CIRenderDestinationAlphaMode.premultiplied`](cirenderdestinationalphamode/premultiplied.md) or [`CIRenderDestinationAlphaMode.unpremultiplied`](cirenderdestinationalphamode/unpremultiplied.md), this command fills the entire destination with clear `(0, 0, 0, 0)`.

## Parameters

- `destination`: The   to clear.
- `error`: Pointer to an error object should the task fail.

## See Also

- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint)](cicontext/2875428-preparerender.md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) -> CIRenderTask](cicontext/2875448-starttask.md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) -> CIRenderTask](cicontext/2875429-starttask.md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/2875450-starttask)*