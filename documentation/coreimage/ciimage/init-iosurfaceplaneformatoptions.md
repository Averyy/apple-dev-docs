# init(ioSurface:plane:format:options:)

**Framework**: Core Image  
**Kind**: init

Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init(ioSurface surface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]? = nil)
```

#### Return Value

An image object initialized with the data from the IOSurface.

## Parameters

- `surface`: An IOSurface object.
- `plane`: The index of the data plane in the IOSurface object containing bitmap data for initializing the image.
- `format`: A pixel format constant. See  .
- `options`: A dictionary specifying image options. (See  .)

## See Also

- [init(cgLayer: CGLayer)](ciimage/init(cglayer:).md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](ciimage/init(cglayer:options:).md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](ciimage/init(texture:size:flipped:colorspace:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/init(texture:size:flipped:options:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [static let textureTarget: CIImageOption](ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](ciimageoption/textureformat.md)
  The key for an OpenGL texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(iosurface:plane:format:options:))*