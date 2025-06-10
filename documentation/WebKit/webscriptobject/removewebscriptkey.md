# removeWebScriptKey(_:)

**Framework**: WebKit  
**Kind**: method

Removes a property from a scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func removeWebScriptKey(_ name: String!)
```

## Parameters

- `name`: Property to remove.

## See Also

- [func jsObject() -> JSObjectRef!](webscriptobject/jsobject.md)
  Returns the JavaScript object corresponding to the receiver.
- [func webScriptValue(at: UInt32) -> Any!](webscriptobject/webscriptvalue(at:).md)
  Returns the value of a property at the specified index.
- [func setWebScriptValueAt(UInt32, value: Any!)](webscriptobject/setwebscriptvalueat(_:value:).md)
  Sets the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/removewebscriptkey(_:))*