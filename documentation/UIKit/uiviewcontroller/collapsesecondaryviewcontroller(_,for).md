# collapseSecondaryViewController(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a split view controller transitions to a compact-width size class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)
```

```objc
- (void) collapseSecondaryViewController:(UIViewController *) secondaryViewController forSplitViewController:(UISplitViewController *) splitViewController;
```

## Discussion

This method provides default behavior when you do not overwrite the [`splitViewController(_:collapseSecondary:onto:)`](../uisplitviewcontrollerdelegate/splitviewcontroller%28_,collapsesecondary,onto%29.md) method. The primary view controller associated with the split view controller is displayed.

## Parameters

- `secondaryViewController`: The secondary view controller associated with the split view controller.
- `splitViewController`: The current split view controller.

## See Also

### Adapting to environment changes
- [func separateSecondaryViewController(for: UISplitViewController) -> UIViewController?](./separatesecondaryviewcontroller%28for%29.md)
  Called when a split view controller transitions to a regular-width size class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/collapsesecondaryviewcontroller(_:for:))*