# WKNavigationType.linkActivated

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

A link activation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
case linkActivated
```

```c
WKNavigationTypeLinkActivated
```

#### Discussion

This action occurs when the user activates a link with an `href` attribute.

## See Also

### Getting the Navigation Types
- [WKNavigationType.formSubmitted](./formsubmitted.md)
  A request to submit a form.
- [WKNavigationType.backForward](./backforward.md)
  A request for the frame’s next or previous item.
- [WKNavigationType.reload](./reload.md)
  A request to reload the webpage.
- [WKNavigationType.formResubmitted](./formresubmitted.md)
  A request to resubmit a form.
- [WKNavigationType.other](./other.md)
  A navigation request that originates for some other reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationtype/linkactivated)*