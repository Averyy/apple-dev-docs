# sourceTileRect(_:sourceImageIndex:sourceImages:destinationTileRect:destinationImage:pluginState:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Calculate the input rectangle needed for the given image input and the output tile to be rendered.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func sourceTileRect(_ sourceTileRect: UnsafeMutablePointer<FxRect>, sourceImageIndex: Int, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws
```

```objc
- (BOOL) sourceTileRect:(FxRect *) sourceTileRect sourceImageIndex:(NSUInteger) sourceImageIndex sourceImages:(NSArray<FxImageTile *> *) sourceImages destinationTileRect:(FxRect) destinationTileRect destinationImage:(FxImageTile *) destinationImage pluginState:(NSData *) pluginState atTime:(CMTime) renderTime error:(NSError * *) outError;
```

## Mentions

- [Working with tiled images](../../Professional-Video-Applications/working-with-tiled-images.md)

## Discussion

This method is called for each image input your plug-in has requested. Use the passed-in information to calculate the portion of the current input image that you’ll need to render the output tile that will be rendered next.

## Parameters

- `sourceTileRect`: The bounds of input tile for this input that will be needed to render the output tile. This method must calculate this value.
- `sourceImageIndex`: The index of the input image for which the tile bounds have been requested. This index matches the order of images in the `inputImages` array below.
- `sourceImages`: An `NSArray` of image tiles representing the input images. This image will not yet contain any pixel data, just the image bounds, pixel transforms, and other data describing the image.
- `destinationTileRect`: The bounds of the output tile, given to you by the host application.
- `destinationImage`: The output image. This image will not yet contain any pixel data, just the image bounds and other data about the output image.
- `pluginState`: The NSData returned from your plug-in’s [`pluginState(_:at:quality:)`](./pluginstate%28_,at,quality%29.md) method.
- `renderTime`: The rational time at which the output will be rendered.

## See Also

### Determining input and output bounds
- [func destinationImageRect(UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at: CMTime) throws](./destinationimagerect%28_,sourceimages,destinationimage,pluginstate,at%29.md)
  Calculates the bounds of the output image determined by the various inputs and plug-in state at the given render time.
- [func FxRectsAreEqual(FxRect, FxRect) -> Bool](../fxrectsareequal%28_,_%29.md)
  Compares two rectangle structures and determines if they are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/sourcetilerect(_:sourceimageindex:sourceimages:destinationtilerect:destinationimage:pluginstate:at:))*