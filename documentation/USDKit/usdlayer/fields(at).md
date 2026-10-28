# fields(at:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

The names of the authored fields.

## Parameters

- `path`: The path to look up.

## See Also

### Reading and authoring fields
- [func field(at: USDLayer.Path, name: USDToken) -> USDValue?](./field%28at,name%29.md)
  Returns the value of the named field at the given path, or `nil` if no such field is authored.
- [func setField(at: USDLayer.Path, name: USDToken, value: USDValue)](./setfield%28at,name,value%29-83nwe.md)
  Sets the value of the named field at the given path.
- [func setField<T>(at: USDLayer.Path, name: USDToken, value: T)](./setfield%28at,name,value%29-3242k.md)
  Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/fields(at:))*