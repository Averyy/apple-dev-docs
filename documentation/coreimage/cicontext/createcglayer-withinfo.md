# createCGLayer(with:info:)

**Framework**: Core Image  
**Kind**: method

Creates a CGLayer object from the provided parameters.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func createCGLayer(with size: CGSize, info: CFDictionary?) -> CGLayer?
```

#### Return Value

A CGLayer object.

#### Discussion

After calling this method, Core Image draws content into the CGLayer object. Core Image creates a CGLayer object by calling the Quartz 2D function [`init(_:size:auxiliaryInfo:)`](https://developer.apple.com/documentation/CoreGraphics/CGLayer/init(_:size:auxiliaryInfo:)), whose prototype is:

```objc
CGLayerRef CGLayerCreateWithContext (
   CGContextRef context,
   CGSize size,
   CFDictionaryRef auxiliaryInfo
);
```

Core Image passes the [`CIContext`](cicontext.md) object as the `context` parameter, the size as the `size` parameter, and the dictionary as the `auxiliaryInfo` parameter. For more information on CGLayer objects, see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGLayer`](https://developer.apple.com/documentation/CoreGraphics/CGLayer).

## Parameters

- `size`: The size, in default user space units, of the layer relative to the graphics context.
- `info`: A dictionary, which is passed to   as the   parameter. Pass   because this parameter is reserved for future use.

## See Also

- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/init(cglcontext:pixelformat:colorspace:options:).md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](cicontext/init(eaglcontext:).md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](cicontext/init(eaglcontext:options:).md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAtIndex: UInt32)](cicontext/init(forofflinegpuatindex:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func draw(CIImage, at: CGPoint, from: CGRect)](cicontext/draw(_:at:from:).md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/createcglayer(with:info:))*