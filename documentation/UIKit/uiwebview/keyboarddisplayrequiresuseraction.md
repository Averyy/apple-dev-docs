# keyboardDisplayRequiresUserAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether web content can programmatically display the keyboard.

**Availability**:
- iOS 6.0+ - Deprecated in 12.0
- iPadOS 6.0+ - Deprecated in 12.0
- Mac Catalyst 6.0+ - Deprecated in 12.0

## Declaration

```swift
var keyboardDisplayRequiresUserAction: Bool { get set }
```

```objc
@property (nonatomic) BOOL keyboardDisplayRequiresUserAction;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), the user must explicitly tap the elements in the web view to display the keyboard (or other relevant input view) for that element. When set to [`false`](../../Swift/false.md), a focus event on an element causes the input view to be displayed and associated with that element automatically.

The default value for this property is [`true`](../../Swift/true.md).

## See Also

### Setting web content properties
- [var allowsLinkPreview: Bool](./allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scalesPageToFit: Bool](./scalespagetofit.md)
  A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.
- [var scrollView: UIScrollView](./scrollview.md)
  The scroll view associated with the web view.
- [var suppressesIncrementalRendering: Bool](./suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var dataDetectorTypes: UIDataDetectorTypes](./datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/keyboarddisplayrequiresuseraction)*