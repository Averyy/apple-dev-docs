# popupViewController

**Framework**: Webkit  
**Kind**: property

A view controller that presents a web view loaded with the pop-up page for this action, or `nil` if no popup is specified.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var popupViewController: UIViewController? { get }
```

#### Discussion

The view controller adaptively adjusts its presentation style based on where it is presented from, preferring popover.

It contains a web view preloaded with the pop-up page and automatically adjusts its `preferredContentSize` to fit the web view’s content size. The [`presentsPopup`](wkwebextension/action/presentspopup.md) property should be checked to determine the availability of a pop-up before using this property.

Dismissing the view controller will close the pop-up and unload the web view.

## See Also

- [var presentsPopup: Bool](wkwebextension/action/presentspopup.md)
  A Boolean value indicating whether the action has a pop-up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/popupviewcontroller)*