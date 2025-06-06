# AEPutDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Adds a descriptor to any descriptor list, possibly replacing an existing descriptor in the list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutDesc(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list to add a descriptor to. See  .
- `index`: You can pass a value of zero or count + 1 to add the descriptor at the end of the list.   returns an error ( ) if you pass a negative number or a value that is out of range.
- `theAEDesc`: A pointer to the descriptor to add to the list. See  .

## See Also

- [func AEPutArray(UnsafeMutablePointer<AEDescList>!, AEArrayType, UnsafePointer<AEArrayData>!, DescType, Size, Int) -> OSErr](1442535-aeputarray.md)
  Inserts the data for an Apple event array into a descriptor list, replacing any previous descriptors in the list.
- [func AEPutPtr(UnsafeMutablePointer<AEDescList>!, Int, DescType, UnsafeRawPointer!, Size) -> OSErr](1445287-aeputptr.md)
  Inserts data specified in a buffer into a descriptor list as a descriptor, possibly replacing an existing descriptor in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450093-aeputdesc)*