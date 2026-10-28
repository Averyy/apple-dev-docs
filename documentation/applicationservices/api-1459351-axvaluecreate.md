# AXValueCreate(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafeRawPointer) -> AXValue?
```

```c
AXValueRef AXValueCreate(AXValueType theType, const void *valuePtr);
```

## Discussion

Encodes a structure pointed to by valuePtr into a CFTypeRef.

## Parameters

- `theType`: 
- `valuePtr`: 

## See Also

### Miscellaneous
- [func AXValueGetType(AXValue) -> AXValueType](./api-1460911-axvaluegettype.md)
- [func AXValueGetTypeID() -> CFTypeID](./api-1460780-axvaluegettypeid.md)
- [func AXValueGetValue(AXValue, AXValueType, UnsafeMutableRawPointer) -> Bool](./api-1462933-axvaluegetvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459351-axvaluecreate)*