# AXValueType

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS 10.2+

## Declaration

```swift
enum AXValueType : UInt32, @unchecked Sendable
```

```c
typedef enum AXValueType : UInt32 {
    ...
} AXValueType;
```

#### Overview

These are AXValueType wrappers for other structures. You must use the AXValueCreate and AXValueGetValue functions to convert between the wrapped structure and the native structure.

## Topics

### Constants
- [kAXValueCGPointType](./axvaluetype/kaxvaluecgpointtype.md)
- [kAXValueCGSizeType](./axvaluetype/kaxvaluecgsizetype.md)
- [kAXValueCGRectType](./axvaluetype/kaxvaluecgrecttype.md)
- [kAXValueCFRangeType](./axvaluetype/kaxvaluecfrangetype.md)
- [kAXValueAXErrorType](./axvaluetype/kaxvalueaxerrortype.md)
- [kAXValueIllegalType](./axvaluetype/kaxvalueillegaltype.md)
### Enumeration Cases
- [AXValueType.axError](./axvaluetype/axerror.md)
- [AXValueType.cfRange](./axvaluetype/cfrange.md)
- [AXValueType.cgPoint](./axvaluetype/cgpoint.md)
- [AXValueType.cgRect](./axvaluetype/cgrect.md)
- [AXValueType.cgSize](./axvaluetype/cgsize.md)
- [AXValueType.illegal](./axvaluetype/illegal.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axvaluetype)*