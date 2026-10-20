# VTSuperResolutionScalerConfiguration.ModelStatus

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum VTSuperResolutionScalerConfigurationModelStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerConfiguration.ModelStatus.downloadRequired](./modelstatus/downloadrequired.md)
- [VTSuperResolutionScalerConfiguration.ModelStatus.downloading](./modelstatus/downloading.md)
- [VTSuperResolutionScalerConfiguration.ModelStatus.ready](./modelstatus/ready.md)
### Initializers
- [init?(rawValue: Int)](./modelstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the configuration model
- [var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus](./configurationmodelstatus.md)
  Reports the download status of models that the system needs for the current configuration.
- [var configurationModelPercentageAvailable: Float](./configurationmodelpercentageavailable.md)
  Returns a floating point value between 0.0 and 1.0 indicating the percentage of required model assets that have been downloaded.
- [func downloadConfigurationModel(completionHandler: ((any Error)?) -> Void)](./downloadconfigurationmodel%28completionhandler%29.md)
  Downloads models that the system needs for the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/modelstatus)*