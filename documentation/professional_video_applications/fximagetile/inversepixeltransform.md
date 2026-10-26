# inversePixelTransform

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

The inverse of the [`pixelTransform`](./pixeltransform.md).

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
@NSCopying
var inversePixelTransform: FxMatrix44! { get }
```

```objc
@property (nonatomic, copy, readonly) FxMatrix44 * inversePixelTransform;
```

## Mentions

- [Optimizing FxPlug plug-ins](https://developer.apple.com/documentation/professional-video-applications/optimizing-fxplug-plug-ins)

## See Also

### Instance Properties
- [var deviceRegistryID: UInt64](./deviceregistryid.md)
  The registryID of the Metal device or OpenGL renderer used to create this texture.
- [var eyeType: FxEyeType](./eyetype.md)
  The stereoscopic eye type of the image tile.
- [var field: FxField](./field.md)
  Which field of the image this is.
- [var fieldOrder: FxFieldOrder](./fieldorder.md)
  What the field order of the image is.
- [var imageOrigin: FxImageOrigin](./imageorigin.md)
  The origin of the image tile.
- [var imagePixelBounds: FxRect](./imagepixelbounds.md)
  The pixel bounds of the entire image.
- [var imageSource: FxImageTileRequestSource](./imagesource.md)
  Whether this image tile is from an effect source or an image well parameter.
- [var ioSurface: IOSurface!](./iosurface.md)
  The surface object to cast as a surface reference.
- [var mediaTime: CMTime](./mediatime.md)
  The media time of this image tile.
- [var parameterID: UInt32](./parameterid.md)
  The parameter ID of the image well parameter of the source of this image tile. `0` if it is the effect source and not from a parameter.
- [var pixelTransform: FxMatrix44!](./pixeltransform.md)
  The transformation between pixel units and idealized, 100% scale, square pixel image units.
- [var requestError: (any Error)!](./requesterror.md)
  Any errors that occurred from the image request. Can be nil if there were no errors or errors are not applicable.
- [var tilePixelBounds: FxRect](./tilepixelbounds.md)
  The pixel bounds of this tile.
- [var colorSpace: CGColorSpace!](./colorspace.md)
  The CGColorSpaceRef that matches the color space used in creating the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetile/inversepixeltransform)*