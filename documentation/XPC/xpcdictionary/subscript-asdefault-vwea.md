# subscript(_:as:default:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this dictionary as a UUID.

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
subscript(key: String, as type: uuid_t.Type = uuid_t.self, default defaultValue: @autoclosure () -> uuid_t) -> uuid_t { get }
```

#### Return Value

A UUID value, possibly `defaultValue`.

## Parameters

- `key`: The key under which to get the UUID.
- `type`: The expected type of the resulting value.
- `defaultValue`: The value to produce if no UUID is available under `key`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:as:default:)-vwea)*