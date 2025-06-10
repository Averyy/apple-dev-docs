# startTask(toRender:to:)

**Framework**: Core Image  
**Kind**: method

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

#### Return Value

The asynchronous [`CIRenderTask`](cirendertask.md) to render the image to the specified destination.

## Parameters

- `image`:   to prepare to render.
- `destination`: The   to which to render.

## See Also

- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws](cicontext/preparerender(_:from:to:at:).md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) throws -> CIRenderTask](cicontext/starttask(toclear:).md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](cicontext/starttask(torender:from:to:at:).md)
  Renders a portion of an image to a point in the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/starttask(torender:to:))*