# WKNavigationType.formResubmitted

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

A request to resubmit a form.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
case formResubmitted
```

```c
WKNavigationTypeFormResubmitted
```

#### Discussion

This type of action occurs when the forward or backward navigation causes the web view to resubmit a form. It also occurs when a reload operation causes the resubmission of the form.

## See Also

### Getting the Navigation Types
- [WKNavigationType.linkActivated](./linkactivated.md)
  A link activation.
- [WKNavigationType.formSubmitted](./formsubmitted.md)
  A request to submit a form.
- [WKNavigationType.backForward](./backforward.md)
  A request for the frame’s next or previous item.
- [WKNavigationType.reload](./reload.md)
  A request to reload the webpage.
- [WKNavigationType.other](./other.md)
  A navigation request that originates for some other reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationtype/formresubmitted)*