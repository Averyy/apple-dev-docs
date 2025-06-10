# textureFormat

**Framework**: Core Image  
**Kind**: property

The key for an OpenGL texture format.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static let textureFormat: CIImageOption
```

#### Discussion

The value for this key must be an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Core Image pixel format constant. (See `Pixel Formats`.) You may only use this key when initializing an image using the [`init(texture:size:flipped:options:)`](ciimage/init(texture:size:flipped:options:).md) method.

## See Also

- [init(cgLayer: CGLayer)](ciimage/init(cglayer:).md)
  Initializes an image object  from the contents supplied by a CGLayer object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/textureformat)*