# VTSuperResolutionScalerConfiguration.ModelStatus

**Framework**: Video Toolbox  
**Kind**: enum

Available super-resolution processor model status types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum ModelStatus
```

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerConfiguration.ModelStatus.downloadRequired](vtsuperresolutionscalerconfiguration/modelstatus/downloadrequired.md)
- [VTSuperResolutionScalerConfiguration.ModelStatus.downloading](vtsuperresolutionscalerconfiguration/modelstatus/downloading.md)
- [VTSuperResolutionScalerConfiguration.ModelStatus.ready](vtsuperresolutionscalerconfiguration/modelstatus/ready.md)
### Initializers
- [init?(rawValue: Int)](vtsuperresolutionscalerconfiguration/modelstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md)
  Reports the download status of models that the system needs for the current configuration.
- [var configurationModelPercentageAvailable: Float](vtsuperresolutionscalerconfiguration/configurationmodelpercentageavailable.md)
  Returns a floating point value between 0.0 and 1.0 indicating the percentage of required model assets that have been downloaded.
- [func downloadConfigurationModel(completionHandler: ((any Error)?) -> Void)](vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:).md)
  Downloads models that the system needs for the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/modelstatus)*