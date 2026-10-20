# loadSimulatedRequest(_:withResponseHTML:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.0+ - Deprecated in 15.0
- iPadOS 15.0+ - Deprecated in 15.0
- Mac Catalyst 15.0+ - Deprecated in 15.0
- macOS 12.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`loadSimulatedRequest(_:responseHTML:)`](./loadsimulatedrequest%28_,responsehtml%29.md) instead.

## Declaration

```swift
func loadSimulatedRequest(_ request: URLRequest, withResponseHTML string: String) -> WKNavigation
```

```objc
- (WKNavigation *) loadSimulatedRequest:(NSURLRequest *) request withResponseHTMLString:(NSString *) string;
```

## See Also

### Deprecated
- [var certificateChain: [Any]](./certificatechain.md)
  An array of objects forming the certificate chain for the currently committed navigation.
- [func closeAllMediaPresentations()](./closeallmediapresentations%28%29.md)
- [func loadSimulatedRequest(URLRequest, with: URLResponse, responseData: Data) -> WKNavigation](./loadsimulatedrequest%28_,with,responsedata%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/loadsimulatedrequest(_:withresponsehtml:))*