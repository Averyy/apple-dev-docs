# startTask(toClear:)

**Framework**: Core Image  
**Kind**: method

Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/alphamode.md).

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

#### Return Value

The asynchronous [`CIRenderTask`](cirendertask.md) for clearing the destination.

#### Discussion

If the destination’s [`alphaMode`](cirenderdestination/alphamode.md) is [`CIRenderDestinationAlphaMode.none`](cirenderdestinationalphamode/none.md), this command fills the entire destination with black `(0, 0, 0, 1)`.

If the destination’s [`alphaMode`](cirenderdestination/alphamode.md) is [`CIRenderDestinationAlphaMode.premultiplied`](cirenderdestinationalphamode/premultiplied.md) or [`CIRenderDestinationAlphaMode.unpremultiplied`](cirenderdestinationalphamode/unpremultiplied.md), this command fills the entire destination with clear `(0, 0, 0, 0)`.

## Parameters

- `destination`: The   to clear.

## See Also

- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws](cicontext/preparerender(_:from:to:at:).md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](cicontext/starttask(torender:from:to:at:).md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) throws -> CIRenderTask](cicontext/starttask(torender:to:).md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/starttask(toclear:))*