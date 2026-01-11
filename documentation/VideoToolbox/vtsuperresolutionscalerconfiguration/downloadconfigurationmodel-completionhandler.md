# downloadConfigurationModel(completionHandler:)

**Framework**: Video Toolbox  
**Kind**: method

Downloads models that the system needs for the current configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func downloadConfigurationModel() async throws
```

#### Discussion

This method downloads model assets required for the current configuration in background. You should call this method if [`configurationModelStatus`](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md) is `VTSuperResolutionScalerConfigurationModelStatusDownloadRequired`. After this method is called, you can query [`configurationModelPercentageAvailable`](vtsuperresolutionscalerconfiguration/configurationmodelpercentageavailable.md) to determine progress of model asset download process. If the download fails, the completion handler is invoked with an `NSError`, and the [`configurationModelStatus`](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md) goes back to `VTSuperResolutionScalerConfigurationModelStatusDownloadRequired`. If the download succeeds, the completion handler is invoked with `nil` NSError.

## See Also

- [var configurationModelStatus: VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/configurationmodelstatus.md)
  Reports the download status of models that the system needs for the current configuration.
- [VTSuperResolutionScalerConfiguration.ModelStatus](vtsuperresolutionscalerconfiguration/modelstatus.md)
  Available super-resolution processor model status types.
- [var configurationModelPercentageAvailable: Float](vtsuperresolutionscalerconfiguration/configurationmodelpercentageavailable.md)
  Returns a floating point value between 0.0 and 1.0 indicating the percentage of required model assets that have been downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:))*