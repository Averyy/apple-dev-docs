# allowsLinkPreview

**Framework**: WebKit  
**Kind**: property

A Boolean value that determines whether pressing a link displays a preview of the destination for the link.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsLinkPreview: Bool { get set }
```

#### Discussion

In iOS, this property is available on devices that support 3D Touch. In iOS 10 and later, the default value is [`true`](https://developer.apple.com/documentation/Swift/true); in previous versions of iOS, the default value is [`false`](https://developer.apple.com/documentation/Swift/false).

If you set this property’s value to [`true`](https://developer.apple.com/documentation/Swift/true), an iOS user can press links to preview link destinations and detected data such as addresses and phone numbers. Such previews are known to users as . If a user presses deeper on a link preview, the preview navigates (or , in user terminology) to the destination. Because pop navigation switches the user from your app to Safari, it is opt-in for iOS apps.

If you want to support link preview in iOS but also want to keep users within your app, you can switch from using the [`WKWebView`](wkwebview.md) class to the [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) class. If you are using a web view as an in-app browser, making this change is best practice. The Safari view controller class automatically supports link previews.

In macOS, this property is available on devices with a Force Touch trackpad. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

With this property set to its default value of [`true`](https://developer.apple.com/documentation/Swift/true), a macOS user can force click a link to display a preview window showing the link’s destination. If the user then clicks the preview, the destination opens in Safari.

On both platforms, all types of detected data respond to presses when this property is set to [`true`](https://developer.apple.com/documentation/Swift/true). That is, in iOS 9 and OS X 10.11, you cannot specify which types of data are detected in the [`WKWebView`](wkwebview.md) class.

## See Also

- [var allowsBackForwardNavigationGestures: Bool](wkwebview/allowsbackforwardnavigationgestures.md)
  A Boolean value that indicates whether horizontal swipe gestures trigger backward and forward page navigation.
- [var backForwardList: WKBackForwardList](wkwebview/backforwardlist.md)
  The web view’s back-forward list.
- [func goBack(Any?)](wkwebview/goback(_:).md)
  Navigates to the back item in the back-forward list.
- [func goBack() -> WKNavigation?](wkwebview/goback.md)
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
- [var interactionState: Any?](wkwebview/interactionstate.md)
  An object you use to capture the current state of interaction in a web view so that you can restore that state later to another web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/allowslinkpreview)*