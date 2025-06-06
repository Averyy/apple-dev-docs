# AEPutArray(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Inserts the data for an Apple event array into a descriptor list, replacing any previous descriptors in the list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutArray(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ arrayType: AEArrayType, _ arrayPtr: UnsafePointer<AEArrayData>!, _ itemType: DescType, _ itemSize: Size, _ itemCount: Int) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

A factored descriptor list is one in which the Apple Event Manager automatically isolates the data that is common to all the elements of the list so that the common data only appears in the list once. To create a factored descriptor list, you call the [`AECreateList(_:_:_:_:)`](1448643-aecreatelist.md) function and specify the data that is common to all elements in the descriptor array. 

##### 1770166

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: See  .
- `arrayType`: The Apple event array type to create. Pass a value specified by one of the constants described in  . See  .
- `arrayPtr`: A pointer to a buffer, local variable, or other storage location, created and disposed of by your application, that contains the array to put into the descriptor list. See  .
- `itemType`: For arrays of type  ,  , or  , the descriptor type of the array items to create. Use one of the constants described in  , such as  . You don’t need to specify an item type for arrays of type   or   because the data is already stored in descriptors which contain a descriptor type. See  .
- `itemSize`: For arrays of type   or  , the size (in bytes) of the array items to create. You don’t need to specify an item size for arrays of type  ,  , or   because their descriptors (though not the data they point to) have a known size. 
- `itemCount`: The number of elements in the array.

## See Also

- [func AEPutDesc(UnsafeMutablePointer<AEDescList>!, Int, UnsafePointer<AEDesc>!) -> OSErr](1450093-aeputdesc.md)
  Adds a descriptor to any descriptor list, possibly replacing an existing descriptor in the list.
- [func AEPutPtr(UnsafeMutablePointer<AEDescList>!, Int, DescType, UnsafeRawPointer!, Size) -> OSErr](1445287-aeputptr.md)
  Inserts data specified in a buffer into a descriptor list as a descriptor, possibly replacing an existing descriptor in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442535-aeputarray)*