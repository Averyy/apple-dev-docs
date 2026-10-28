# AXValueGetType(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXValueGetType(_ value: AXValue) -> AXValueType
```

```c
AXValueType AXValueGetType(AXValueRef value);
```

## Discussion

Returns the structure type encoded in value. If the type is not recognized, it returns kAXValueIllegalType.

## Parameters

- `value`: 

## See Also

### Miscellaneous
- [func AXValueCreate(AXValueType, UnsafeRawPointer) -> AXValue?](./api-1459351-axvaluecreate.md)
- [func AXValueGetTypeID() -> CFTypeID](./api-1460780-axvaluegettypeid.md)
- [func AXValueGetValue(AXValue, AXValueType, UnsafeMutableRawPointer) -> Bool](./api-1462933-axvaluegetvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460911-axvaluegettype)*