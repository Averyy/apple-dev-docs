# field(at:name:)

**Framework**: USDKit  
**Kind**: method

Returns the value of the named field at the given path, or `nil` if no such field is authored.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func field(at path: USDLayer.Path, name: USDToken) -> USDValue?
```

#### Return Value

The field’s value, or `nil` if unauthored.

## Parameters

- `path`: The path to look up.
- `name`: The field name.

## See Also

- [func fields(at: USDLayer.Path) -> [USDToken]](usdlayer/fields(at:).md)
  Returns the names of the fields authored at the given path.
- [func setField(at: USDLayer.Path, name: USDToken, value: USDValue)](usdlayer/setfield(at:name:value:)-83nwe.md)
  Sets the value of the named field at the given path.
- [func setField<T>(at: USDLayer.Path, name: USDToken, value: T)](usdlayer/setfield(at:name:value:)-3242k.md)
  Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/field(at:name:))*