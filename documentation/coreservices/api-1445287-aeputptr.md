# AEPutPtr(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Inserts data specified in a buffer into a descriptor list as a descriptor, possibly replacing an existing descriptor in the list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutPtr(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int, _ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list to add a descriptor to. See  .
- `index`: You can pass a value of zero or count + 1 to add the descriptor at the end of the list.   returns an error ( ) if you pass a negative number or a value that is out of range.
- `typeCode`: The descriptor type for the descriptor to be put into the list. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataPtr`: A pointer to the data for the descriptor to add.
- `dataSize`: The length, in bytes, of the data for the descriptor to add.

## See Also

- [func AEPutArray(UnsafeMutablePointer<AEDescList>!, AEArrayType, UnsafePointer<AEArrayData>!, DescType, Size, Int) -> OSErr](1442535-aeputarray.md)
  Inserts the data for an Apple event array into a descriptor list, replacing any previous descriptors in the list.
- [func AEPutDesc(UnsafeMutablePointer<AEDescList>!, Int, UnsafePointer<AEDesc>!) -> OSErr](1450093-aeputdesc.md)
  Adds a descriptor to any descriptor list, possibly replacing an existing descriptor in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445287-aeputptr)*