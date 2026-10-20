# loadSimulatedRequest(_:with:responseData:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.0+ - Deprecated in 15.0
- iPadOS 15.0+ - Deprecated in 15.0
- Mac Catalyst 15.0+ - Deprecated in 15.0
- macOS 12.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`loadSimulatedRequest(_:response:responseData:)`](./loadsimulatedrequest%28_,response,responsedata%29.md) instead.

## Declaration

```swift
func loadSimulatedRequest(_ request: URLRequest, with response: URLResponse, responseData data: Data) -> WKNavigation
```

```objc
- (WKNavigation *) loadSimulatedRequest:(NSURLRequest *) request withResponse:(NSURLResponse *) response responseData:(NSData *) data;
```

## See Also

### Deprecated
- [var certificateChain: [Any]](./certificatechain.md)
  An array of objects forming the certificate chain for the currently committed navigation.
- [func closeAllMediaPresentations()](./closeallmediapresentations%28%29.md)
- [func loadSimulatedRequest(URLRequest, withResponseHTML: String) -> WKNavigation](./loadsimulatedrequest%28_,withresponsehtml%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/loadsimulatedrequest(_:with:responsedata:))*