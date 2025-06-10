# evaluateJavaScript(_:in:contentWorld:)

**Framework**: WebKit  
**Kind**: method

Evaluates a JavaScript string in the context of the specified frame and content world.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func evaluateJavaScript(_ javaScript: String, in frame: WKFrameInfo? = nil, contentWorld: WKContentWorld) async throws -> Any?
```

#### Return Value

The result of the script evaluation, or an error object that contains information about the problem that occurred. If your function body doesn’t return an explicit value, WebKit returns `nil` on success. If your function explicitly returns `null`, WebKit returns that value as an [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object.

## Parameters

- `javaScript`: The JavaScript string to evaluate.
- `frame`: The frame in which to evaluate the JavaScript code. Specify   to target the main frame. If this frame is no longer valid when script evaluation begins, this method returns a   error.
- `contentWorld`: The namespace in which to evaluate the JavaScript code. This parameter doesn’t apply to changes you make to the underlying web content, such as the document’s DOM structure. Those changes remain visible to all scripts, regardless of which content world you specify. For more information about content worlds, see  .

## See Also

- [func evaluateJavaScript(String, completionHandler: ((Any?, (any Error)?) -> Void)?)](wkwebview/evaluatejavascript(_:completionhandler:).md)
  Evaluates the specified JavaScript string.
- [func evaluateJavaScript(String, in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/evaluatejavascript(_:in:in:completionhandler:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/callasyncjavascript(_:arguments:in:in:completionhandler:).md)
  Executes the specified string as an asynchronous JavaScript function.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/callasyncjavascript(_:arguments:in:contentworld:).md)
  Executes the specified string as an asynchronous JavaScript function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/evaluatejavascript(_:in:contentworld:))*