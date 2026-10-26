# handleJavaScriptConfirm(message:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

By default, this method immediately returns with a result of `.cancel`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func handleJavaScriptConfirm(message: String, initiatedBy frame: WebPage.FrameInfo) async -> WebPage.JavaScriptConfirmResult
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlejavascriptconfirm(message:initiatedby:)-86j9x)*