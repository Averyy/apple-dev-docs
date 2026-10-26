# FxTileableEffect

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

The designated initializer for your plug-in for rendering only certain portions of the plug-in’s output, referred to as tiles.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxTileableEffect : NSObjectProtocol
```

```objc
@protocol FxTileableEffect <NSObject>
```

## Mentions

- [Building an FxPlug plug-in manually](https://developer.apple.com/documentation/professional-video-applications/building-an-fxplug-plug-in-manually)
- [Migrating FxPlug 3 plug-ins to FxPlug 4](https://developer.apple.com/documentation/professional-video-applications/migrating-fxplug-3-plug-ins-to-fxplug-4)
- [Adding parameters to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-parameters-to-plug-ins)
- [Thread safety in plug-ins](https://developer.apple.com/documentation/professional-video-applications/thread-safety-in-plug-ins)

#### Overview

Using this protocol, your plug-in can render select portions of its output, or tiles, to increase efficiency and to operate outside the host’s process. Your plug-in should saves a weak reference to the `apiManager` object to use in subsequent calls. The plug-in initializes its properties and instance variables and returns a pointer to `self`. If any part of initialization fails in an unrecoverable way, this method returns `nil`.

## Parameters

- `apiManager`: An object that obtains the various API objects your plug-in needs for communicating with the host application.

## Topics

### Setting up your plug-in
- [init?(apiManager: any PROAPIAccessing)](./fxtileableeffect/init%28apimanager%29-6vvaz.md)
  Initializes the API manager for your plug-in.
- [protocol PROAPIAccessing](./proapiaccessing.md)
- [func finishInitialSetup() throws](./fxtileableeffect/finishinitialsetup%28%29.md)
  Finishes the initial setup and is called exactly once on first application of your plug-in to allow it to do anything else it needs to in order to finish setting itself up.
- [func pluginInstanceAddedToDocument()](./fxtileableeffect/plugininstanceaddedtodocument%28%29.md)
  Notifies your plug-in when it becomes part of user’s document.
- [func properties(AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws](./fxtileableeffect/properties%28_%29.md)
  Tells the host application about what the plug-in needs and supports, such as whether it renders in a gamma-corrected color space or a linear one.
### Adding and setting parameters
- [func addParameters() throws](./fxtileableeffect/addparameters%28%29.md)
  Tells the host application what parameters your plug-in requires.
- [func `class`(forCustomParameterID: UInt32) -> AnyClass](./fxtileableeffect/class%28forcustomparameterid%29.md)
  Returns the class of the object contained in the custom parameter with the given ID.
- [func classes(forCustomParameterID: UInt32) -> Set<AnyHashable>](./fxtileableeffect/classes%28forcustomparameterid%29.md)
  Returns the classes of the objects contained in the custom parameter with the given ID.
- [func parameterChanged(UInt32, at: CMTime) throws](./fxtileableeffect/parameterchanged%28_,at%29.md)
  Executes when the host detects that a parameter has changed.
### Determining input and output bounds
- [func sourceTileRect(UnsafeMutablePointer<FxRect>, sourceImageIndex: Int, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at: CMTime) throws](./fxtileableeffect/sourcetilerect%28_,sourceimageindex,sourceimages,destinationtilerect,destinationimage,pluginstate,at%29.md)
  Calculate the input rectangle needed for the given image input and the output tile to be rendered.
- [func destinationImageRect(UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at: CMTime) throws](./fxtileableeffect/destinationimagerect%28_,sourceimages,destinationimage,pluginstate,at%29.md)
  Calculates the bounds of the output image determined by the various inputs and plug-in state at the given render time.
- [func FxRectsAreEqual(FxRect, FxRect) -> Bool](./fxrectsareequal%28_,_%29.md)
  Compares two rectangle structures and determines if they are equal.
### Rendering an output
- [func pluginState(AutoreleasingUnsafeMutablePointer<NSData>?, at: CMTime, quality: FxQuality) throws](./fxtileableeffect/pluginstate%28_,at,quality%29.md)
  Retrieves the plug-in’s parameter values, performs any calculations it needs to from those values, and packages up the result to be used later with rendering.
- [func scheduleInputs(AutoreleasingUnsafeMutablePointer<NSArray?>?, withPluginState: Data?, at: CMTime) throws](./fxtileableeffect/scheduleinputs%28_,withpluginstate,at%29.md)
  Tells the host application how many frames from the given input sources your plug-in requires in order to render at the given render time.
- [func renderDestinationImage(FxImageTile, sourceImages: [FxImageTile], pluginState: Data?, at: CMTime) throws](./fxtileableeffect/renderdestinationimage%28_,sourceimages,pluginstate,at%29.md)
  Sends a request that the host wants your plug-in to do its rendering for a given output image tile.
### Data types
- [typealias FxDepth](./fxdepth.md)
  Constants used to identify bit depth.
- [typealias FxField](./fxfield.md)
  Constants used to identify a field.
- [typealias FxFieldOrder](./fxfieldorder.md)
  Constants used to identify the field order of an image stream.
- [typealias FxPoint2D](./fxpoint2d.md)
  A 2D point representation.
- [struct FxPoint3D](./fxpoint3d.md)
  A 3D point representation
- [typealias FxQuality](./fxquality.md)
  Constants used to identify rendering quality.
- [struct FxRect](./fxrect.md)
  A 2D axis-aligned rectangle with integer coordinates.
- [typealias FxSize](./fxsize.md)
  A structure to store width and height values.
- [typealias FxDrawingCoordinates](./fxdrawingcoordinates.md)
  Constants used to identify coordinate spaces.
- [typealias FxError](./fxerror.md)
  Errors returned by plug-in hosts applications.
- [typealias FxImageColorInfo](./fximagecolorinfo.md)
  Identifies some color properties of an FxImage instance. These include the color space, gamma level, and, in the case of `YCbCr` images, the color matrix for conversion to RGB.
### Constants
- [var kFxRect_Empty: FxRect](./kfxrect_empty.md)
  An empty rectangle.
- [var kFxRect_Infinite: FxRect](./kfxrect_infinite.md)
  An infinite rectangle.
- [typealias FxQuality](./fxquality.md)
  Constants used to identify rendering quality.
- [typealias FxDepth](./fxdepth.md)
  Constants used to identify bit depth.
- [let FxPlugErrorDomain: String](./fxplugerrordomain.md)
  The error domain for FxPlug-related errors.
### Initializers
- [init?(APIManager: any PROAPIAccessing)](./fxtileableeffect/init%28apimanager%29-31e6q.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Rendering
- [Rendering in FxPlug](https://developer.apple.com/documentation/professional-video-applications/rendering-in-fxplug)
  Use Metal or other frameworks to render images with your FxPlug plug-in.
- [Communicating with the plug-in state](https://developer.apple.com/documentation/professional-video-applications/communicating-with-the-plug-in-state)
  Prepare the necessary information, such as parameter values, for your FxPlug plug-in to render.
- [Working with tiled images](https://developer.apple.com/documentation/professional-video-applications/working-with-tiled-images)
  Render only the necessary tiles of an image in your FxPlug plug-in to improve efficiency.
- [Optimizing FxPlug plug-ins](https://developer.apple.com/documentation/professional-video-applications/optimizing-fxplug-plug-ins)
  Maintain consistent rendering at all resolutions and aspect ratios by using pixel transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect)*