# setField(at:name:value:)

**Framework**: USDKit  
**Kind**: method

Sets the value of the named field at the given path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setField(at path: USDLayer.Path, name: USDToken, value: USDValue)
```

## Parameters

- `path`: The path of the spec to update.
- `name`: The field name.
- `value`: The new field value.

## See Also

- [func field(at: USDLayer.Path, name: USDToken) -> USDValue?](usdlayer/field(at:name:).md)
  Returns the value of the named field at the given path, or `nil` if no such field is authored.
- [func fields(at: USDLayer.Path) -> [USDToken]](usdlayer/fields(at:).md)
  Returns the names of the fields authored at the given path.
- [func setField<T>(at: USDLayer.Path, name: USDToken, value: T)](usdlayer/setfield(at:name:value:)-3242k.md)
  Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/setfield(at:name:value:)-83nwe)*