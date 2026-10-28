# injectionTime

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The time at which to inject the script into the webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var injectionTime: WKUserScriptInjectionTime { get }
```

```objc
@property (nonatomic, readonly) WKUserScriptInjectionTime injectionTime;
```

## Discussion

The value is one of the constants of the enumerated type [`WKUserScriptInjectionTime`](../wkuserscriptinjectiontime.md).

## See Also

### Inspecting Script Information
- [var source: String](./source.md)
  The script’s source code.
- [enum WKUserScriptInjectionTime](../wkuserscriptinjectiontime.md)
  Constants for the times at which to inject script content into a webpage.
- [var isForMainFrameOnly: Bool](./isformainframeonly.md)
  A Boolean value that indicates whether to inject the script into the main frame or all frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/injectiontime)*