# FxImageTile

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

An image tile object that is passed between an out-of-process FxPlug plug-in and a host application.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
class FxImageTile
```

```objc
@interface FxImageTile : NSObject
```

## Mentions

- [Rendering in FxPlug](../Professional-Video-Applications/rendering-in-fxplug.md)
- [Building an FxPlug plug-in manually](../Professional-Video-Applications/building-an-fxplug-plug-in-manually.md)
- [Optimizing FxPlug plug-ins](../Professional-Video-Applications/optimizing-fxplug-plug-ins.md)
- [Using out-of-process FxPlug plug-ins](../Professional-Video-Applications/using-out-of-process-fxplug-plug-ins.md)

## Overview

An [`FxTileableEffect`](./fxtileableeffect.md) will receive all images as `FxImageTile` objects. These are passed to effects to describe tiles within the full image that need to be rendered. The image data is contained in the [`ioSurface`](./fximagetile/iosurface.md) property. This property may be nil during calls to the plug-in to gather information rather than rendering.

## Topics

### Instance Properties
- [var deviceRegistryID: UInt64](./fximagetile/deviceregistryid.md)
  The registryID of the Metal device or OpenGL renderer used to create this texture.
- [var eyeType: FxEyeType](./fximagetile/eyetype.md)
  The stereoscopic eye type of the image tile.
- [var field: FxField](./fximagetile/field.md)
  Which field of the image this is.
- [var fieldOrder: FxFieldOrder](./fximagetile/fieldorder.md)
  What the field order of the image is.
- [var imageOrigin: FxImageOrigin](./fximagetile/imageorigin.md)
  The origin of the image tile.
- [var imagePixelBounds: FxRect](./fximagetile/imagepixelbounds.md)
  The pixel bounds of the entire image.
- [var imageSource: FxImageTileRequestSource](./fximagetile/imagesource.md)
  Whether this image tile is from an effect source or an image well parameter.
- [var inversePixelTransform: FxMatrix44!](./fximagetile/inversepixeltransform.md)
  The inverse of the [`pixelTransform`](./fximagetile/pixeltransform.md).
- [var ioSurface: IOSurface!](./fximagetile/iosurface.md)
  The surface object to cast as a surface reference.
- [var mediaTime: CMTime](./fximagetile/mediatime.md)
  The media time of this image tile.
- [var parameterID: UInt32](./fximagetile/parameterid.md)
  The parameter ID of the image well parameter of the source of this image tile. `0` if it is the effect source and not from a parameter.
- [var pixelTransform: FxMatrix44!](./fximagetile/pixeltransform.md)
  The transformation between pixel units and idealized, 100% scale, square pixel image units.
- [var requestError: (any Error)!](./fximagetile/requesterror.md)
  Any errors that occurred from the image request. Can be nil if there were no errors or errors are not applicable.
- [var tilePixelBounds: FxRect](./fximagetile/tilepixelbounds.md)
  The pixel bounds of this tile.
- [var colorSpace: CGColorSpace!](./fximagetile/colorspace.md)
  The CGColorSpaceRef that matches the color space used in creating the image.
- [var pixelAspect: Double](./fximagetile/pixelaspect.md)
  The ratio of the width of each pixel to its height.
- [var scaleX: Double](./fximagetile/scalex.md)
  The horizontal scale value.
- [var scaleY: Double](./fximagetile/scaley.md)
  The vertical scale value.
### Instance Methods
- [func metalTexture(for: (any MTLDevice)!) -> (any MTLTexture)!](./fximagetile/metaltexture%28for%29.md)
  Retrieve a Metal texture from the IOSurface for rendering on the passed-in device. The returned texture is autoreleased.
- [func openGLTexture(forContext: CGLContextObj!) -> GLuint](./fximagetile/opengltexture%28forcontext%29.md)
  Retrieve an OpenGL texture from the [`ioSurface`](./fximagetile/iosurface.md) for rendering with the passed-in context. You are responsible for deleting this texture.
### Enumerations
- [typealias FxError](./fxerror.md)
  Errors returned by plug-in hosts applications.
- [struct FxEyeType](./fxeyetype.md)
  Identifies which eye is being sent from a stereoscopic project.
- [struct FxImageTileRequestSource](./fximagetilerequestsource.md)
  An enumeration that identifies the requested frame.
### Initializers
- [init?(coder: NSCoder)](./fximagetile/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Exchanging Image Tiles Between Host and Plug-in
- [class FxImageTileRequest](./fximagetilerequest.md)
  An image tile request object that is passed between an out-of-process FxPlug plug-in and a host application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetile)*