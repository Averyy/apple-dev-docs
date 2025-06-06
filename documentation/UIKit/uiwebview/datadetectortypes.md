# dataDetectorTypes

**Framework**: UIKit  
**Kind**: property

The types of data converted to clickable URLs in the web view’s content.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+

## Declaration

```swift
@MainActor
var dataDetectorTypes: UIDataDetectorTypes { get set }
```

#### Discussion

Use this property to specify the types of data (phone numbers, HTTP links, email address, and so on) that should be automatically converted to clickable URLs in the web view. When clicked, the web view opens the app responsible for handling the URL type and passes it the URL.

See the [`UIDataDetectorTypes`](uidatadetectortypes.md) enumeration for the types of data available for automatic detection.

## See Also

- [var allowsLinkPreview: Bool](uiwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scalesPageToFit: Bool](uiwebview/scalespagetofit.md)
  A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.
- [var scrollView: UIScrollView](uiwebview/scrollview.md)
  The scroll view associated with the web view.
- [var suppressesIncrementalRendering: Bool](uiwebview/suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var keyboardDisplayRequiresUserAction: Bool](uiwebview/keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/datadetectortypes)*