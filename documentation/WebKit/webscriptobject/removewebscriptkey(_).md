# removeWebScriptKey(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Removes a property from a scripting environment.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func removeWebScriptKey(_ name: String!)
```

```objc
- (void) removeWebScriptKey:(NSString *) name;
```

## Parameters

- `name`: Property to remove.

## See Also

### Getting and setting properties
- [func jsObject() -> JSObjectRef!](./jsobject%28%29.md)
  Returns the JavaScript object corresponding to the receiver.
- [func webScriptValue(at: UInt32) -> Any!](./webscriptvalue%28at%29.md)
  Returns the value of a property at the specified index.
- [func setWebScriptValueAt(UInt32, value: Any!)](./setwebscriptvalueat%28_,value%29.md)
  Sets the value of a property at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/removewebscriptkey(_:))*