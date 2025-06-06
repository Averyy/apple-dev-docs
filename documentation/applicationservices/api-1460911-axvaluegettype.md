# AXValueGetType(_:)

**Framework**: Application Services  
**Kind**: func

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXValueGetType(_ value: AXValue) -> AXValueType
```

#### Discussion

Returns the structure type encoded in value. If the type is not recognized, it returns kAXValueIllegalType.

## Parameters

- `value`: 

## See Also

- [func AXValueCreate(AXValueType, UnsafeRawPointer) -> AXValue?](1459351-axvaluecreate.md)
- [func AXValueGetTypeID() -> CFTypeID](1460780-axvaluegettypeid.md)
- [func AXValueGetValue(AXValue, AXValueType, UnsafeMutableRawPointer) -> Bool](1462933-axvaluegetvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460911-axvaluegettype)*