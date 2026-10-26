# renderDestinationImage(_:sourceImages:pluginState:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends a request that the host wants your plug-in to do its rendering for a given output image tile.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func renderDestinationImage(_ destinationImage: FxImageTile, sourceImages: [FxImageTile], pluginState: Data?, at renderTime: CMTime) throws
```

```objc
- (BOOL) renderDestinationImage:(FxImageTile *) destinationImage sourceImages:(NSArray<FxImageTile *> *) sourceImages pluginState:(NSData *) pluginState atTime:(CMTime) renderTime error:(NSError * *) outError;
```

## Mentions

- [Migrating FxPlug 3 plug-ins to FxPlug 4](https://developer.apple.com/documentation/professional-video-applications/migrating-fxplug-3-plug-ins-to-fxplug-4)
- [Rendering in FxPlug](https://developer.apple.com/documentation/professional-video-applications/rendering-in-fxplug)
- [Thread safety in plug-ins](https://developer.apple.com/documentation/professional-video-applications/thread-safety-in-plug-ins)

#### Discussion

The host calls method when it wants your plug-in to render an image tile of the output image. It passes in each of the input tiles needed as well as the plug-in state needed for the calculations. Your plug-in does all its rendering in this method. Do not attempt to use the `FxParameterRetrievalAPI*` object, as it is invalid at this time. Note that this method will be called on multiple threads at the same time.

## Parameters

- `destinationImage`: The output image tile that your plug-in should render to.
- `sourceImages`: An array of image tiles. Each one will have the size calculated in your plug-in’s [`sourceTileRect(_:sourceImageIndex:sourceImages:destinationTileRect:destinationImage:pluginState:at:)`](./sourcetilerect%28_,sourceimageindex,sourceimages,destinationtilerect,destinationimage,pluginstate,at%29.md) method.
- `pluginState`: The `NSData` returned from your plug-in’s [`pluginState(_:at:quality:)`](./pluginstate%28_,at,quality%29.md) method.
- `renderTime`: The rational time at which to render your output.

## See Also

### Rendering an output
- [func pluginState(AutoreleasingUnsafeMutablePointer<NSData>?, at: CMTime, quality: FxQuality) throws](./pluginstate%28_,at,quality%29.md)
  Retrieves the plug-in’s parameter values, performs any calculations it needs to from those values, and packages up the result to be used later with rendering.
- [func scheduleInputs(AutoreleasingUnsafeMutablePointer<NSArray?>?, withPluginState: Data?, at: CMTime) throws](./scheduleinputs%28_,withpluginstate,at%29.md)
  Tells the host application how many frames from the given input sources your plug-in requires in order to render at the given render time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/renderdestinationimage(_:sourceimages:pluginstate:at:))*