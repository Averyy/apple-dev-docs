# throwException(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Raises an exception in the current script execution context.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class func throwException(_ exceptionMessage: String!) -> Bool
```

```objc
+ (BOOL) throwException:(NSString *) exceptionMessage;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `exceptionMessage`: The exception message.

## See Also

### Raising exceptions
- [func setException(String!)](./setexception%28_%29.md)
  Raises a scripting environment exception in the context of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/throwexception(_:))*