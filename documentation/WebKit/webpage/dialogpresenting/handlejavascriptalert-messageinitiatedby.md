# handleJavaScriptAlert(message:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

A JavaScript `alert()` function has been invoked.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlejavascriptalert(message:initiatedby:))*