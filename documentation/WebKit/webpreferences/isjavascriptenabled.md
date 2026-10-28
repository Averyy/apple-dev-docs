# isJavaScriptEnabled

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether or not the web view allows JavaScript.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var isJavaScriptEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isJavaScriptEnabled) BOOL javaScriptEnabled;
```

## Discussion

Set to [`true`](../../Swift/true.md) if the web view should allow JavaScript, otherwise [`false`](../../Swift/false.md).

## See Also

### Enabling JavaScript
- [var javaScriptCanOpenWindowsAutomatically: Bool](./javascriptcanopenwindowsautomatically.md)
  A Boolean that indicates whether or not the web view allows JavaScript to open windows automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/isjavascriptenabled)*