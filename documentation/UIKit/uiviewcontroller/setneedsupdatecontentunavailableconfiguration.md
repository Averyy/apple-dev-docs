# setNeedsUpdateContentUnavailableConfiguration()

**Framework**: UIKit  
**Kind**: method

Requests that the system update the content-unavailable configuration for the latest state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateContentUnavailableConfiguration()
```

## See Also

- [var contentUnavailableConfiguration: (any UIContentConfiguration)?](uiviewcontroller/contentunavailableconfiguration-4b95e.md)
  The current content-unavailable configuration of the view controller.
- [var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState](uiviewcontroller/contentunavailableconfigurationstate-7sczw.md)
  The current configuration state of the content-unavailable view.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.
- [struct UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdatecontentunavailableconfiguration())*