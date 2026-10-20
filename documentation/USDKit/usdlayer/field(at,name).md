# field(at:name:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns the value of the named field at the given path, or `nil` if no such field is authored.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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

### Reading and authoring fields
- [func fields(at: USDLayer.Path) -> [USDToken]](./fields%28at%29.md)
  Returns the names of the fields authored at the given path.
- [func setField(at: USDLayer.Path, name: USDToken, value: USDValue)](./setfield%28at,name,value%29-83nwe.md)
  Sets the value of the named field at the given path.
- [func setField<T>(at: USDLayer.Path, name: USDToken, value: T)](./setfield%28at,name,value%29-3242k.md)
  Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/field(at:name:))*