# handleFileInputPrompt(parameters:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Returns the result of handling a JavaScript request to open files.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func handleFileInputPrompt(parameters: WKOpenPanelParameters, initiatedBy frame: WebPage.FrameInfo) async -> WebPage.FileInputPromptResult
```

#### Return Value

The result of handling the invocation; if the result is affirmative, the response will include a set of files returned to JavaScript.

## Parameters

- `parameters`: The options to use for the file dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/dialogpresenting/handlefileinputprompt(parameters:initiatedby:))*