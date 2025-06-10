# VTSuperResolutionScalerConfiguration

**Framework**: Video Toolbox  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
class VTSuperResolutionScalerConfiguration
```

#### Overview

This configuration enables the SuperResolution on a VTFrameProcessing session.  IMPORTANT: The VTSuperResolutionScaler processor may require ML models which need to be downloaded by the framework in order to operate.  Before using calling startSessionWithConfiguration with a VTSuperResolutionScalerConfiguration, it is important that you verify that the necessary models are present by checking the configurationModelStatus on the configuration object.  If models are not available, model download can be triggered using the downloadConfigurationModelWithCompletionHandler method on the configuration object.  Best practice is to confirm availability of models and drive download with user awareness and interaction before engaging workflows where the processor is needed.

## Topics

### Initializers
- [init?(frameWidth: Int, frameHeight: Int, scaleFactor: Int, inputType: VTSuperResolutionScalerConfiguration.InputType, usePrecomputedFlow: Bool, qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization, revision: VTSuperResolutionScalerConfiguration.Revision)](vtsuperresolutionscalerconfiguration/init(framewidth:frameheight:scalefactor:inputtype:useprecomputedflow:qualityprioritization:revision:).md)
### Instance Properties
- [var configurationModelPercentageAvailable: Float](vtsuperresolutionscalerconfiguration/configurationmodelpercentageavailable.md)
- [var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md)
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
- [var frameHeight: Int](vtsuperresolutionscalerconfiguration/frameheight.md)
- [var frameWidth: Int](vtsuperresolutionscalerconfiguration/framewidth.md)
- [var inputType: VTSuperResolutionScalerConfiguration.InputType](vtsuperresolutionscalerconfiguration/inputtype-swift.property.md)
- [var qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.property.md)
- [var revision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.property.md)
- [var scaleFactor: Int](vtsuperresolutionscalerconfiguration/scalefactor.md)
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
- [var supportedPixelFormats: [OSType]](vtsuperresolutionscalerconfiguration/supportedpixelformats.md)
- [var usesPrecomputedFlow: Bool](vtsuperresolutionscalerconfiguration/usesprecomputedflow.md)
### Instance Methods
- [func downloadConfigurationModel(completionHandler: ((any Error)?) -> Void)](vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:).md)
### Type Properties
- [class var defaultRevision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/defaultrevision.md)
- [class var isSupported: Bool](vtsuperresolutionscalerconfiguration/issupported.md)
- [class var supportedRevisions: IndexSet](vtsuperresolutionscalerconfiguration/supportedrevisions.md)
- [class var supportedScaleFactors: [Int]](vtsuperresolutionscalerconfiguration/supportedscalefactors-7ucur.md)
### Enumerations
- [VTSuperResolutionScalerConfiguration.InputType](vtsuperresolutionscalerconfiguration/inputtype-swift.enum.md)
- [VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/modelstatus.md)
- [VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.enum.md)
- [VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.enum.md)

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