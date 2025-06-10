# webScriptValue(at:)

**Framework**: WebKit  
**Kind**: method

Returns the value of a property at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func webScriptValue(at index: UInt32) -> Any!
```

#### Return Value

The value of a property at `index`. Returns [`WebUndefined`](webundefined.md) if an exception is thrown in the JavaScript environment.

#### Discussion

Accessing property values by index is dependent on the scripting environment.

## Parameters

- `index`: The index of the property.

## See Also

- [func jsObject() -> JSObjectRef!](webscriptobject/jsobject.md)
  Returns the JavaScript object corresponding to the receiver.
- [func removeWebScriptKey(String!)](webscriptobject/removewebscriptkey(_:).md)
  Removes a property from a scripting environment.
- [func setWebScriptValueAt(UInt32, value: Any!)](webscriptobject/setwebscriptvalueat(_:value:).md)
  Sets the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/webscriptvalue(at:))*