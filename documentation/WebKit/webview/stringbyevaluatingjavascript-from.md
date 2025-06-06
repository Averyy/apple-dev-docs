# stringByEvaluatingJavaScript(from:)

**Framework**: Webkit  
**Kind**: method

Returns the result of running a script.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func stringByEvaluatingJavaScript(from script: String!) -> String!
```

#### Return Value

The result of running a JavaScript specified by `script`, or an empty string if the script failed.

## Parameters

- `script`: The script to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/stringbyevaluatingjavascript(from:))*