# suppressesIncrementalRendering

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+

## Declaration

```swift
@MainActor
var suppressesIncrementalRendering: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/Swift/true), the web view does not attempt to render incoming content as it arrives. Instead, the view’s current contents remain in place until all of the new content has been received, at which point the new content is rendered. This property does not affect the rendering of content retrieved after a frame finishes loading.

The value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) by default.

## See Also

- [var allowsLinkPreview: Bool](uiwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scalesPageToFit: Bool](uiwebview/scalespagetofit.md)
  A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.
- [var scrollView: UIScrollView](uiwebview/scrollview.md)
  The scroll view associated with the web view.
- [var keyboardDisplayRequiresUserAction: Bool](uiwebview/keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.
- [var dataDetectorTypes: UIDataDetectorTypes](uiwebview/datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/suppressesincrementalrendering)*