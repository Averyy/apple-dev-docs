# setField(at:name:value:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setField<T>(at path: USDLayer.Path, name: USDToken, value: T) where T : USDValueProtocol
```

## Parameters

- `path`: The path of the spec to update.
- `name`: The field name.
- `value`: The typed value to store.

## See Also

### Reading and authoring fields
- [func field(at: USDLayer.Path, name: USDToken) -> USDValue?](./field%28at,name%29.md)
  Returns the value of the named field at the given path, or `nil` if no such field is authored.
- [func fields(at: USDLayer.Path) -> [USDToken]](./fields%28at%29.md)
  Returns the names of the fields authored at the given path.
- [func setField(at: USDLayer.Path, name: USDToken, value: USDValue)](./setfield%28at,name,value%29-83nwe.md)
  Sets the value of the named field at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/setfield(at:name:value:)-3242k)*