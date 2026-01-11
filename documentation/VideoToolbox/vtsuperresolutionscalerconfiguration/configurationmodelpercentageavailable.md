# configurationModelPercentageAvailable

**Framework**: Video Toolbox  
**Kind**: property

Returns a floating point value between 0.0 and 1.0 indicating the percentage of required model assets that have been downloaded.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var configurationModelPercentageAvailable: Float { get }
```

## See Also

- [var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md)
  Reports the download status of models that the system needs for the current configuration.
- [VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/modelstatus.md)
  Available super-resolution processor model status types.
- [func downloadConfigurationModel(completionHandler: ((any Error)?) -> Void)](vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:).md)
  Downloads models that the system needs for the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/configurationmodelpercentageavailable)*