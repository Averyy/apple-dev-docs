# scalesPageToFit

**Framework**: UIKit  
**Kind**: property

A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
var scalesPageToFit: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the webpage is scaled to fit and the user can zoom in and zoom out. If [`false`](https://developer.apple.com/documentation/swift/false), user zooming is disabled. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var allowsLinkPreview: Bool](uiwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scrollView: UIScrollView](uiwebview/scrollview.md)
  The scroll view associated with the web view.
- [var suppressesIncrementalRendering: Bool](uiwebview/suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var keyboardDisplayRequiresUserAction: Bool](uiwebview/keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.
- [var dataDetectorTypes: UIDataDetectorTypes](uiwebview/datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/scalespagetofit)*