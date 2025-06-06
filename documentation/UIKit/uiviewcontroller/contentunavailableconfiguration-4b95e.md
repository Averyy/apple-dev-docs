# contentUnavailableConfiguration

**Framework**: UIKit  
**Kind**: property

The current content-unavailable configuration of the view controller.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var contentUnavailableConfiguration: (any UIContentConfiguration)? { get set }
```

#### Discussion

Use this property to configure a content-unavailable view that the view controller manages. The value of this property is commonly an instance of [`UIContentUnavailableConfiguration`](uicontentunavailableconfiguration-swift.struct.md), but you can use other types of content configuration, including a [`UIHostingConfiguration`](https://developer.apple.com/documentation/SwiftUI/UIHostingConfiguration), to display a SwiftUI view.

## See Also

- [var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState](uiviewcontroller/contentunavailableconfigurationstate-7sczw.md)
  The current configuration state of the content-unavailable view.
- [func setNeedsUpdateContentUnavailableConfiguration()](uiviewcontroller/setneedsupdatecontentunavailableconfiguration.md)
  Requests that the system update the content-unavailable configuration for the latest state.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.
- [struct UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/contentunavailableconfiguration-4b95e)*