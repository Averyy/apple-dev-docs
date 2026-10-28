# stringByEvaluatingJavaScript(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the result of running a JavaScript script.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
func stringByEvaluatingJavaScript(from script: String) -> String?
```

```objc
- (NSString *) stringByEvaluatingJavaScriptFromString:(NSString *) script;
```

## Return Value

The result of running the JavaScript script passed in the `script` parameter, or `nil` if the script fails.

## Discussion

New apps should instead use the [`evaluateJavaScript(_:completionHandler:)`](../../WebKit/wkwebview/evaluatejavascript%28_,completionhandler%29.md) method from the [`WKWebView`](../../WebKit/wkwebview.md) class. Legacy apps should adopt that method if possible.

> ❗ **Important**:  The [`stringByEvaluatingJavaScript(from:)`](./stringbyevaluatingjavascript%28from%29.md) method waits synchronously for JavaScript evaluation to complete. If you load web content whose JavaScript code you have not vetted, invoking this method could hang your app. Best practice is to adopt the [`WKWebView`](../../WebKit/wkwebview.md) class and use its [`evaluateJavaScript(_:completionHandler:)`](../../WebKit/wkwebview/evaluatejavascript%28_,completionhandler%29.md) method instead.

## Parameters

- `script`: The JavaScript script to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/stringbyevaluatingjavascript(from:))*