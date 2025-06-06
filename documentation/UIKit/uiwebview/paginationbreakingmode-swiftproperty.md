# paginationBreakingMode

**Framework**: UIKit  
**Kind**: property

The manner in which column- or page-breaking occurs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

## Declaration

```swift
@MainActor
var paginationBreakingMode: UIWebView.PaginationBreakingMode { get set }
```

#### Discussion

This property determines whether certain CSS properties regarding column- and page-breaking are honored or ignored. When this property is set to [`UIWebView.PaginationBreakingMode.column`](uiwebview/paginationbreakingmode-swift.enum/column.md), the content respects the CSS properties related to column-breaking in place of page-breaking.

See [`UIWebView.PaginationBreakingMode`](uiwebview/paginationbreakingmode-swift.enum.md) for possible values. The default value is [`UIWebView.PaginationBreakingMode.page`](uiwebview/paginationbreakingmode-swift.enum/page.md).

## See Also

- [var gapBetweenPages: CGFloat](uiwebview/gapbetweenpages.md)
  The size of the gap, in points, between pages.
- [var pageCount: Int](uiwebview/pagecount.md)
  The number of pages produced by the layout of the web view.
- [var pageLength: CGFloat](uiwebview/pagelength.md)
  The size of each page, in points, in the direction that the pages flow.
- [var paginationMode: UIWebView.PaginationMode](uiwebview/paginationmode-swift.property.md)
  The layout of content in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode-swift.property)*