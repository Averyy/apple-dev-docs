# updateProperties()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Configures the view controller’s content and styling properties.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func updateProperties()
```

```objc
- (void) updateProperties;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)
- [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md)

## Overview

Override this method to configure the view’s content and styling in your view controller subclass. Don’t call this method directly; instead, call [`setNeedsUpdateProperties()`](./setneedsupdateproperties%28%29.md) to schedule an update.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in view controllers
- [func viewWillLayoutSubviews()](./viewwilllayoutsubviews%28%29.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](./viewdidlayoutsubviews%28%29.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](./updateviewconstraints%28%29.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](./updatecontentunavailableconfiguration%28using%29.md)
  Updates the content-unavailable configuration for the provided state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/updateproperties())*