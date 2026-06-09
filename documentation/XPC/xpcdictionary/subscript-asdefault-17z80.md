# subscript(_:as:default:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this dictionary as an XPCArray.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript(key: String, as type: XPCArray.Type = XPCArray.self, default defaultValue: @autoclosure () -> XPCArray) -> XPCArray { get }
```

#### Return Value

An XPCArray value, possibly `defaultValue`.

## Parameters

- `key`: The key under which to get the XPCArray.
- `type`: The expected type of the resulting value.
- `defaultValue`: The value to produce if no XPCArray is available under `key`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:as:default:)-17z80)*