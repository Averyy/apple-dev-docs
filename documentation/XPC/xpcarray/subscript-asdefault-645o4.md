# subscript(_:as:default:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this array as an XPCArray.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript(index: Int, as type: XPCArray.Type = XPCArray.self, default defaultValue: @autoclosure () -> XPCArray) -> XPCArray { get }
```

#### Return Value

An XPCArray value, possibly `defaultValue`.

## Parameters

- `index`: The index at which to get the XPCArray.
- `type`: The expected type of the resulting value.
- `defaultValue`: The value to produce if no XPCArray is available at `index`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:as:default:)-645o4)*