# WKDialogResult.showDefault

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

A result that indicates the delegate didn’t display a message, so the web view should show the default Lockdown Mode message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
case showDefault
```

```c
WKDialogResultShowDefault
```

## See Also

### First use dialog results
- [WKDialogResult.askAgain](./askagain.md)
  A result that indicates the delegate didn’t display a message, so other web views should check again.
- [WKDialogResult.handled](./handled.md)
  A result that indicates the delegate displayed the first use message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdialogresult/showdefault)*