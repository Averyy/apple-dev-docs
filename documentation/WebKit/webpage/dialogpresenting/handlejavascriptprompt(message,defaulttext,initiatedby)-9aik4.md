# handleJavaScriptPrompt(message:defaultText:initiatedBy:)

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
func handleJavaScriptPrompt(message: String, defaultText: String?, initiatedBy frame: WebPage.FrameInfo) async -> WebPage.JavaScriptPromptResult
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlejavascriptprompt(message:defaulttext:initiatedby:)-9aik4)*