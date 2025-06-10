# init(eaglContext:options:)

**Framework**: Core Image  
**Kind**: init

Creates a Core Image context from an EAGL context using the specified options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS ?+

## Declaration

```swift
init(eaglContext: EAGLContext, options: [CIContextOption : Any]? = nil)
```

#### Return Value

A Core Image context that targets OpenGL ES.

#### Discussion

The OpenGL ES context must support OpenGL ES 2.0. All drawing performed using the methods listed in Drawing Images is rendered directly into the context.

## Parameters

- `eaglContext`: The EAGL context to render to.
- `options`: A dictionary that contains options for creating a   object. You can pass any of the keys defined in   along with the appropriate value.

## See Also

- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/init(cglcontext:pixelformat:colorspace:options:).md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](cicontext/init(eaglcontext:).md)
  Creates a Core Image context from an EAGL context.
- [init?(forOfflineGPUAtIndex: UInt32)](cicontext/init(forofflinegpuatindex:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](cicontext/createcglayer(with:info:).md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](cicontext/draw(_:at:from:).md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(eaglcontext:options:))*