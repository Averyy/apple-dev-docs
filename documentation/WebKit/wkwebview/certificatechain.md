# certificateChain

**Framework**: WebKit  
**Kind**: property

An array of objects forming the certificate chain for the currently committed navigation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var certificateChain: [Any] { get }
```

#### Discussion

Each item in the array is a [`SecCertificate`](https://developer.apple.com/documentation/Security/SecCertificate) object.

## See Also

- [func closeAllMediaPresentations()](wkwebview/closeallmediapresentations.md)
- [func loadSimulatedRequest(URLRequest, with: URLResponse, responseData: Data) -> WKNavigation](wkwebview/loadsimulatedrequest(_:with:responsedata:).md)
- [func loadSimulatedRequest(URLRequest, withResponseHTML: String) -> WKNavigation](wkwebview/loadsimulatedrequest(_:withresponsehtml:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/certificatechain)*