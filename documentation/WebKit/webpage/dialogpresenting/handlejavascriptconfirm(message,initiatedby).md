# handleJavaScriptConfirm(message:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A JavaScript `confirm()` function has been invoked.

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

#### Return Value

The result of handling the invocation.

## Parameters

- `message`: The message provided by JavaScript.
- `frame`: Information about the frame whose JavaScript process initiated this call.

## Default Implementations

### WebPage.DialogPresenting Implementations
- [func handleJavaScriptConfirm(message: String, initiatedBy: WebPage.FrameInfo) async -> WebPage.JavaScriptConfirmResult](./handlejavascriptconfirm%28message,initiatedby%29-86j9x.md)
  By default, this method immediately returns with a result of `.cancel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlejavascriptconfirm(message:initiatedby:))*