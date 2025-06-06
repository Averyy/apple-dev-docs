# handlesURLScheme(_:)

**Framework**: Webkit  
**Kind**: method

Returns a Boolean value that indicates whether WebKit natively supports resources with the specified URL scheme.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func handlesURLScheme(_ urlScheme: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if WebKit provides native support for the URL scheme, or [`false`](https://developer.apple.com/documentation/swift/false) if it doesn’t.

## Parameters

- `urlScheme`: The URL scheme associated with the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/handlesurlscheme(_:))*