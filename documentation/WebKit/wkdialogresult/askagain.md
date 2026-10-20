# WKDialogResult.askAgain

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

A result that indicates the delegate didn’t display a message, so other web views should check again.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
case askAgain
```

```c
WKDialogResultAskAgain
```

## See Also

### First use dialog results
- [WKDialogResult.handled](./handled.md)
  A result that indicates the delegate displayed the first use message.
- [WKDialogResult.showDefault](./showdefault.md)
  A result that indicates the delegate didn’t display a message, so the web view should show the default Lockdown Mode message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdialogresult/askagain)*