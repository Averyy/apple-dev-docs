# evaluateJavaScript:inFrame:inContentWorld:completionHandler:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Evaluates the specified JavaScript string in the specified frame and content world.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (void) evaluateJavaScript:(NSString *) javaScriptString inFrame:(WKFrameInfo *) frame inContentWorld:(WKContentWorld *) contentWorld completionHandler:(void (^)(id, NSError *)) completionHandler;
```

## Discussion

The evaluation of your script may change global state in a way that remains visible to subsequent JavaScript code. The changes are restricted to scripts you execute using the same [`WKContentWorld`](../wkcontentworld.md) object. In fact, you can use this method to set up global state in the specified content world, and use that state in subsequent JavaScript code. If you do so, consider using [`callAsyncJavaScript:arguments:inFrame:inContentWorld:completionHandler:`](./callasyncjavascript_arguments_inframe_incontentworld_completionhandler_.md) for more flexible interactions with the JavaScript programming model.

After evaluating the script, this method executes the completion handler block with either the result of the script evaluation or an error. The completion handler always runs on the app’s main thread.

## Parameters

- `javaScriptString`: The JavaScript string to evaluate.
- `frame`: The frame in which to evaluate the JavaScript string. Specify `nil` to target the main frame. If this frame is no longer valid when script evaluation begins, this method returns a [`WKError.Code.javaScriptInvalidFrameTarget`](../wkerror/code/javascriptinvalidframetarget.md) error.
- `contentWorld`: The namespace in which to evaluate the JavaScript string. This parameter doesn’t apply to changes you make to the underlying web content, such as the document’s DOM structure. Those changes remain visible to all scripts, regardless of which content world you specify. For more information about content worlds, see [`WKContentWorld`](../wkcontentworld.md).
- `completionHandler`: A handler block to execute when script evaluation finishes. The method calls your block whether script evaluation completes successfully or fails. The block has no return value and takes the following parameters:

  - **object**: The result of the script evaluation, or `nil` if an error occurred.
  - **error**: `nil` on success, or an error object with information about the problem.

## See Also

### Executing JavaScript
- [func evaluateJavaScript(String, completionHandler: ((Any?, (any Error)?) -> Void)?)](./evaluatejavascript%28_,completionhandler%29.md)
  Evaluates the specified JavaScript string.
- [- callAsyncJavaScript:arguments:inFrame:inContentWorld:completionHandler:](./callasyncjavascript_arguments_inframe_incontentworld_completionhandler_.md)
  Executes the specified string as an asynchronous JavaScript function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/evaluatejavascript:inframe:incontentworld:completionhandler:)*