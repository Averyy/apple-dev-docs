# stringByEvaluatingJavaScript(from:)

**Framework**: UIKit  
**Kind**: method

Returns the result of running a JavaScript script.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
func stringByEvaluatingJavaScript(from script: String) -> String?
```

#### Return Value

The result of running the JavaScript script passed in the `script` parameter, or `nil` if the script fails.

#### Discussion

New apps should instead use the [`evaluateJavaScript(_:completionHandler:)`](https://developer.apple.com/documentation/WebKit/WKWebView/evaluateJavaScript(_:completionHandler:)) method from the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class. Legacy apps should adopt that method if possible.

> ❗ **Important**:  The [`stringByEvaluatingJavaScript(from:)`](uiwebview/stringbyevaluatingjavascript(from:).md) method waits synchronously for JavaScript evaluation to complete. If you load web content whose JavaScript code you have not vetted, invoking this method could hang your app. Best practice is to adopt the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class and use its [`evaluateJavaScript(_:completionHandler:)`](https://developer.apple.com/documentation/WebKit/WKWebView/evaluateJavaScript(_:completionHandler:)) method instead.

 The [`stringByEvaluatingJavaScript(from:)`](uiwebview/stringbyevaluatingjavascript(from:).md) method waits synchronously for JavaScript evaluation to complete. If you load web content whose JavaScript code you have not vetted, invoking this method could hang your app. Best practice is to adopt the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class and use its [`evaluateJavaScript(_:completionHandler:)`](https://developer.apple.com/documentation/WebKit/WKWebView/evaluateJavaScript(_:completionHandler:)) method instead.

## Parameters

- `script`: The JavaScript script to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/stringbyevaluatingjavascript(from:))*