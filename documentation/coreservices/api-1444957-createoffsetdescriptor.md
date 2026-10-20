# CreateOffsetDescriptor(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CreateOffsetDescriptor(_ theOffset: Int, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

```c
OSErr CreateOffsetDescriptor(long theOffset, AEDesc *theDescriptor);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

## Parameters

- `theOffset`: A positive integer that specifies the offset from the beginning of the container (the first element has an offset of 1), or a negative integer that specifies the offset from the end (the last element has an offset of –1).
- `theDescriptor`: A pointer to a descriptor. On successful return, the offset descriptor created by `CreateOffsetDescriptor`. On error, returns a null descriptor. Your application must dispose of the descriptor after it has finished using it. See [`AEDesc`](./aedesc.md).

## See Also

### Creating Object Specifiers
- [func CreateCompDescriptor(DescType, UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1449155-createcompdescriptor.md)
  Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.
- [func CreateLogicalDescriptor(UnsafeMutablePointer<AEDescList>!, DescType, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1445212-createlogicaldescriptor.md)
  Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 
- [func CreateObjSpecifier(DescType, UnsafeMutablePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1450244-createobjspecifier.md)
  Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.
- [func CreateRangeDescriptor(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1444087-createrangedescriptor.md)
  Creates a range descriptor that specifies a series of consecutive elements in the same container. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444957-createoffsetdescriptor)*