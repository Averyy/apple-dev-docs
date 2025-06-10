# draw(_:in:from:)

**Framework**: Core Image  
**Kind**: method

Renders a region of an image to a rectangle in the context destination.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func draw(_ image: CIImage, in inRect: CGRect, from fromRect: CGRect)
```

#### Discussion

In iOS, this method draws the `CIImage` object into a renderbuffer for the OpenGL ES context. Use this method only if the [`CIContext`](cicontext.md) object is created with `contextWithEAGLContext:`  and if you are rendering to a CAEAGLayer. This method is asynchronous for apps linked against the iOS 6 or later SDK.

In macOS, you need to be aware of whether the [`CIContext`](cicontext.md) object is created with a `CGContextRef` or a `CGLContext` object. If you create the [`CIContext`](cicontext.md) object with a `CGContextRef`, the dimensions of the destination rectangle are in points. If you create the [`CIContext`](cicontext.md) object with a `CGLContext` object, the dimensions are in pixels.

## Parameters

- `image`: A Core Image image object.
- `inRect`: The rectangle in the context destination to draw into. The image is scaled to fill the destination rectangle.
- `fromRect`: The subregion of the image that you want to draw into the context, with the origin and target size defined by the   parameter. This rectangle is always in pixel dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/draw(_:in:from:))*