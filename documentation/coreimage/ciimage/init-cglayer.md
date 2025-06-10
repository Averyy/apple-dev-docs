# init(cgLayer:)

**Framework**: Core Image  
**Kind**: init

Initializes an image object  from the contents supplied by a CGLayer object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init(cgLayer layer: CGLayer)
```

#### Return Value

The initialized image object.

## Parameters

- `layer`: A CGLayer object. For more information see   and  .

## See Also

- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](ciimage/init(cglayer:options:).md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](ciimage/init(texture:size:flipped:colorspace:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/init(texture:size:flipped:options:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](ciimage/init(iosurface:plane:format:options:).md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](ciimageoption/textureformat.md)
  The key for an OpenGL texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(cglayer:))*