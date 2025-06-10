# subscript(_:as:)

**Framework**: XPC  
**Kind**: subscript

Get an `XPCEndpoint` value in this dictionary.

**Availability**:
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
subscript(key: String, as type: XPCListener.Endpoint.Type = XPCListener.Endpoint.self) -> XPCListener.Endpoint? { get }
```

#### Return Value

A previously-set endpoint value. If no endpoint was previously set for `key`, returns `nil`.

## Parameters

- `key`: The key under which to get the xpc endpoint.
- `type`: The expected type of the resulting value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:as:)-1c5kw)*