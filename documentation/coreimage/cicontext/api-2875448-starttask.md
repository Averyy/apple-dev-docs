# startTask(toRender:from:to:at:)

**Framework**: Core Image  
**Kind**: instm

Renders a portion of an image to a point in the destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startTask(toRender image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws -> CIRenderTask
```

#### Return_value

An asynchronous [`CIRenderTask`](cirendertask.md) to render the image to the specified destination.

#### Discussion

This method crops the image to the specified rectangle and renders the result at the indicated origin point. If the image’s [`extent`](ciimage/1437996-extent.md) property and `fromRect` argument values are infinite, this call renders the image’s (0, 0) point starting from the origin `atPoint`.

You must use an [`MTLTexture`](https://developer.apple.com/documentation/metal/mtltexture)-backed [`CIContext`](cicontext.md) to support an [`MTLTexture`](https://developer.apple.com/documentation/metal/mtltexture)-backed [`CIRenderDestination`](cirenderdestination.md). Similarly, you must use `GLContext`-backed [`CIContext`](cicontext.md) to support a `GLTexture`-backed [`CIRenderDestination`](cirenderdestination.md).

This call returns as soon as it enqueues all work required to render the image on the context’s device. In many situations, after issuing a render, you may need to wait for it to complete. In these cases, use the returned [`CIRenderTask`](cirendertask.md) as follows:

```swift
let renderTask = try context.startTask(toRender: image, from: fromRect, to: destination, at: point)

let renderInfo = try renderTask.waitUntilCompleted()
```

## Parameters

- `image`: A   to render.
- `fromRect`: The part of the image to render, as if cropped.
- `destination`: A   into which to render the image.
- `atPoint`: An origin point in the destination at which to place the image.

## See Also

- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint)](cicontext/2875428-preparerender.md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) -> CIRenderTask](cicontext/2875450-starttask.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/2875443-alphamode.md).
- [func startTask(toRender: CIImage, to: CIRenderDestination) -> CIRenderTask](cicontext/2875429-starttask.md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/2875448-starttask)*