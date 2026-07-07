# subscript(_:as:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this array as data.

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
subscript(index: Int, as type: RawSpan.Type = RawSpan.self) -> RawSpan? { get }
```

#### Return Value

An array containing the data or `nil` if no such value was found.

## Parameters

- `index`: The index at which to get the data.
- `type`: The expected type of the resulting value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:as:)-96zf2)*