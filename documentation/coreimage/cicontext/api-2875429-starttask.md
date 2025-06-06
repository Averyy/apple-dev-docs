# startTask(toRender:to:)

**Framework**: Core Image  
**Kind**: instm

Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startTask(toRender image: CIImage, to destination: CIRenderDestination) throws -> CIRenderTask
```

#### Return_value

The asynchronous [`CIRenderTask`](cirendertask.md) to render the image to the specified destination.

## Parameters

- `image`:  to prepare to render.
- `destination`: The   to which to render.
- `error`: Pointer to an error should the render task creation fail.

## See Also

- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint)](cicontext/2875428-preparerender.md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) -> CIRenderTask](cicontext/2875450-starttask.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/2875443-alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) -> CIRenderTask](cicontext/2875448-starttask.md)
  Renders a portion of an image to a point in the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/2875429-starttask)*