# isForMainFrameOnly

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to inject the script into the main frame or all frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var isForMainFrameOnly: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isForMainFrameOnly) BOOL forMainFrameOnly;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the web view injects the script only into the main frame. When the value is [`false`](../../Swift/false.md), the web view injects the script into all frames.

## See Also

### Inspecting Script Information
- [var source: String](./source.md)
  The script’s source code.
- [var injectionTime: WKUserScriptInjectionTime](./injectiontime.md)
  The time at which to inject the script into the webpage.
- [enum WKUserScriptInjectionTime](../wkuserscriptinjectiontime.md)
  Constants for the times at which to inject script content into a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/isformainframeonly)*