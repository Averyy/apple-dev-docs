# separateSecondaryViewController(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a split view controller transitions to a regular-width size class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?
```

```objc
- (UIViewController *) separateSecondaryViewControllerForSplitViewController:(UISplitViewController *) splitViewController;
```

## Return Value

The designated secondary view controller for the split view controller.

## Discussion

This method provides default behavior when you do not overwrite the [`splitViewController(_:separateSecondaryFrom:)`](../uisplitviewcontrollerdelegate/splitviewcontroller%28_,separatesecondaryfrom%29.md) method. The previous secondary view controller is returned.

## Parameters

- `splitViewController`: The current split view controller.

## See Also

### Adapting to environment changes
- [func collapseSecondaryViewController(UIViewController, for: UISplitViewController)](./collapsesecondaryviewcontroller%28_,for%29.md)
  Called when a split view controller transitions to a compact-width size class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/separatesecondaryviewcontroller(for:))*