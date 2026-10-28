# closePopup()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Triggers the dismissal process of the pop-up.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func closePopup()
```

```objc
- (void) closePopup;
```

## Discussion

Invoke this method to manage the pop-up’s lifecycle, ensuring the web view is unloaded and resources are released once the pop-up closes. This method is automatically called upon the dismissal of the action’s [`UIViewController`](../../../UIKit/uiviewcontroller.md) or [`NSPopover`](../../../AppKit/nspopover.md).  For custom scenarios where the pop-up’s lifecycle is manually managed, it must be explicitly invoked to ensure proper closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/closepopup())*