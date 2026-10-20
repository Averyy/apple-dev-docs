# stringByEvaluatingJavaScript(from:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the result of running a script.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func stringByEvaluatingJavaScript(from script: String!) -> String!
```

```objc
- (NSString *) stringByEvaluatingJavaScriptFromString:(NSString *) script;
```

#### Return Value

The result of running a JavaScript specified by `script`, or an empty string if the script failed.

## Parameters

- `script`: The script to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/stringbyevaluatingjavascript(from:))*