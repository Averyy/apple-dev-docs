# init(forOfflineGPUAtIndex:)

**Framework**: Core Image  
**Kind**: init

Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init?(forOfflineGPUAt index: UInt32)
```

#### Return Value

A Core Image context.

#### Discussion

GPU devices that are not currently being used to drive a display can be used for Core Image rendering. Use the [`offlineGPUCount()`](cicontext/offlinegpucount().md) method to determine whether any such GPUs are available.

To create a Metal-based Core Image context using an offline GPU, use the [`MTLCopyAllDevices()`](https://developer.apple.com/documentation/Metal/MTLCopyAllDevices()) function to list Metal devices, then choose a device without a display to pass to the [`init(mtlDevice:)`](cicontext/init(mtldevice:).md) method.

## Parameters

- `index`: The index of the offline GPU with which to create the context; a number between zero and the value returned by the   method.

## See Also

- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/init(cglcontext:pixelformat:colorspace:options:).md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](cicontext/init(eaglcontext:).md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](cicontext/init(eaglcontext:options:).md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](cicontext/createcglayer(with:info:).md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](cicontext/draw(_:at:from:).md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(forofflinegpuatindex:))*