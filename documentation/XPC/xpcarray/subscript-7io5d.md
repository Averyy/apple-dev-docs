# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this array as an endpoint.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
subscript(index: Int) -> XPCEndpoint? { get set }
```

#### Return Value

An endpoint value or `nil` if no such value was found.

## Parameters

- `index`: The index at which to get or set the endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-7io5d)*