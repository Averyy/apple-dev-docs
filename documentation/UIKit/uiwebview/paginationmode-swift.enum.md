# UIWebView.PaginationMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The layout of content in the web view, which determines the direction that the pages flow.

**Availability**:
- iOS
- iPadOS

## Declaration

```swift
enum PaginationMode
```

```c
enum UIWebPaginationMode : NSInteger;
```

## Topics

### Constants
- [UIWebView.PaginationMode.unpaginated](./paginationmode-swift.enum/unpaginated.md)
  Content appears as one long scrolling view with no distinct pages.
- [UIWebView.PaginationMode.leftToRight](./paginationmode-swift.enum/lefttoright.md)
  Content is broken up into pages that flow from left to right.
- [UIWebView.PaginationMode.topToBottom](./paginationmode-swift.enum/toptobottom.md)
  Content is broken up into pages that flow from top to bottom.
- [UIWebView.PaginationMode.bottomToTop](./paginationmode-swift.enum/bottomtotop.md)
  Content is broken up into pages that flow from bottom to top.
- [UIWebView.PaginationMode.rightToLeft](./paginationmode-swift.enum/righttoleft.md)
  Content is broken up into pages that flow from right to left.
### Initializers
- [init?(rawValue: Int)](./paginationmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIWebView.NavigationType](./navigationtype.md)
  Constant indicating the user’s action.
- [UIWebView.PaginationBreakingMode](./paginationbreakingmode-swift.enum.md)
  The manner in which column- or page-breaking occurs.
- [struct UIDataDetectorTypes](../uidatadetectortypes.md)
  Constants that define the types of information to detect in text-based content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/paginationmode-swift.enum)*