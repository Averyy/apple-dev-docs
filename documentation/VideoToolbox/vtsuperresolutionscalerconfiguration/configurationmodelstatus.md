# configurationModelStatus

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Reports the download status of models that the system needs for the current configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus { get }
```

```objc
@property (nonatomic, readonly) VTSuperResolutionScalerConfigurationModelStatus configurationModelStatus;
```

## See Also

### Managing the configuration model
- [VTSuperResolutionScalerConfiguration.ModelStatus](./modelstatus.md)
  Available super-resolution processor model status types.
- [var configurationModelPercentageAvailable: Float](./configurationmodelpercentageavailable.md)
  Returns a floating point value between 0.0 and 1.0 indicating the percentage of required model assets that have been downloaded.
- [func downloadConfigurationModel(completionHandler: ((any Error)?) -> Void)](./downloadconfigurationmodel%28completionhandler%29.md)
  Downloads models that the system needs for the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/configurationmodelstatus)*