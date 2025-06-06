# imageWithTexture:size:flipped:options:

**Framework**: Core Image  
**Kind**: clm

Creates and returns an image object initialized with data supplied by an OpenGL texture.

**Availability**:
- macOS 10.9+ - Deprecated in 10.14

## Declaration

```swift
+ (CIImage *)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped options:(NSDictionary<CIImageOption, id> *)options;
```

#### Return_value

An image object initialized with the texture data.

#### Discussion

When using a texture to create a [`CIImage`](ciimage.md) object, the texture must be valid in the Core Image context ([`CIContext`](cicontext.md)) that you draw the [`CIImage`](ciimage.md) object into. This means that one of the following must be true:

- The texture must be created using the `CGLContext` object that the Core Image context is based on.
- The context that the texture was created in must be shared with the `CGLContext` that the Core Image context is based on.

Note that textures do not have a retain and release mechanism. This means that your application must make sure that the texture exists for the life cycle of the image. When you no longer need the image, you can delete the texture.

Core Image ignores the texture filtering and wrap modes (`GL_TEXTURE_FILTER` and `GL_TEXTURE_WRAP`) that you set through OpenGL. The filter and wrap modes are overridden by what the [`CISampler`](cisampler.md) object specifies when you apply a filter to the [`CIImage`](ciimage.md) object.

## Parameters

- `name`: An OpenGL texture. Because   objects are immutable, the texture  must remain unchanged for the life of the image object. See the discussion for more information.
- `size`: The dimensions of the texture.
- `flag`:  to have Core Image flip the coordinates of the texture vertically to convert between OpenGL and Core Image coordinate systems.
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
- [- initWithTexture:size:flipped:colorSpace:](ciimage/1438015-initwithtexture.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [- initWithTexture:size:flipped:options:](ciimage/1437880-initwithtexture.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [+ imageWithIOSurface:options:](ciimage/1547001-imagewithiosurface.md)
  Creates, using the specified options, and returns an image from the contents of an IOSurface.
- [- initWithIOSurface:plane:format:options:](ciimage/1437670-initwithiosurface.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [kCIImageTextureTarget](kciimagetexturetarget.md)
  The key for an OpenGL texture target.
- [kCIImageTextureFormat](kciimagetextureformat.md)
  The key for an OpenGL texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1547000-imagewithtexture)*