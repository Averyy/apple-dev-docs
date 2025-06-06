# CreateRangeDescriptor(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a range descriptor that specifies a series of consecutive elements in the same container. 

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func CreateRangeDescriptor(_ rangeStart: UnsafeMutablePointer<AEDesc>!, _ rangeStop: UnsafeMutablePointer<AEDesc>!, _ disposeInputs: Bool, _ theDescriptor: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Although the `rangeStart` and `rangeStop` parameters can be any object specifiers—including object specifiers that specify more than one Apple event object—most applications expect these parameters to specify single Apple event objects. 

## Parameters

- `rangeStart`: A pointer to an object specifier that identifies the first Apple event object in the range. See  .
- `rangeStop`: A pointer to an object specifier that identifies the last Apple event object in the range. See  .
- `disposeInputs`: A Boolean value. Pass ( ) if the function should dispose of the descriptors for the   and   parameters and set them to the null descriptor or ( ) if your application will. A value of   may be more efficient for some applications because it allows them to reuse descriptors. 
- `theDescriptor`: A pointer to a descriptor. On successful return, the range descriptor created by  . Your application must dispose of this descriptor after it has finished using it. See  .

## See Also

- [func CreateCompDescriptor(DescType, UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449155-createcompdescriptor.md)
  Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.
- [func CreateLogicalDescriptor(UnsafeMutablePointer<AEDescList>!, DescType, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1445212-createlogicaldescriptor.md)
  Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 
- [func CreateObjSpecifier(DescType, UnsafeMutablePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450244-createobjspecifier.md)
  Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.
- [func CreateOffsetDescriptor(Int, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444957-createoffsetdescriptor.md)
  Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444087-createrangedescriptor)*