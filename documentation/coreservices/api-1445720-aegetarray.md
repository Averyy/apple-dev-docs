# AEGetArray(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Extracts data from an Apple event array created with the `AEPutArray` function and stores it as a standard array of fixed size items in the specified buffer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetArray(_ theAEDescList: UnsafePointer<AEDescList>!, _ arrayType: AEArrayType, _ arrayPtr: AEArrayDataPointer!, _ maximumSize: Size, _ itemType: UnsafeMutablePointer<DescType>!, _ itemSize: UnsafeMutablePointer<Size>!, _ itemCount: UnsafeMutablePointer<Int>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The `AEGetArray` function uses a buffer identified by the pointer in the `arrayPtr` parameter to store the converted data for the Apple event array specified by the `theAEDescList` parameter. For example, `AEGetArray` may convert an array of descriptors of type `typeLongInteger` into a simple array of integer values or an array of descriptors of type `typeFSS` into an array of file specification records.

Even if the descriptor list that contains the array is factored, the converted data for each array item includes the data common to all the descriptors in the list. The Apple Event Manager automatically reconstructs the common data for each item when you call `AEGetArray`.

For information about creating and factoring descriptor lists for Apple event arrays, see [`AECreateList(_:_:_:_:)`](1448643-aecreatelist.md). For information about adding an Apple event array to a descriptor list, see [`AEPutArray(_:_:_:_:_:_:)`](1442535-aeputarray.md). 

##### 1770193

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list to get the array from. If the array is of type  ,  , or  , the descriptor list must be factored. A factored descriptor list is one in which the Apple Event Manager automatically isolates the data that is common to all the elements of the list so that the common data only appears in the list once. To create a factored descriptor list, you call the   function and specify the data that is common to all elements in the descriptor array. See the Discussion section for related information. See  .
- `arrayType`: The Apple event array type to convert. Pass one of the constants: described in  . See  .
- `arrayPtr`: A pointer to a buffer, allocated and disposed of by your application, for storing the array. The size in bytes must be at least as large as the value you pass in the   parameter. On return, the buffer contains the array of fixed-size items. See  .
- `maximumSize`: The maximum length, in bytes, of the expected data. The   function will not return more data than you specify in this parameter. 
- `itemType`: A pointer to a descriptor type. On return, for arrays of type  ,  , or  , the descriptor type of the items in the returned array. The   function doesn’t supply a value in   for arrays of type   and   because they may contain descriptors of different types. Possible descriptor types are listed in  . See  .
- `itemSize`: A pointer to a size variable. On return, for arrays of type   or  , the size (in bytes) of each item in the returned array. You don’t get an item size for arrays of type  ,  , or   because descriptors and handles (though not the data they point to) have a known size.
- `itemCount`: A pointer to a size variable. On return, the number of items in the returned array.

## See Also

- [func AEGetNthDesc(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1448326-aegetnthdesc.md)
   Copies a descriptor from a specified position in a descriptor list into a specified descriptor; typically used when your application needs to pass the extracted data to another function as a descriptor.
- [func AEGetNthPtr(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1447539-aegetnthptr.md)
  Gets a copy of the data from a descriptor at a specified position in a descriptor list; typically used when your application needs to work with the extracted data directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445720-aegetarray)*