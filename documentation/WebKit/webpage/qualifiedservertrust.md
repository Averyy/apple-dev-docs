# qualifiedServerTrust

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The trust management object for the 2-QWAC of the currently committed navigation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var qualifiedServerTrust: SecTrust? { get }
```

## Discussion

A 2-QWAC binds a qualified website authentication certificate to the TLS certificate the webpage was served with. Since a separate fetch is needed to get the 2-QWAC data, this value becomes available after [`serverTrust`](./servertrust.md), and only if the server has a valid 2-QWAC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/qualifiedservertrust)*