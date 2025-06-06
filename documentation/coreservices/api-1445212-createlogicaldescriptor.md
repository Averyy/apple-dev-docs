# CreateLogicalDescriptor(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CreateLogicalDescriptor(_ theLogicalTerms: UnsafeMutablePointer<AEDescList>!, _ theLogicOperator: DescType, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The `CreateLogicalDescriptor` function creates a logical descriptor, which specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 

## Parameters

- `theLogicalTerms`: A pointer to a list containing comparison descriptors ( ), logical descriptors ( ), or both. If the value of the parameter   is   or  , the list can contain any number of descriptors. If the value of the parameter   is  , logically this list should contain a single descriptor. However, the function will not return an error if the list contains more than one descriptor for a logical operator of  . See  .
- `theLogicOperator`: A logical operator represented by one of the constants described in  . What you pass for this parameter helps determine what you pass for the   parameter. See  .
- `disposeInputs`: A Boolean value. Pass   if the function should automatically dispose of the descriptors you have provided in the   parameter or ( ) if your application will. A value of   may be more efficient for some applications because it allows them to reuse descriptors. 
- `theDescriptor`: A pointer to a descriptor. On successful return, the logical descriptor created by  . Your application must dispose of this descriptor after it has finished using it. See  .

## See Also

- [func CreateCompDescriptor(DescType, UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449155-createcompdescriptor.md)
  Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.
- [func CreateObjSpecifier(DescType, UnsafeMutablePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450244-createobjspecifier.md)
  Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.
- [func CreateOffsetDescriptor(Int, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444957-createoffsetdescriptor.md)
  Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 
- [func CreateRangeDescriptor(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444087-createrangedescriptor.md)
  Creates a range descriptor that specifies a series of consecutive elements in the same container. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445212-createlogicaldescriptor)*