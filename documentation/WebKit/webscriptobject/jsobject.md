# jsObject()

**Framework**: Webkit  
**Kind**: method

Returns the JavaScript object corresponding to the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func jsObject() -> JSObjectRef!
```

#### Return Value

The JavaScript object corresponding to the receiver in the JavaScriptCore C API.

## See Also

- [func removeWebScriptKey(String!)](webscriptobject/removewebscriptkey(_:).md)
  Removes a property from a scripting environment.
- [func webScriptValue(at: UInt32) -> Any!](webscriptobject/webscriptvalue(at:).md)
  Returns the value of a property at the specified index.
- [func setWebScriptValueAt(UInt32, value: Any!)](webscriptobject/setwebscriptvalueat(_:value:).md)
  Sets the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/jsobject())*