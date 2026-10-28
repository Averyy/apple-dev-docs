# unreachableURL

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The data source’s unreachable URL.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var unreachableURL: URL! { get }
```

```objc
@property (nonatomic, strong, readonly) NSURL * unreachableURL;
```

## Discussion

The data source has an unreachable URL if it was created using the ``WebFrame/loadAlternateHTMLString(_:baseURL:forUnreachableURL:)```WebFrame` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/unreachableurl)*