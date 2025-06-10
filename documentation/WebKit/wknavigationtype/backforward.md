# WKNavigationType.backForward

**Framework**: WebKit  
**Kind**: case

A request for the frame’s next or previous item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
case backForward
```

#### Discussion

This type of action occurs when the navigation originates from an item in a [`WKBackForwardList`](wkbackforwardlist.md) object.

## See Also

- [WKNavigationType.linkActivated](wknavigationtype/linkactivated.md)
  A link activation.
- [WKNavigationType.formSubmitted](wknavigationtype/formsubmitted.md)
  A request to submit a form.
- [WKNavigationType.reload](wknavigationtype/reload.md)
  A request to reload the webpage.
- [WKNavigationType.formResubmitted](wknavigationtype/formresubmitted.md)
  A request to resubmit a form.
- [WKNavigationType.other](wknavigationtype/other.md)
  A navigation request that originates for some other reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationtype/backforward)*