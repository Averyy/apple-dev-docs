# VTSuperResolutionScalerConfiguration

**Framework**: Video Toolbox  
**Kind**: class

Configuration that you use to set up the super-resolution processor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class VTSuperResolutionScalerConfiguration
```

#### Overview

This configuration enables the super-resolution processor on a `VTFrameProcessor` session.

> ❗ **Important**: The super-resolution processor may require ML models which the framework needs to download in order to operate. Before calling [`startSession(configuration:)`](vtframeprocessor/startsession(configuration:).md) with an instance of this class, it is important that you verify that the necessary models are present by checking [`configurationModelStatus`](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md). If models are not available, you can trigger model download using the [`downloadConfigurationModel(completionHandler:)`](vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:).md) method. Best practice is to confirm availability of models and drive download with user awareness and interaction before engaging workflows that need this processor.

## Topics

### Initializers
- [init?(frameWidth: Int, frameHeight: Int, scaleFactor: Int, inputType: VTSuperResolutionScalerConfiguration.InputType, usePrecomputedFlow: Bool, qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization, revision: VTSuperResolutionScalerConfiguration.Revision)](vtsuperresolutionscalerconfiguration/init(framewidth:frameheight:scalefactor:inputtype:useprecomputedflow:qualityprioritization:revision:).md)
  Creates a new super-resolution scaler processor configuration.
### Instance Properties
- [var configurationModelPercentageAvailable: Float](vtsuperresolutionscalerconfiguration/configurationmodelpercentageavailable.md)
  Returns a floating point value between 0.0 and 1.0 indicating the percentage of required model assets that have been downloaded.
- [var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md)
  Reports the download status of models that the system needs for the current configuration.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var frameHeight: Int](vtsuperresolutionscalerconfiguration/frameheight.md)
  Height of source frame in pixels.
- [var frameWidth: Int](vtsuperresolutionscalerconfiguration/framewidth.md)
  Width of source frame in pixels.
- [var inputType: VTSuperResolutionScalerConfiguration.InputType](vtsuperresolutionscalerconfiguration/inputtype-swift.property.md)
  Indicates the type of input.
- [var qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.property.md)
  A parameter to control quality and performance levels.
- [var revision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision you use to perform the request.
- [var scaleFactor: Int](vtsuperresolutionscalerconfiguration/scalefactor.md)
  Indicates the scale factor between input and output.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var supportedPixelFormats: [OSType]](vtsuperresolutionscalerconfiguration/supportedpixelformats.md)
- [var usesPrecomputedFlow: Bool](vtsuperresolutionscalerconfiguration/usesprecomputedflow.md)
  Indicates that you provide optical flow.
### Instance Methods
- [func downloadConfigurationModel(completionHandler: ((any Error)?) -> Void)](vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:).md)
  Downloads models that the system needs for the current configuration.
### Type Properties
- [class var defaultRevision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/defaultrevision.md)
  Provides the default revision of a specific algorithm or configuration.
- [class var isSupported: Bool](vtsuperresolutionscalerconfiguration/issupported.md)
  Reports whether the system supports this processor.
- [class var supportedRevisions: IndexSet](vtsuperresolutionscalerconfiguration/supportedrevisions.md)
  Provides the collection of currently supported algorithms or configuration revisions for the class of configuration.
- [class var supportedScaleFactors: [Int]](vtsuperresolutionscalerconfiguration/supportedscalefactors-7ucur.md)
### Enumerations
- [VTSuperResolutionScalerConfiguration.InputType](vtsuperresolutionscalerconfiguration/inputtype-swift.enum.md)
  Available super-resolution processor input types.
- [VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/modelstatus.md)
  Available super-resolution processor model status types.
- [VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.enum.md)
  Configuration value you set to prioritize quality or performance.
- [VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.enum.md)
  Available algorithm revisions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VTFrameProcessorConfiguration](vtframeprocessorconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration)*