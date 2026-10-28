# pageLength

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The size of each page, in points, in the direction that the pages flow.

**Availability**:
- iOS 7.0+ - Deprecated in 12.0
- iPadOS 7.0+ - Deprecated in 12.0
- Mac Catalyst 7.0+ - Deprecated in 12.0

## Declaration

```swift
var pageLength: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat pageLength;
```

## Discussion

When [`paginationMode`](./paginationmode-swift.property.md) is right to left or left to right, this property represents the width of each page. When [`paginationMode`](./paginationmode-swift.property.md) is top to bottom or bottom to top, this property represents the height of each page.

The default value is `0`, which means the layout uses the size of the viewport to determine the dimensions of the page. Adjusting the value of this property causes a relayout.

## See Also

### Managing pages
- [var gapBetweenPages: CGFloat](./gapbetweenpages.md)
  The size of the gap, in points, between pages.
- [var pageCount: Int](./pagecount.md)
  The number of pages produced by the layout of the web view.
- [var paginationBreakingMode: UIWebView.PaginationBreakingMode](./paginationbreakingmode-swift.property.md)
  The manner in which column- or page-breaking occurs.
- [var paginationMode: UIWebView.PaginationMode](./paginationmode-swift.property.md)
  The layout of content in the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/pagelength)*