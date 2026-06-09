# field(_:as:)

**Framework**: USDKit  
**Kind**: method

Typed field accessor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func field<T>(_ name: USDToken, as type: T.Type) -> T? where T : USDValueProtocol
```

#### Return Value

The field’s value as `T`, or `nil` if the field is unauthored or holds a different type.

## Parameters

- `name`: The field name to look up.
- `type`: The expected value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec/fieldcollection/field(_:as:))*