# createCGLayer(with:info:)

**Framework**: Core Image  
**Kind**: instm

Creates a CGLayer object from the provided parameters.

**Availability**:
- macOS 10.4+ - Deprecated in 10.11

## Declaration

```swift
func createCGLayer(with size: CGSize, info: CFDictionary?) -> CGLayer?
```

#### Return_value

A CGLayer object. 

#### Discussion

After calling this method, Core Image draws content into the CGLayer object. Core Image creates a CGLayer object by calling the Quartz 2D function [`init(_:size:auxiliaryInfo:)`](https://developer.apple.com/documentation/coregraphics/cglayer/init(_:size:auxiliaryinfo:)), whose prototype is:

```occ
CGLayerRef CGLayerCreateWithContext (
   CGContextRef context,
   CGSize size,
   CFDictionaryRef auxiliaryInfo
);
```

Core Image passes the [`CIContext`](cicontext.md) object as the `context` parameter, the size as the `size` parameter, and the dictionary as the `auxiliaryInfo` parameter. For more information on CGLayer objects, see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and `CGLayer`.

## Parameters

- `size`: The size, in default user space units, of the layer relative to the graphics context.
- `d`: A dictionary, which is passed to   as the   parameter. Pass   because this parameter is reserved for future use.

## See Also

- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/1438137-init.md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](cicontext/1620419-init.md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](cicontext/1620362-init.md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAt: UInt32)](cicontext/1437772-init.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAt: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/1437758-init.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [+ imageWithCGLayer:](ciimage/1547022-imagewithcglayer.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.
- [+ imageWithCGLayer:options:](ciimage/1546998-imagewithcglayer.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1438267-createcglayer)*