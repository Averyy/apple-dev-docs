# setNeedsUpdateContentUnavailableConfiguration()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests that the system update the content-unavailable configuration for the latest state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setNeedsUpdateContentUnavailableConfiguration()
```

```objc
- (void) setNeedsUpdateContentUnavailableConfiguration;
```

## See Also

### Indicating missing content
- [var contentUnavailableConfiguration: (any UIContentConfiguration)?](./contentunavailableconfiguration-4b95e.md)
  The current content-unavailable configuration of the view controller.
- [var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState](./contentunavailableconfigurationstate-7sczw.md)
  The current configuration state of the content-unavailable view.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](./updatecontentunavailableconfiguration%28using%29.md)
  Updates the content-unavailable configuration for the provided state.
- [struct UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdatecontentunavailableconfiguration())*