# go(to:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Navigates to an item from the back-forward list and sets it as the current item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func go(to item: WKBackForwardListItem) -> WKNavigation?
```

```objc
- (WKNavigation *) goToBackForwardListItem:(WKBackForwardListItem *) item;
```

#### Return Value

A new navigation to the requested item, or `nil` if it is already the current item or is not part of the web view’s back-forward list.

## Parameters

- `item`: The item to navigate to. The item must be in the web view’s back-forward list.

## See Also

### Navigating between webpages
- [var allowsBackForwardNavigationGestures: Bool](./allowsbackforwardnavigationgestures.md)
  A Boolean value that indicates whether horizontal swipe gestures trigger backward and forward page navigation.
- [var backForwardList: WKBackForwardList](./backforwardlist.md)
  The web view’s back-forward list.
- [func goBack(Any?)](./goback%28_%29.md)
  Navigates to the back item in the back-forward list.
- [func goBack() -> WKNavigation?](./goback%28%29.md)
  Navigates to the back item in the back-forward list.
- [func goForward(Any?)](./goforward%28_%29.md)
  Navigates to the forward item in the back-forward list.
- [func goForward() -> WKNavigation?](./goforward%28%29.md)
  Navigates to the forward item in the back-forward list.
- [var canGoBack: Bool](./cangoback.md)
  A Boolean value that indicates whether there is a valid back item in the back-forward list.
- [var canGoForward: Bool](./cangoforward.md)
  A Boolean value that indicates whether there is a valid forward item in the back-forward list.
- [var allowsLinkPreview: Bool](./allowslinkpreview.md)
  A Boolean value that determines whether pressing a link displays a preview of the destination for the link.
- [var interactionState: Any?](./interactionstate.md)
  An object you use to capture the current state of interaction in a web view so that you can restore that state later to another web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/go(to:))*