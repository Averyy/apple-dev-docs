# source

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The script’s source code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var source: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * source;
```

## See Also

### Inspecting Script Information
- [var injectionTime: WKUserScriptInjectionTime](./injectiontime.md)
  The time at which to inject the script into the webpage.
- [enum WKUserScriptInjectionTime](../wkuserscriptinjectiontime.md)
  Constants for the times at which to inject script content into a webpage.
- [var isForMainFrameOnly: Bool](./isformainframeonly.md)
  A Boolean value that indicates whether to inject the script into the main frame or all frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/source)*