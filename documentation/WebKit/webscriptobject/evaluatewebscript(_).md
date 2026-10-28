# evaluateWebScript(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the result of evaluating a script in the scripting environment.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func evaluateWebScript(_ script: String!) -> Any!
```

```objc
- (id) evaluateWebScript:(NSString *) script;
```

## Return Value

The scripting object. The format of the script is dependent on the target scripting environment. Returns [`WebUndefined`](../webundefined.md) if an exception is thrown in the JavaScript environment or there is no return value.

## Parameters

- `script`: The script to evaluate.

## See Also

### Executing scripts
- [func callWebScriptMethod(String!, withArguments: [Any]!) -> Any!](./callwebscriptmethod%28_,witharguments%29.md)
  Returns the result of executing a method in the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/evaluatewebscript(_:))*