# evaluateJavaScript(_:in:in:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Evaluates a JavaScript string in the context of the specified frame and content world.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func evaluateJavaScript(_ javaScript: String, in frame: WKFrameInfo? = nil, in contentWorld: WKContentWorld, completionHandler: (@MainActor (Result<Any, any Error>) -> Void)? = nil)
```

#### Discussion

The evaluation of your script may change global state in a way that remains visible to subsequent JavaScript code. The changes are restricted to scripts you execute using the same [`WKContentWorld`](wkcontentworld.md) object. In fact, you can use this method to set up global state in the specified content world, and use that state in subsequent JavaScript code. If you do so, consider using [`callAsyncJavaScript(_:arguments:in:in:completionHandler:)`](wkwebview/callasyncjavascript(_:arguments:in:in:completionhandler:).md) for more flexible interactions with the JavaScript programming model.

After evaluating the script, this method executes the completion handler block with either the result of the script evaluation or an error. The completion handler always runs on the app’s main thread.

## Parameters

- `javaScript`: The JavaScript string to evaluate.
- `frame`: The frame in which to evaluate the JavaScript code. Specify   to target the main frame. If this frame is no longer valid when script evaluation begins, this method returns a   error.
- `contentWorld`: The namespace in which to evaluate the JavaScript code. This parameter doesn’t apply to changes you make to the underlying web content, such as the document’s DOM structure. Those changes remain visible to all scripts, regardless of which content world you specify. For more information about content worlds, see  .
- `completionHandler`: A handler block to execute when script evaluation finishes. The method calls your block whether script evaluation completes successfully or fails. The block has no return value and takes the following parameters:

## See Also

- [func evaluateJavaScript(String, completionHandler: ((Any?, (any Error)?) -> Void)?)](wkwebview/evaluatejavascript(_:completionhandler:).md)
  Evaluates the specified JavaScript string.
- [func evaluateJavaScript(String, in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/evaluatejavascript(_:in:contentworld:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/callasyncjavascript(_:arguments:in:in:completionhandler:).md)
  Executes the specified string as an asynchronous JavaScript function.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/callasyncjavascript(_:arguments:in:contentworld:).md)
  Executes the specified string as an asynchronous JavaScript function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/evaluatejavascript(_:in:in:completionhandler:))*