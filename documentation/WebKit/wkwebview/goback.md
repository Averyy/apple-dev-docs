# goBack()

**Framework**: WebKit  
**Kind**: method

Navigates to the back item in the back-forward list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func goBack() -> WKNavigation?
```

#### Return Value

A new navigation to the requested item, or `nil` if there is no back item in the back-forward list.

## See Also

- [var allowsBackForwardNavigationGestures: Bool](wkwebview/allowsbackforwardnavigationgestures.md)
  A Boolean value that indicates whether horizontal swipe gestures trigger backward and forward page navigation.
- [var backForwardList: WKBackForwardList](wkwebview/backforwardlist.md)
  The web view’s back-forward list.
- [func goBack(Any?)](wkwebview/goback(_:).md)
  Navigates to the back item in the back-forward list.
- [func goForward(Any?)](wkwebview/goforward(_:).md)
  Navigates to the forward item in the back-forward list.
- [func goForward() -> WKNavigation?](wkwebview/goforward.md)
  Navigates to the forward item in the back-forward list.
- [func go(to: WKBackForwardListItem) -> WKNavigation?](wkwebview/go(to:).md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [var canGoBack: Bool](wkwebview/cangoback.md)
  A Boolean value that indicates whether there is a valid back item in the back-forward list.
- [var canGoForward: Bool](wkwebview/cangoforward.md)
  A Boolean value that indicates whether there is a valid forward item in the back-forward list.
- [var allowsLinkPreview: Bool](wkwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing a link displays a preview of the destination for the link.
- [var interactionState: Any?](wkwebview/interactionstate.md)
  An object you use to capture the current state of interaction in a web view so that you can restore that state later to another web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/goback())*