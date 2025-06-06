# initWithIOSurface:plane:format:options:

**Framework**: Core Image  
**Kind**: instm

Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.

**Availability**:
- macOS 10.9+ - Deprecated in 10.11

## Declaration

```swift
- (instancetype)initWithIOSurface:(IOSurfaceRef)surface plane:(size_t)plane format:(CIFormat)format options:(NSDictionary<CIImageOption, id> *)options;
```

#### Return_value

An image object initialized with the data from the IOSurface.

## Parameters

- `surface`: An IOSurface object.
- `plane`: The index of the data plane in the IOSurface object containing bitmap data for initializing the image.
- `format`: A pixel format constant. See  . 
- `options`: A dictionary specifying image options. (See  .)

## See Also

- [+ imageWithCGLayer:](ciimage/1547022-imagewithcglayer.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.
- [+ imageWithCGLayer:options:](ciimage/1546998-imagewithcglayer.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.
- [- initWithCGLayer:](ciimage/1438065-initwithcglayer.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [- initWithCGLayer:options:](ciimage/1437687-initwithcglayer.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [+ imageWithTexture:size:flipped:colorSpace:](ciimage/1547006-imagewithtexture.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithTexture:size:flipped:options:](ciimage/1547000-imagewithtexture.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [- initWithTexture:size:flipped:colorSpace:](ciimage/1438015-initwithtexture.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [- initWithTexture:size:flipped:options:](ciimage/1437880-initwithtexture.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [+ imageWithIOSurface:options:](ciimage/1547001-imagewithiosurface.md)
  Creates, using the specified options, and returns an image from the contents of an IOSurface.
- [kCIImageTextureTarget](kciimagetexturetarget.md)
  The key for an OpenGL texture target.
- [kCIImageTextureFormat](kciimagetextureformat.md)
  The key for an OpenGL texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1437670-initwithiosurface)*