# qualifiedServerTrust

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var qualifiedServerTrust: SecTrust? { get }
```

```objc
@property (nonatomic, readonly, nullable) SecTrustRef qualifiedServerTrust;
```

## Discussion

A SecTrustRef with a 2-QWAC for the currently committed navigation.

Since a separate fetch is needed to get the 2-QWAC data, this becomes available after the serverTrust.  It will only become available if the server has a valid 2-QWAC. This property is key-value observing (KVO) compliant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/qualifiedservertrust)*