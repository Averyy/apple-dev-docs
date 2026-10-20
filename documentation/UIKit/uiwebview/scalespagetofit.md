# scalesPageToFit

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
var scalesPageToFit: Bool { get set }
```

```objc
@property (nonatomic) BOOL scalesPageToFit;
```

#### Discussion

If [`true`](../../Swift/true.md), the webpage is scaled to fit and the user can zoom in and zoom out. If [`false`](../../Swift/false.md), user zooming is disabled. The default value is [`false`](../../Swift/false.md).

## See Also

### Setting web content properties
- [var allowsLinkPreview: Bool](./allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scrollView: UIScrollView](./scrollview.md)
  The scroll view associated with the web view.
- [var suppressesIncrementalRendering: Bool](./suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var keyboardDisplayRequiresUserAction: Bool](./keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.
- [var dataDetectorTypes: UIDataDetectorTypes](./datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/scalespagetofit)*