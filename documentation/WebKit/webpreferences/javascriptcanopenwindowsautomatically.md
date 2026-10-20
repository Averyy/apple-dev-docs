# javaScriptCanOpenWindowsAutomatically

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether or not the web view allows JavaScript to open windows automatically.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var javaScriptCanOpenWindowsAutomatically: Bool { get set }
```

```objc
@property (nonatomic) BOOL javaScriptCanOpenWindowsAutomatically;
```

#### Discussion

Set to [`true`](../../Swift/true.md) if the web view should allow JavaScript to open windows automatically, otherwise [`false`](../../Swift/false.md).

Explicit calls to a JavaScript window opener that are activated by user action (such as a button click) are not affected by this setting.

## See Also

### Enabling JavaScript
- [var isJavaScriptEnabled: Bool](./isjavascriptenabled.md)
  A Boolean that indicates whether or not the web view allows JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/javascriptcanopenwindowsautomatically)*