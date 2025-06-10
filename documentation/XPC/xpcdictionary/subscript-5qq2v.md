# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set an `XPCEndpoint` value in this dictionary.

**Availability**:
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
subscript(key: String) -> XPCListener.Endpoint? { get set }
```

#### Return Value

A previously-set endpoint value. If no endpoint was previously set for `key`, returns `nil`.

## Parameters

- `key`: The key under which to get the xpc endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:)-5qq2v)*