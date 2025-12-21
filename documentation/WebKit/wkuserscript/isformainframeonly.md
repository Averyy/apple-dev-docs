# isForMainFrameOnly

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether to inject the script into the main frame or all frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isForMainFrameOnly: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the web view injects the script only into the main frame. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the web view injects the script into all frames.

## See Also

- [var source: String](wkuserscript/source.md)
  The script’s source code.
- [var injectionTime: WKUserScriptInjectionTime](wkuserscript/injectiontime.md)
  The time at which to inject the script into the webpage.
- [enum WKUserScriptInjectionTime](wkuserscriptinjectiontime.md)
  Constants for the times at which to inject script content into a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/isformainframeonly)*