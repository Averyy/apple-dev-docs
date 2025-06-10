# callJavaScript(_:arguments:in:contentWorld:)

**Framework**: WebKit  
**Kind**: method

Executes the specified string as an async JavaScript function.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@discardableResult
@MainActor final func callJavaScript(_ functionBody: String, arguments: [String : Any] = [:], in frame: WebPage.FrameInfo? = nil, contentWorld: WKContentWorld? = nil) async throws -> sending Any?
```

#### Return Value

The result of the script evaluation. If your function body doesn’t return an explicit value, `nil` is returned. If your function body explicitly returns `null`, then `NSNull` is returned.

#### Discussion

Don’t format the string in the functionBody parameter as a function-like callable object, as you would in pure JavaScript. Instead, put only the body of the function in the string. For example, the following string shows a valid function body that takes x, y, and z arguments and returns a result.

```javascript
return x ? y : z;
```

If your JavaScript code returns an object with a callable then property, WebKit calls that property on the resulting object and waits for its resolution. If resolution succeeds, WebKit returns the resulting object. If resolution fails, WebKit throws a `WKErrorJavaScriptAsyncFunctionResultRejected` error. If the garbage collector reclaims the object before resolution finishes, WebKit throws a `WKErrorJavaScriptAsyncFunctionResultUnreachable` error.

Because this method calls your JavaScript code asynchronously, you can call `await` on objects with a `then` property inside your function body. The following code example illustrates this technique.

```javascript
var p = new Promise(function (f) {
  window.setTimeout("f(42)", 1000);
});
await p;
return p;
```

## Parameters

- `functionBody`: The JavaScript string to use as the function body. This method treats the string as an anonymous   JavaScript function body and calls it with the named arguments in the   parameter.
- `arguments`: A dictionary of the arguments to pass to the function call. Each key in the dictionary corresponds   to the name of an argument in the   string, and the value of that key is the value to use during   the evaluation of the code. Supported value types are  ,  ,  , and arrays, dictionaries,   and optional values of those types.
- `frame`: The frame in which to evaluate the JavaScript code. Specify   to target the main frame. If this   frame is no longer valid when script evaluation begins, this function throws an error with the    code.
- `contentWorld`: The namespace in which to evaluate the JavaScript code. THis parameter doesn’t apply to changes   you make in the underlying web content, such as the document’s DOM structure. Those changes remain visible to   all scripts, regardless of which content world you specify. For more information about content worlds, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/calljavascript(_:arguments:in:contentworld:))*