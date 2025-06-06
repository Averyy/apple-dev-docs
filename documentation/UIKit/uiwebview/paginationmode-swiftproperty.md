# paginationMode

**Framework**: UIKit  
**Kind**: property

The layout of content in the web view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

## Declaration

```swift
@MainActor
var paginationMode: UIWebView.PaginationMode { get set }
```

#### Discussion

This property determines whether content in the web view is broken up into pages that fill the view one screen at a time, or shown as one long scrolling view. If set to a paginated form, this property toggles a paginated layout on the content, causing the web view to use the values of [`pageLength`](uiwebview/pagelength.md) and [`gapBetweenPages`](uiwebview/gapbetweenpages.md) to relayout its content.

See [`UIWebView.PaginationMode`](uiwebview/paginationmode-swift.enum.md) for possible values. The default value is [`UIWebView.PaginationMode.unpaginated`](uiwebview/paginationmode-swift.enum/unpaginated.md).

## See Also

- [var gapBetweenPages: CGFloat](uiwebview/gapbetweenpages.md)
  The size of the gap, in points, between pages.
- [var pageCount: Int](uiwebview/pagecount.md)
  The number of pages produced by the layout of the web view.
- [var pageLength: CGFloat](uiwebview/pagelength.md)
  The size of each page, in points, in the direction that the pages flow.
- [var paginationBreakingMode: UIWebView.PaginationBreakingMode](uiwebview/paginationbreakingmode-swift.property.md)
  The manner in which column- or page-breaking occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/paginationmode-swift.property)*