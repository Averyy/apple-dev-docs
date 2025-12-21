# allowsLinkPreview

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Declaration

```swift
@MainActor
var allowsLinkPreview: Bool { get set }
```

#### Discussion

This property is available on devices that support 3D Touch. Default value is [`false`](https://developer.apple.com/documentation/Swift/false).

If you set this value to [`true`](https://developer.apple.com/documentation/Swift/true) for a web view, users (with devices that support 3D Touch) can preview link destinations, and can preview detected data such as addresses, by pressing on links. Such previews are known to users as . If a user presses deeper, the preview navigates (or , in user terminology) to the destination. Because pop navigation switches the user from your app to Safari, it is opt-in, by way of this property, rather default behavior for this class.

If you want to support link preview but also want to keep users within your app, you can switch from using the [`UIWebView`](uiwebview.md) class to the [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) class. If you are using a web view as an in-app browser, making this change is best practice. The Safari view controller class automatically supports link previews.

## See Also

- [var scalesPageToFit: Bool](uiwebview/scalespagetofit.md)
  A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.
- [var scrollView: UIScrollView](uiwebview/scrollview.md)
  The scroll view associated with the web view.
- [var suppressesIncrementalRendering: Bool](uiwebview/suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var keyboardDisplayRequiresUserAction: Bool](uiwebview/keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.
- [var dataDetectorTypes: UIDataDetectorTypes](uiwebview/datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/allowslinkpreview)*