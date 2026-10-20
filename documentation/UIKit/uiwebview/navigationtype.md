# UIWebView.NavigationType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constant indicating the user’s action.

**Availability**:
- iOS
- iPadOS

## Declaration

```swift
enum NavigationType
```

```c
enum UIWebViewNavigationType : NSInteger;
```

## Topics

### Constants
- [UIWebView.NavigationType.linkClicked](./navigationtype/linkclicked.md)
  User tapped a link.
- [UIWebView.NavigationType.formSubmitted](./navigationtype/formsubmitted.md)
  User submitted a form.
- [UIWebView.NavigationType.backForward](./navigationtype/backforward.md)
  User tapped the back or forward button.
- [UIWebView.NavigationType.reload](./navigationtype/reload.md)
  User tapped the reload button.
- [UIWebView.NavigationType.formResubmitted](./navigationtype/formresubmitted.md)
  User resubmitted a form.
- [UIWebView.NavigationType.other](./navigationtype/other.md)
  Some other action occurred.
### Initializers
- [init?(rawValue: Int)](./navigationtype/init%28rawvalue%29.md)

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
- [UIWebView.PaginationBreakingMode](./paginationbreakingmode-swift.enum.md)
  The manner in which column- or page-breaking occurs.
- [UIWebView.PaginationMode](./paginationmode-swift.enum.md)
  The layout of content in the web view, which determines the direction that the pages flow.
- [struct UIDataDetectorTypes](../uidatadetectortypes.md)
  Constants that define the types of information to detect in text-based content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/navigationtype)*