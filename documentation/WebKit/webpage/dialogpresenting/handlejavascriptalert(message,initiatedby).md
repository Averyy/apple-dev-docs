# handleJavaScriptAlert(message:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A JavaScript `alert()` function has been invoked.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func handleJavaScriptAlert(message: String, initiatedBy frame: WebPage.FrameInfo) async
```

## Parameters

- `message`: The message provided by JavaScript.
- `frame`: Information about the frame whose JavaScript process initiated this call.

## Default Implementations

### WebPage.DialogPresenting Implementations
- [func handleJavaScriptAlert(message: String, initiatedBy: WebPage.FrameInfo) async](./handlejavascriptalert%28message,initiatedby%29-32742.md)
  By default, this method immediately returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlejavascriptalert(message:initiatedby:))*