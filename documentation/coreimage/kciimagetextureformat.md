# textureFormat

**Framework**: Core Image  
**Kind**: structdata

The key for an OpenGL texture format.

**Availability**:
- macOS 10.9+ - Deprecated in 10.14

## Declaration

```swift
static let textureFormat: CIImageOption
```

#### Discussion

The value for this key must be an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Core Image pixel format constant. (See `Pixel Formats`.) You may only use this key when initializing an image using the [`init(texture:size:flipped:options:)`](ciimage/1437880-init.md) method.

## See Also

- [init(cgLayer: CGLayer)](ciimage/1438065-init.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](ciimage/1437687-init.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](ciimage/1438015-init.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/1437880-init.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](ciimage/1437670-init.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](ciimageoption/1437613-texturetarget.md)
  The key for an OpenGL texture target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kciimagetextureformat)*