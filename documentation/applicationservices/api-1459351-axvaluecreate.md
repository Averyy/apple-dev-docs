# AXValueCreate(_:_:)

**Framework**: Application Services  
**Kind**: func

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafeRawPointer) -> AXValue?
```

#### Discussion

Encodes a structure pointed to by valuePtr into a CFTypeRef.

## Parameters

- `theType`: 
- `valuePtr`: 

## See Also

- [func AXValueGetType(AXValue) -> AXValueType](1460911-axvaluegettype.md)
- [func AXValueGetTypeID() -> CFTypeID](1460780-axvaluegettypeid.md)
- [func AXValueGetValue(AXValue, AXValueType, UnsafeMutableRawPointer) -> Bool](1462933-axvaluegetvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459351-axvaluecreate)*