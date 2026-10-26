# destinationImageRect(_:sourceImages:destinationImage:pluginState:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Calculates the bounds of the output image determined by the various inputs and plug-in state at the given render time.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func destinationImageRect(_ destinationImageRect: UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws
```

```objc
- (BOOL) destinationImageRect:(FxRect *) destinationImageRect sourceImages:(NSArray<FxImageTile *> *) sourceImages destinationImage:(FxImageTile *) destinationImage pluginState:(NSData *) pluginState atTime:(CMTime) renderTime error:(NSError * *) outError;
```

## Mentions

- [Working with tiled images](../../Professional-Video-Applications/working-with-tiled-images.md)

#### Discussion

This method is called when the plug-in wants to calculate the output bounds of your plug-in when rendering at a particular time. It will pass in an array of images, the plug-in state returned from your plug-in’s [`pluginState(_:at:quality:)`](./pluginstate%28_,at,quality%29.md) method, and the render time. If your plug-in is unable to calculate the output rectangle at the given time, it should return `NO` and fill out the `outError` parameter with an `NSError` that uses the [`FxPlugErrorDomain`](../fxplugerrordomain.md) and appropriate (possibly custom) error code.

## Parameters

- `destinationImageRect`: The bounds of the output image. Your plug-in should calculate this value.
- `sourceImages`: An array of images that represent the input images. They will have proper bounding rectangles and pixel transforms, but no pixel data will be given yet.
- `destinationImage`: 
- `pluginState`: The `NSData` returned from your plug-in’s [`pluginState(_:at:quality:)`](./pluginstate%28_,at,quality%29.md) method.
- `renderTime`: The rational time at which the output will be rendered.

## See Also

### Determining input and output bounds
- [func sourceTileRect(UnsafeMutablePointer<FxRect>, sourceImageIndex: Int, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at: CMTime) throws](./sourcetilerect%28_,sourceimageindex,sourceimages,destinationtilerect,destinationimage,pluginstate,at%29.md)
  Calculate the input rectangle needed for the given image input and the output tile to be rendered.
- [func FxRectsAreEqual(FxRect, FxRect) -> Bool](../fxrectsareequal%28_,_%29.md)
  Compares two rectangle structures and determines if they are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/destinationimagerect(_:sourceimages:destinationimage:pluginstate:at:))*