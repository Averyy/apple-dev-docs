# handleFileInputPrompt(parameters:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Returns the result of handling a JavaScript request to open files.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func handleFileInputPrompt(parameters: WKOpenPanelParameters, initiatedBy frame: WebPage.FrameInfo) async -> WebPage.FileInputPromptResult
```

#### Return Value

The result of handling the invocation; if the result is affirmative, the response will include a set of files returned to JavaScript.

## Parameters

- `parameters`: The options to use for the file dialog.
- `frame`: Information about the frame whose JavaScript process initiated this call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlefileinputprompt(parameters:initiatedby:))*