# subscript(_:as:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this array as an endpoint.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
subscript(index: Int, as type: XPCEndpoint.Type = XPCEndpoint.self) -> XPCEndpoint? { get }
```

#### Return Value

An endpoint value or `nil` if no such value was found.

## Parameters

- `index`: The index at which to get the endpoint.
- `type`: The expected type of the resulting value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:as:)-5g1u8)*