# evaluateJavaScript(_:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Evaluates the specified JavaScript string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func evaluateJavaScript(_ javaScriptString: String) async throws -> Any?
```

#### Discussion

After evaluating the script, this method executes the completion handler block with either the result of the script evaluation or an error. The completion handler always runs on the app’s main thread.

## Parameters

- `javaScriptString`: The JavaScript string to evaluate.
- `completionHandler`: A handler block to execute when script evaluation finishes. The method calls your block whether script evaluation completes successfully or fails. The block has no return value and takes the following parameters:

## See Also

- [func evaluateJavaScript(String, in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/evaluatejavascript(_:in:in:completionhandler:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func evaluateJavaScript(String, in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/evaluatejavascript(_:in:contentworld:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/callasyncjavascript(_:arguments:in:in:completionhandler:).md)
  Executes the specified string as an asynchronous JavaScript function.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/callasyncjavascript(_:arguments:in:contentworld:).md)
  Executes the specified string as an asynchronous JavaScript function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/evaluatejavascript(_:completionhandler:))*