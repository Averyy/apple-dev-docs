# contentUnavailableConfigurationState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current configuration state of the content-unavailable view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
@objc(_bridgedContentUnavailableConfigurationState) @preconcurrency dynamic var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState { get }
```

## Discussion

You can customize the configuration state by overriding this property in your subclass. Obtain the system instance from the superclass, and customize the state as appropriate.

## See Also

### Indicating missing content
- [var contentUnavailableConfiguration: (any UIContentConfiguration)?](./contentunavailableconfiguration-4b95e.md)
  The current content-unavailable configuration of the view controller.
- [func setNeedsUpdateContentUnavailableConfiguration()](./setneedsupdatecontentunavailableconfiguration%28%29.md)
  Requests that the system update the content-unavailable configuration for the latest state.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](./updatecontentunavailableconfiguration%28using%29.md)
  Updates the content-unavailable configuration for the provided state.
- [struct UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-7sczw)*