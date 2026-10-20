# paginationBreakingMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The manner in which column- or page-breaking occurs.

**Availability**:
- iOS 7.0+ - Deprecated in 12.0
- iPadOS 7.0+ - Deprecated in 12.0
- Mac Catalyst 7.0+ - Deprecated in 12.0

## Declaration

```swift
var paginationBreakingMode: UIWebView.PaginationBreakingMode { get set }
```

```objc
@property (nonatomic) UIWebPaginationBreakingMode paginationBreakingMode;
```

#### Discussion

This property determines whether certain CSS properties regarding column- and page-breaking are honored or ignored. When this property is set to [`UIWebView.PaginationBreakingMode.column`](./paginationbreakingmode-swift.enum/column.md), the content respects the CSS properties related to column-breaking in place of page-breaking.

See [`UIWebView.PaginationBreakingMode`](./paginationbreakingmode-swift.enum.md) for possible values. The default value is [`UIWebView.PaginationBreakingMode.page`](./paginationbreakingmode-swift.enum/page.md).

## See Also

### Managing pages
- [var gapBetweenPages: CGFloat](./gapbetweenpages.md)
  The size of the gap, in points, between pages.
- [var pageCount: Int](./pagecount.md)
  The number of pages produced by the layout of the web view.
- [var pageLength: CGFloat](./pagelength.md)
  The size of each page, in points, in the direction that the pages flow.
- [var paginationMode: UIWebView.PaginationMode](./paginationmode-swift.property.md)
  The layout of content in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode-swift.property)*