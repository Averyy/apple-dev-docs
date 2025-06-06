# closePopup()

**Framework**: Webkit  
**Kind**: method

Triggers the dismissal process of the pop-up.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func closePopup()
```

#### Discussion

Invoke this method to manage the pop-up’s lifecycle, ensuring the web view is unloaded and resources are released once the pop-up closes. This method is automatically called upon the dismissal of the action’s [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) or [`NSPopover`](https://developer.apple.com/documentation/AppKit/NSPopover).  For custom scenarios where the pop-up’s lifecycle is manually managed, it must be explicitly invoked to ensure proper closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/closepopup())*