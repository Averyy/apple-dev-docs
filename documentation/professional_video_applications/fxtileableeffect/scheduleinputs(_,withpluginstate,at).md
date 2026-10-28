# scheduleInputs(_:withPluginState:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Tells the host application how many frames from the given input sources your plug-in requires in order to render at the given render time.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
optional func scheduleInputs(_ inputImageRequests: AutoreleasingUnsafeMutablePointer<NSArray?>?, withPluginState pluginState: Data?, at renderTime: CMTime) throws
```

```objc
- (BOOL) scheduleInputs:(NSArray<FxImageTileRequest *> * *) inputImageRequests withPluginState:(NSData *) pluginState atTime:(CMTime) renderTime error:(NSError * *) error;
```

## Mentions

- [Migrating FxPlug 3 plug-ins to FxPlug 4](../../Professional-Video-Applications/migrating-fxplug-3-plug-ins-to-fxplug-4.md)
- [Scheduling media in plug-ins](../../Professional-Video-Applications/scheduling-media-in-plug-ins.md)

## Discussion

The host calls this method before rendering. Fill out the `inputImageRequests` parameter with an array of image requests. Each request represents one frame your plug-in needs to render. These can be frames of the effect source or they can be frames from image well parameters. If you don’t implement this method, the application will assume that a filter needs only the current frame of its effect source.

When instantiating an [`FxImageTileRequest`](../fximagetilerequest.md) array using [`init(source:time:includeFilters:parameterID:)`](../fximagetilerequest/init%28source,time,includefilters,parameterid%29.md), the currently supported keys for [`FxImageTileRequestSource`](../fximagetilerequestsource.md) are:

| Key | Description |
| --- | --- |
| [`kFxImageTileRequestSourceNone`](../kfximagetilerequestsourcenone.md) | Not associated with an effect or parameter. |
| [`kFxImageTileRequestSourceEffectClip`](../kfximagetilerequestsourceeffectclip.md) | Request frame from the source clip. |
| [`kFxImageTileRequestSourceParameter`](../kfximagetilerequestsourceparameter.md) | Request frame from an image well parameter. |
| [`kFxImageTileRequestSourceOutput`](../kfximagetilerequestsourceoutput.md) | The output of the plug-in. |

`time` should indicate the requested [`CMTime`](../../CoreMedia/cmtime.md) of the input, `includeFilters` will indicate if the plugin requires frames after leading filter effects have already been applied, and `parameterID` will indicate the ID of the effect source (`0`) or image well.

## Parameters

- `inputImageRequests`: An NSArray that you fill out with requests for input image sources, input image times, whether to include leading filters, and the parameter IDs you wish to schedule.
- `pluginState`: The plug-in state returned by your plug-in’s [`pluginState(_:at:quality:)`](./pluginstate%28_,at,quality%29.md) method.
- `renderTime`: The time at which your plug-in will be asked to render with the frames being scheduled.

## See Also

### Rendering an output
- [func pluginState(AutoreleasingUnsafeMutablePointer<NSData>?, at: CMTime, quality: FxQuality) throws](./pluginstate%28_,at,quality%29.md)
  Retrieves the plug-in’s parameter values, performs any calculations it needs to from those values, and packages up the result to be used later with rendering.
- [func renderDestinationImage(FxImageTile, sourceImages: [FxImageTile], pluginState: Data?, at: CMTime) throws](./renderdestinationimage%28_,sourceimages,pluginstate,at%29.md)
  Sends a request that the host wants your plug-in to do its rendering for a given output image tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/scheduleinputs(_:withpluginstate:at:))*