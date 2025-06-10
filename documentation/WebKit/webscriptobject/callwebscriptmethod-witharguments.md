# callWebScriptMethod(_:withArguments:)

**Framework**: WebKit  
**Kind**: method

Returns the result of executing a method in the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func callWebScriptMethod(_ name: String!, withArguments arguments: [Any]!) -> Any!
```

#### Return Value

The return value of the method. Returns [`WebUndefined`](webundefined.md) if an exception is thrown in the JavaScript environment or the method has no return value.

## Parameters

- `name`: The name of the method to invoke.
- `arguments`: The values to pass to the method.

## See Also

- [func evaluateWebScript(String!) -> Any!](webscriptobject/evaluatewebscript(_:).md)
  Returns the result of evaluating a script in the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/callwebscriptmethod(_:witharguments:))*