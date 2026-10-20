# setException(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Raises a scripting environment exception in the context of the current object.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func setException(_ description: String!)
```

```objc
- (void) setException:(NSString *) description;
```

## Parameters

- `description`: Description of the exception.

## See Also

### Raising exceptions
- [class func throwException(String!) -> Bool](./throwexception%28_%29.md)
  Raises an exception in the current script execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject/setexception(_:))*