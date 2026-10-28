# callWebScriptMethod(_:withArguments:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the result of executing a method in the scripting environment.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func callWebScriptMethod(_ name: String!, withArguments arguments: [Any]!) -> Any!
```

```objc
- (id) callWebScriptMethod:(NSString *) name withArguments:(NSArray *) arguments;
```

## Return Value

The return value of the method. Returns [`WebUndefined`](../webundefined.md) if an exception is thrown in the JavaScript environment or the method has no return value.

## Parameters

- `name`: The name of the method to invoke.
- `arguments`: The values to pass to the method.

## See Also

### Executing scripts
- [func evaluateWebScript(String!) -> Any!](./evaluatewebscript%28_%29.md)
  Returns the result of evaluating a script in the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/callwebscriptmethod(_:witharguments:))*