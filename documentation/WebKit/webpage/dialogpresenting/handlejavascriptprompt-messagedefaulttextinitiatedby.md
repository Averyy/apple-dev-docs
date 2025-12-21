# handleJavaScriptPrompt(message:defaultText:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

A JavaScript `prompt()` function has been invoked.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func handleJavaScriptPrompt(message: String, defaultText: String?, initiatedBy frame: WebPage.FrameInfo) async -> WebPage.JavaScriptPromptResult
```

#### Return Value

The result of handling the invocation; if the result is affirmative, the response will include some text returned to JavaScript.

## Parameters

- `message`: The message provided by JavaScript.
- `defaultText`: The initial text provided by JavaScript, intended to be displayed in some text entry field.
- `frame`: Information about the frame whose JavaScript process initiated this call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlejavascriptprompt(message:defaulttext:initiatedby:))*