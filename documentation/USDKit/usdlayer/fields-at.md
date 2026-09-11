# fields(at:)

**Framework**: USDKit  
**Kind**: method

Returns the names of the fields authored at the given path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func fields(at path: USDLayer.Path) -> [USDToken]
```

#### Return Value

The names of the authored fields.

## Parameters

- `path`: The path to look up.

## See Also

- [func field(at: USDLayer.Path, name: USDToken) -> USDValue?](usdlayer/field(at:name:).md)
  Returns the value of the named field at the given path, or `nil` if no such field is authored.
- [func setField(at: USDLayer.Path, name: USDToken, value: USDValue)](usdlayer/setfield(at:name:value:)-83nwe.md)
  Sets the value of the named field at the given path.
- [func setField<T>(at: USDLayer.Path, name: USDToken, value: T)](usdlayer/setfield(at:name:value:)-3242k.md)
  Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/fields(at:))*