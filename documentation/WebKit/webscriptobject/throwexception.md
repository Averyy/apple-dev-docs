# throwException(_:)

**Framework**: WebKit  
**Kind**: method

Raises an exception in the current script execution context.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func throwException(_ exceptionMessage: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `exceptionMessage`: The exception message.

## See Also

- [func setException(String!)](webscriptobject/setexception(_:).md)
  Raises a scripting environment exception in the context of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/throwexception(_:))*