# WebPage.DialogPresenting

**Framework**: WebKit  
**Kind**: protocol

Allows providing custom behavior to handle JavaScript actions and provide a response.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
protocol DialogPresenting
```

#### Overview

Typically when handling these, some UI should be presented to the user for them to provide a response, which will then be communicated back to JavaScript.

When these methods are invoked, JavaScript is blocked until the async method returns.

## Topics

### Instance Methods
- [func handleFileInputPrompt(parameters: WKOpenPanelParameters, initiatedBy: WebPage.FrameInfo) async -> WebPage.FileInputPromptResult](webpage/dialogpresenting/handlefileinputprompt(parameters:initiatedby:).md)
  Returns the result of handling a JavaScript request to open files.
- [func handleJavaScriptAlert(message: String, initiatedBy: WebPage.FrameInfo) async](webpage/dialogpresenting/handlejavascriptalert(message:initiatedby:).md)
  A JavaScript `alert()` function has been invoked.
- [func handleJavaScriptConfirm(message: String, initiatedBy: WebPage.FrameInfo) async -> WebPage.JavaScriptConfirmResult](webpage/dialogpresenting/handlejavascriptconfirm(message:initiatedby:).md)
  A JavaScript `confirm()` function has been invoked.
- [func handleJavaScriptPrompt(message: String, defaultText: String?, initiatedBy: WebPage.FrameInfo) async -> WebPage.JavaScriptPromptResult](webpage/dialogpresenting/handlejavascriptprompt(message:defaulttext:initiatedby:).md)
  A JavaScript `prompt()` function has been invoked.

## See Also

- [WebPage.FileInputPromptResult](webpage/fileinputpromptresult.md)
  The result of handling a JavaScript open invocation.
- [WebPage.JavaScriptConfirmResult](webpage/javascriptconfirmresult.md)
  The result of handling a JavaScript confirm invocation.
- [WebPage.JavaScriptPromptResult](webpage/javascriptpromptresult.md)
  The result of handling a JavaScript confirm invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting)*