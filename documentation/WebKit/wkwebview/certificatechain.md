# certificateChain

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An array of objects forming the certificate chain for the currently committed navigation.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`serverTrust`](./servertrust.md) instead.

## Declaration

```swift
var certificateChain: [Any] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray * certificateChain;
```

## Discussion

Each item in the array is a [`SecCertificate`](../../Security/seccertificate.md) object.

## See Also

### Deprecated
- [func closeAllMediaPresentations()](./closeallmediapresentations%28%29.md)
- [func loadSimulatedRequest(URLRequest, with: URLResponse, responseData: Data) -> WKNavigation](./loadsimulatedrequest%28_,with,responsedata%29.md)
- [func loadSimulatedRequest(URLRequest, withResponseHTML: String) -> WKNavigation](./loadsimulatedrequest%28_,withresponsehtml%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/certificatechain)*