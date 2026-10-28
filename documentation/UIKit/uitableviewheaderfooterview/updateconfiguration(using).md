# updateConfiguration(using:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the view’s configuration using the current state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@MainActor
@objc(_bridgedUpdateConfigurationUsingState:) @preconcurrency dynamic func updateConfiguration(using state: UIViewConfigurationState)
```

## Discussion

Avoid calling this method directly. Instead, use [`setNeedsUpdateConfiguration()`](./setneedsupdateconfiguration%28%29.md) to request an update.

Override this method in a subclass to update the view’s configuration using the provided state.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in table header and footer views
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](./configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/updateconfiguration(using:))*