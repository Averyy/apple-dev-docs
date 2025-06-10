# downloadConfigurationModel(completionHandler:)

**Framework**: Video Toolbox  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func downloadConfigurationModel() async throws
```

#### Discussion

This interface can be used to download model assets required for the current VTSuperResolutionScalerConfiguration if the state is currently VTSuperResolutionScalerConfigurationModelStatusDownloadRequired.  The processorModelStatus class property can be queried to see if models are all already present.  If a download has been initiated, processorModelPercentageAvailable can be queried to determine what percentage of the model models are avialable. If the download fails, the completion handler will return an NSError, and the status will go back to VTSuperResolutionScalerConfigurationModelStatusDownloadRequired.  If the download succeeds, the NSError return value will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/downloadconfigurationmodel(completionhandler:))*