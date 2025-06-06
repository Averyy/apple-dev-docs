# evaluateWebScript(_:)

**Framework**: Webkit  
**Kind**: method

Returns the result of evaluating a script in the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func evaluateWebScript(_ script: String!) -> Any!
```

#### Return Value

The scripting object. The format of the script is dependent on the target scripting environment. Returns [`WebUndefined`](webundefined.md) if an exception is thrown in the JavaScript environment or there is no return value.

## Parameters

- `script`: The script to evaluate.

## See Also

- [func callWebScriptMethod(String!, withArguments: [Any]!) -> Any!](webscriptobject/callwebscriptmethod(_:witharguments:).md)
  Returns the result of executing a method in the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/evaluatewebscript(_:))*