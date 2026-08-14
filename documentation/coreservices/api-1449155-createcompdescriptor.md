# CreateCompDescriptor(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CreateCompDescriptor(_ comparisonOperator: DescType, _ operand1: UnsafeMutablePointer<AEDesc>!, _ operand2: UnsafeMutablePointer<AEDesc>!, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

## Parameters

- `comparisonOperator`: The comparison operator for comparing the descriptors in the `operand1` and `operand2` parameters. The standard comparison operators are defined in [`Comparison Operator Constants`](https://developer.apple.com/documentation/applicationservices/apple_event_manager/comparison_operator_constants). The actual comparison of the two operands is performed by the object comparison function provided by the client application. The way a comparison operator is interpreted is up to each application. See [`DescType`](desctype.md).
- `operand1`: A pointer to an object specifier. See [`AEDesc`](aedesc.md).
- `operand2`: A pointer to a descriptor (which can be an object specifier or any other descriptor) whose value is compared to the value of `operand1`. See [`AEDesc`](aedesc.md).
- `disposeInputs`: A Boolean value. Pass `TRUE` if the function should automatically dispose of any descriptors you have provided in the `operand1` and `operand2` parameters to the function. Pass `FALSE` if your application will dispose of the descriptors itself. A value of `FALSE` may be more efficient for some applications because it allows them to reuse descriptors. 
- `theDescriptor`: A pointer to a descriptor. On successful return, the comparison descriptor created by `CreateCompDescriptor`. Your application must dispose of this descriptor after it has finished using it. See [`AEDesc`](aedesc.md).

## See Also

- [func CreateLogicalDescriptor(UnsafeMutablePointer<AEDescList>!, DescType, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1445212-createlogicaldescriptor.md)
  Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 
- [func CreateObjSpecifier(DescType, UnsafeMutablePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450244-createobjspecifier.md)
  Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.
- [func CreateOffsetDescriptor(Int, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444957-createoffsetdescriptor.md)
  Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 
- [func CreateRangeDescriptor(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444087-createrangedescriptor.md)
  Creates a range descriptor that specifies a series of consecutive elements in the same container. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449155-createcompdescriptor)*