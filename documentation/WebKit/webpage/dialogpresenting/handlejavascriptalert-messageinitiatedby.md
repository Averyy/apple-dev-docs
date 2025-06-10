# handleJavaScriptAlert(message:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

A JavaScript `alert()` function has been invoked.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

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