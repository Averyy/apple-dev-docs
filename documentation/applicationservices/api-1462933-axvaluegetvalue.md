# AXValueGetValue(_:_:_:)

**Framework**: Application Services  
**Kind**: func

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXValueGetValue(_ value: AXValue, _ theType: AXValueType, _ valuePtr: UnsafeMutableRawPointer) -> Bool
```

#### Discussion

Decodes the structure stored in value and copies it into valuePtr. If the structure stored in value is not the same as requested by theType, the function returns false.

## Parameters

- `value`: 

## See Also

- [func AXValueCreate(AXValueType, UnsafeRawPointer) -> AXValue?](1459351-axvaluecreate.md)
- [func AXValueGetType(AXValue) -> AXValueType](1460911-axvaluegettype.md)
- [func AXValueGetTypeID() -> CFTypeID](1460780-axvaluegettypeid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462933-axvaluegetvalue)*