# handlesURLScheme(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether WebKit natively supports resources with the specified URL scheme.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class func handlesURLScheme(_ urlScheme: String) -> Bool
```

```objc
+ (BOOL) handlesURLScheme:(NSString *) urlScheme;
```

## Return Value

[`true`](../../Swift/true.md) if WebKit provides native support for the URL scheme, or [`false`](../../Swift/false.md) if it doesn’t.

## Parameters

- `urlScheme`: The URL scheme associated with the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/handlesurlscheme(_:))*