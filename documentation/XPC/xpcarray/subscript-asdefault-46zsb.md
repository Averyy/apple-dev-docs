# subscript(_:as:default:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this array as an endpoint.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
subscript(index: Int, as type: XPCEndpoint.Type = XPCEndpoint.self, default defaultValue: @autoclosure () -> XPCEndpoint) -> XPCEndpoint { get }
```

#### Return Value

An endpoint value, possibly `defaultValue`.

## Parameters

- `index`: The index at which to get the endpoint.
- `type`: The expected type of the resulting value.
- `defaultValue`: The value to produce if no endpoint is available at `index`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:as:default:)-46zsb)*