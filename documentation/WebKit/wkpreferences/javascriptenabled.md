# javaScriptEnabled

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether JavaScript is enabled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var javaScriptEnabled: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) disables JavaScripts that are loaded or executed by the webpage. This setting does not affect user scripts. See [`WKUserContentController`](wkusercontentcontroller.md).

## See Also

- [var javaEnabled: Bool](wkpreferences/javaenabled.md)
  A Boolean value that indicates whether Java is enabled.
- [var plugInsEnabled: Bool](wkpreferences/pluginsenabled.md)
  A Boolean value that indicates whether plug-ins are enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/javascriptenabled)*