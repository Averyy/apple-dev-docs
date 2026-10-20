# webScriptValue(at:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the value of a property at the specified index.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func webScriptValue(at index: UInt32) -> Any!
```

```objc
- (id) webScriptValueAtIndex:(unsigned int) index;
```

#### Return Value

The value of a property at `index`. Returns [`WebUndefined`](../webundefined.md) if an exception is thrown in the JavaScript environment.

#### Discussion

Accessing property values by index is dependent on the scripting environment.

## Parameters

- `index`: The index of the property.

## See Also

### Getting and setting properties
- [func jsObject() -> JSObjectRef!](./jsobject%28%29.md)
  Returns the JavaScript object corresponding to the receiver.
- [func removeWebScriptKey(String!)](./removewebscriptkey%28_%29.md)
  Removes a property from a scripting environment.
- [func setWebScriptValueAt(UInt32, value: Any!)](./setwebscriptvalueat%28_,value%29.md)
  Sets the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/webscriptvalue(at:))*