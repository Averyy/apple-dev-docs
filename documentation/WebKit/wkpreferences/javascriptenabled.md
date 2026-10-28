# javaScriptEnabled

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether JavaScript is enabled.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use WKWebpagePreferences.allowsContentJavaScript to disable content JavaScript on a per-navigation basis

## Declaration

```swift
var javaScriptEnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL javaScriptEnabled;
```

## Discussion

The default value is [`true`](../../Swift/true.md). Setting this property to [`false`](../../Swift/false.md) disables JavaScripts that are loaded or executed by the webpage. This setting does not affect user scripts. See [`WKUserContentController`](../wkusercontentcontroller.md).

## See Also

### Deprecated
- [var javaEnabled: Bool](./javaenabled.md)
  A Boolean value that indicates whether Java is enabled.
- [var plugInsEnabled: Bool](./pluginsenabled.md)
  A Boolean value that indicates whether plug-ins are enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/javascriptenabled)*