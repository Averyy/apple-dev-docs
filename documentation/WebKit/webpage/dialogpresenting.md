# WebPage.DialogPresenting

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

Allows providing custom behavior to handle JavaScript actions and provide a response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol DialogPresenting
```

#### Overview

Typically when handling these, some UI should be presented to the user for them to provide a response, which will then be communicated back to JavaScript.

When these methods are invoked, JavaScript is blocked until the async method returns.

## Topics

### Instance Methods
- [func handleFileInputPrompt(parameters: WKOpenPanelParameters, initiatedBy: WebPage.FrameInfo) async -> WebPage.FileInputPromptResult](./dialogpresenting/handlefileinputprompt%28parameters,initiatedby%29.md)
  Returns the result of handling a JavaScript request to open files.
- [func handleJavaScriptAlert(message: String, initiatedBy: WebPage.FrameInfo) async](./dialogpresenting/handlejavascriptalert%28message,initiatedby%29.md)
  A JavaScript `alert()` function has been invoked.
- [func handleJavaScriptConfirm(message: String, initiatedBy: WebPage.FrameInfo) async -> WebPage.JavaScriptConfirmResult](./dialogpresenting/handlejavascriptconfirm%28message,initiatedby%29.md)
  A JavaScript `confirm()` function has been invoked.
- [func handleJavaScriptPrompt(message: String, defaultText: String?, initiatedBy: WebPage.FrameInfo) async -> WebPage.JavaScriptPromptResult](./dialogpresenting/handlejavascriptprompt%28message,defaulttext,initiatedby%29.md)
  A JavaScript `prompt()` function has been invoked.

## See Also

### Customizing JavaScript dialogs
- [WebPage.FileInputPromptResult](./fileinputpromptresult.md)
  The result of handling a JavaScript open invocation.
- [WebPage.JavaScriptConfirmResult](./javascriptconfirmresult.md)
  The result of handling a JavaScript confirm invocation.
- [WebPage.JavaScriptPromptResult](./javascriptpromptresult.md)
  The result of handling a JavaScript confirm invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting)*