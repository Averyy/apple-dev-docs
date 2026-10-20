# setWebScriptValueAt(_:value:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of a property at the specified index.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func setWebScriptValueAt(_ index: UInt32, value: Any!)
```

```objc
- (void) setWebScriptValueAtIndex:(unsigned int) index value:(id) value;
```

## Parameters

- `index`: The index of the property.
- `value`: The value of the property.

## See Also

### Getting and setting properties
- [func jsObject() -> JSObjectRef!](./jsobject%28%29.md)
  Returns the JavaScript object corresponding to the receiver.
- [func removeWebScriptKey(String!)](./removewebscriptkey%28_%29.md)
  Removes a property from a scripting environment.
- [func webScriptValue(at: UInt32) -> Any!](./webscriptvalue%28at%29.md)
  Returns the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/setwebscriptvalueat(_:value:))*