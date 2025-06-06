# setWebScriptValueAt(_:value:)

**Framework**: Webkit  
**Kind**: method

Sets the value of a property at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setWebScriptValueAt(_ index: UInt32, value: Any!)
```

## Parameters

- `index`: The index of the property.
- `value`: The value of the property.

## See Also

- [func jsObject() -> JSObjectRef!](webscriptobject/jsobject.md)
  Returns the JavaScript object corresponding to the receiver.
- [func removeWebScriptKey(String!)](webscriptobject/removewebscriptkey(_:).md)
  Removes a property from a scripting environment.
- [func webScriptValue(at: UInt32) -> Any!](webscriptobject/webscriptvalue(at:).md)
  Returns the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/setwebscriptvalueat(_:value:))*