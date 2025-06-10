# WKUserScriptInjectionTime

**Framework**: WebKit  
**Kind**: enum

Constants for the times at which to inject script content into a webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
enum WKUserScriptInjectionTime
```

## Topics

### Script-Injection Times
- [WKUserScriptInjectionTime.atDocumentStart](wkuserscriptinjectiontime/atdocumentstart.md)
  A constant to inject the script after the creation of the webpage’s document element, but before loading any other content.
- [WKUserScriptInjectionTime.atDocumentEnd](wkuserscriptinjectiontime/atdocumentend.md)
  A constant to inject the script after the document finishes loading, but before loading any other subresources.
### Initializers
- [init?(rawValue: Int)](wkuserscriptinjectiontime/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var source: String](wkuserscript/source.md)
  The script’s source code.
- [var injectionTime: WKUserScriptInjectionTime](wkuserscript/injectiontime.md)
  The time at which to inject the script into the webpage.
- [var isForMainFrameOnly: Bool](wkuserscript/isformainframeonly.md)
  A Boolean value that indicates whether to inject the script into the main frame or all frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscriptinjectiontime)*