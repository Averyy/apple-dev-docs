# CreateObjSpecifier(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CreateObjSpecifier(_ desiredClass: DescType, _ theContainer: UnsafeMutablePointer<AEDesc>!, _ keyForm: DescType, _ keyData: UnsafeMutablePointer<AEDesc>!, _ disposeInputs: Bool, _ objSpecifier: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

## Parameters

- `desiredClass`: The object class of the desired Apple event objects. See  .
- `theContainer`: A pointer to a descriptor that describes the container for the requested object, usually in the form of another object specifier. See  .
- `keyForm`: The key form for the object specifier.
- `keyData`: A pointer to a descriptor that supplies the key data for the object specifier.
- `disposeInputs`: A Boolean value. Pass ( ) if the function should dispose of the descriptors for the   and   parameters or ( ) if your application will. A value of   may be more efficient for some applications because it allows them to reuse descriptors.
- `objSpecifier`: On successful return, a pointer to the object specifier created by the   function. If the function returns successfully, your application should call the   function to dispose of this descriptor after it has finished using it.

## See Also

- [func CreateCompDescriptor(DescType, UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449155-createcompdescriptor.md)
  Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.
- [func CreateLogicalDescriptor(UnsafeMutablePointer<AEDescList>!, DescType, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1445212-createlogicaldescriptor.md)
  Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 
- [func CreateOffsetDescriptor(Int, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444957-createoffsetdescriptor.md)
  Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 
- [func CreateRangeDescriptor(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444087-createrangedescriptor.md)
  Creates a range descriptor that specifies a series of consecutive elements in the same container. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450244-createobjspecifier)*