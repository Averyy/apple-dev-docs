# pluginState(_:at:quality:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves the plug-in’s parameter values, performs any calculations it needs to from those values, and packages up the result to be used later with rendering.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func pluginState(_ pluginState: AutoreleasingUnsafeMutablePointer<NSData>?, at renderTime: CMTime, quality qualityLevel: FxQuality) throws
```

```objc
- (BOOL) pluginState:(NSData * *) pluginState atTime:(CMTime) renderTime quality:(FxQuality) qualityLevel error:(NSError * *) error;
```

## Mentions

- [Analyzing media](../../Professional-Video-Applications/analyzing-media.md)
- [Thread safety in plug-ins](../../Professional-Video-Applications/thread-safety-in-plug-ins.md)
- [Using FxPlug APIs](../../Professional-Video-Applications/using-fxplug-apis.md)

## Discussion

The host application calls this method before rendering. The `FxParameterRetrievalAPI*` is valid during this call. Use it to get the values of your plug-in’s parameters, then put those values or the results of any calculations you need to do with those parameters to render into an `NSData` that you return to the host application. The host passes it back to you during subsequent calls. Do not re-use the `NSData`; always create a new one, as this method may be called on multiple threads at the same time.

## Parameters

- `pluginState`: The state of the plug-in. Your plug-in should return an autoreleased [`NSData`](../../Foundation/nsdata.md) that the host retains. Once created, your plug-in should not hold on to this pointer. The host returns this data (or a copy of it) to your plug-in during other methods, such as the [`renderDestinationImage(_:sourceImages:pluginState:at:)`](./renderdestinationimage%28_,sourceimages,pluginstate,at%29.md) method and [`scheduleInputs(_:withPluginState:at:)`](./scheduleinputs%28_,withpluginstate,at%29.md) methods.
- `renderTime`: The rational time at which your plug-in is being asked to gather its rendering state.
- `qualityLevel`: The requested render quality (`kFxQuality_LOW`, `kFxQuality_MEDIUM`, or `kFxQuality_HIGH`).

## See Also

### Rendering an output
- [func scheduleInputs(AutoreleasingUnsafeMutablePointer<NSArray?>?, withPluginState: Data?, at: CMTime) throws](./scheduleinputs%28_,withpluginstate,at%29.md)
  Tells the host application how many frames from the given input sources your plug-in requires in order to render at the given render time.
- [func renderDestinationImage(FxImageTile, sourceImages: [FxImageTile], pluginState: Data?, at: CMTime) throws](./renderdestinationimage%28_,sourceimages,pluginstate,at%29.md)
  Sends a request that the host wants your plug-in to do its rendering for a given output image tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/pluginstate(_:at:quality:))*