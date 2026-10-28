# allowsBackForwardNavigationGestures

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether horizontal swipe gestures trigger backward and forward page navigation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var allowsBackForwardNavigationGestures: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsBackForwardNavigationGestures;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Navigating between webpages
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
- [func go(to: WKBackForwardListItem) -> WKNavigation?](./go%28to%29.md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [var canGoBack: Bool](./cangoback.md)
  A Boolean value that indicates whether there is a valid back item in the back-forward list.
- [var canGoForward: Bool](./cangoforward.md)
  A Boolean value that indicates whether there is a valid forward item in the back-forward list.
- [var allowsLinkPreview: Bool](./allowslinkpreview.md)
  A Boolean value that determines whether pressing a link displays a preview of the destination for the link.
- [var interactionState: Any?](./interactionstate.md)
  An object you use to capture the current state of interaction in a web view so that you can restore that state later to another web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/allowsbackforwardnavigationgestures)*