# WKNavigationType.formResubmitted

**Framework**: Webkit  
**Kind**: case

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

#### Discussion

This type of action occurs when the forward or backward navigation causes the web view to resubmit a form. It also occurs when a reload operation causes the resubmission of the form.

## See Also

- [WKNavigationType.linkActivated](wknavigationtype/linkactivated.md)
  A link activation.
- [WKNavigationType.formSubmitted](wknavigationtype/formsubmitted.md)
  A request to submit a form.
- [WKNavigationType.backForward](wknavigationtype/backforward.md)
  A request for the frame’s next or previous item.
- [WKNavigationType.reload](wknavigationtype/reload.md)
  A request to reload the webpage.
- [WKNavigationType.other](wknavigationtype/other.md)
  A navigation request that originates for some other reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationtype/formresubmitted)*