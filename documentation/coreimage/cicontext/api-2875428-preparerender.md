# prepareRender(_:from:to:at:)

**Framework**: Core Image  
**Kind**: instm

An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func prepareRender(_ image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws
```

#### Return_value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if preparation succeeded.

#### Discussion

By making this call, the Core Image framework ensures that any needed kernels are compiled, and any intermediate buffers are allocated and marked volatile up front.

## Parameters

- `image`:  to prepare to render.
- `fromRect`: A   defining the region to render.
- `destination`: The   to which you are preparing to render.
- `atPoint`: The   at which you are preparing to render.
- `error`: Pointer to an error should preparation to render fail.

## See Also

- [func startTask(toClear: CIRenderDestination) -> CIRenderTask](cicontext/2875450-starttask.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/2875443-alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) -> CIRenderTask](cicontext/2875448-starttask.md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) -> CIRenderTask](cicontext/2875429-starttask.md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/2875428-preparerender)*