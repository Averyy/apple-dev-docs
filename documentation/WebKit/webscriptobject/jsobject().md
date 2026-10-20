# jsObject()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the JavaScript object corresponding to the receiver.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

## Declaration

```swift
func jsObject() -> JSObjectRef!
```

```objc
- (JSObjectRef) JSObject;
```

#### Return Value

The JavaScript object corresponding to the receiver in the JavaScriptCore C API.

## See Also

### Getting and setting properties
- [func removeWebScriptKey(String!)](./removewebscriptkey%28_%29.md)
  Removes a property from a scripting environment.
- [func webScriptValue(at: UInt32) -> Any!](./webscriptvalue%28at%29.md)
  Returns the value of a property at the specified index.
- [func setWebScriptValueAt(UInt32, value: Any!)](./setwebscriptvalueat%28_,value%29.md)
  Sets the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/jsobject())*