# callAsyncJavaScript(_:arguments:in:contentWorld:)

**Framework**: Webkit  
**Kind**: method

Executes the specified string as an asynchronous JavaScript function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func callAsyncJavaScript(_ functionBody: String, arguments: [String : Any] = [:], in frame: WKFrameInfo? = nil, contentWorld: WKContentWorld) async throws -> Any?
```

#### Return Value

The result of the script evaluation, or an error object that contains information about the problem that occurred. If your function body doesn’t return an explicit value, WebKit returns `nil` on success. If your function explicitly returns `null`, WebKit returns that value as an [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object.

#### Discussion

Don’t format the string in the `functionBody` parameter as a function-like callable object, as you would in pure JavaScript. Instead, put only the body of the function in the string. For example, the following string shows a valid function body that takes `x`, `y`, and `z` arguments and returns a result.

```javascript
return x ? y : z
```

If your JavaScript code returns an object with a callable `then` property, WebKit calls that property on the resulting object and waits for its resolution. If resolution succeeds, WebKit passes the resulting object to your completion handler. If resolution fails, WebKit returns a `WKErrorJavaScriptAsyncFunctionResultRejected` error to your completion handler. Examine the userInfo dictionary of the error object to determine the reason for the object’s rejection. If the garbage collector reclaims the object before resolution finishes, WebKit returns a `WKErrorJavaScriptAsyncFunctionResultUnreachable` error to your completion handler.

Because this method calls your JavaScript code asynchronously, you can call `await` on objects with a `then` property inside your function body. The following code example illustrates this technique.

```javascript
var p = new Promise(function (f) {
   window.setTimeout("f(42)", 1000);
});
await p;
return p;
```

## Parameters

- `functionBody`: The JavaScript string to use as the function body. This method treats the string as an anonymous JavaScript function body and calls it with the named arguments in the   parameter.
- `arguments`: A dictionary of the arguments to pass to the function call. Each key in the dictionary corresponds to the name of an argument in the   string, and the value of that key is the value to use during the evaluation of the code. Supported value types are  ,  ,  ,  ,  , or  . All items in an array or dictionary must also be one of the supported types.
- `frame`: The frame in which to evaluate the JavaScript code. Specify   to target the main frame. If this frame is no longer valid when script evaluation begins, this method returns a   error.
- `contentWorld`: The namespace in which to evaluate the JavaScript code. This parameter doesn’t apply to changes you make to the underlying web content, such as the document’s DOM structure. Those changes remain visible to all scripts, regardless of which content world you specify. For more information about content worlds, see  .

## See Also

- [func evaluateJavaScript(String, completionHandler: ((Any?, (any Error)?) -> Void)?)](wkwebview/evaluatejavascript(_:completionhandler:).md)
  Evaluates the specified JavaScript string.
- [func evaluateJavaScript(String, in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/evaluatejavascript(_:in:in:completionhandler:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func evaluateJavaScript(String, in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/evaluatejavascript(_:in:contentworld:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/callasyncjavascript(_:arguments:in:in:completionhandler:).md)
  Executes the specified string as an asynchronous JavaScript function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/callasyncjavascript(_:arguments:in:contentworld:))*