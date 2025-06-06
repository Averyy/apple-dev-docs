# scrollView

**Framework**: UIKit  
**Kind**: property

The scroll view associated with the web view.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+

## Declaration

```swift
@MainActor
var scrollView: UIScrollView { get }
```

#### Discussion

Your app can access the scroll view if it wants to customize the scrolling behavior of the web view.

## See Also

- [var allowsLinkPreview: Bool](uiwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scalesPageToFit: Bool](uiwebview/scalespagetofit.md)
  A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.
- [var suppressesIncrementalRendering: Bool](uiwebview/suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var keyboardDisplayRequiresUserAction: Bool](uiwebview/keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.
- [var dataDetectorTypes: UIDataDetectorTypes](uiwebview/datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/scrollview)*