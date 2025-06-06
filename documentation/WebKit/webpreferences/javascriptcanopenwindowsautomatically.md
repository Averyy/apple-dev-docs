# javaScriptCanOpenWindowsAutomatically

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether or not the web view allows JavaScript to open windows automatically.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var javaScriptCanOpenWindowsAutomatically: Bool { get set }
```

#### Discussion

Set to [`true`](https://developer.apple.com/documentation/swift/true) if the web view should allow JavaScript to open windows automatically, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

Explicit calls to a JavaScript window opener that are activated by user action (such as a button click) are not affected by this setting.

## See Also

- [var isJavaScriptEnabled: Bool](webpreferences/isjavascriptenabled.md)
  A Boolean that indicates whether or not the web view allows JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/javascriptcanopenwindowsautomatically)*