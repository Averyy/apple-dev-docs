# WKDialogResult.handled

**Framework**: WebKit  
**Kind**: case

A result that indicates the delegate displayed the first use message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
case handled
```

#### Discussion

This result tells the system that it does not need to check any more whether it needs to display the Lockdown Mode first use message.

## See Also

- [WKDialogResult.askAgain](wkdialogresult/askagain.md)
  A result that indicates the delegate didn’t display a message, so other web views should check again.
- [WKDialogResult.showDefault](wkdialogresult/showdefault.md)
  A result that indicates the delegate didn’t display a message, so the web view should show the default Lockdown Mode message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdialogresult/handled)*