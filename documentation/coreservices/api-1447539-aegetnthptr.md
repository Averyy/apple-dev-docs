# AEGetNthPtr(_:_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets a copy of the data from a descriptor at a specified position in a descriptor list; typically used when your application needs to work with the extracted data directly.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetNthPtr(_ theAEDescList: UnsafePointer<AEDescList>!, _ index: Int, _ desiredType: DescType, _ theAEKeyword: UnsafeMutablePointer<AEKeyword>!, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The `AEGetNthPtr` function uses a buffer to return the data for a specified descriptor from a specified descriptor list. The function attempts to coerce the descriptor to the descriptor type specified by the `desiredType` parameter.

Before calling `AEGetNthPtr`, you can call the [`AESizeOfNthItem(_:_:_:_:)`](1447307-aesizeofnthitem.md) function to determine a size for the `dataPtr` buffer. However, unless you specify `typeWildCard` for the `desiredType` parameter, `AESizeOfNthIte`m may coerce the data, which may cause the size of the data to change. If you are using `AEGetNthPtr` to iterate through a list of descriptors of the same type with a fixed size, such as a list of descriptors of type `typeFSS`, you can get the size once, allocate a buffer, and reuse it for each call.

The order of items in an Apple event record may change after an insertion or deletion. In addition, duplicating an Apple event record is not guaranteed to preserve the item order. 

##### 1770195

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list that contains the descriptor. See  .
- `index`: A one-based positive integer indicating the position in the descriptor list of the descriptor to get the data from.   returns an error if you pass zero, a negative number, or a value that is out of range.
- `desiredType`: See  .
- `theAEKeyword`: A pointer to a keyword. On return, the keyword for the specified descriptor, if you are getting data from a list of keyword-specified descriptors; otherwise,   returns the value  . Some keyword constants are described in   and  . See  .
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the data pointed to by  . For a list of AppleScript’s predefined descriptor types, see  .
- `dataPtr`: A pointer to a buffer, local variable, or other storage location created and disposed of by your application. The size in bytes must be at least as large as the value you pass in the   parameter. On return, contains the data from the descriptor at the position in the descriptor list specified by the   parameter.
- `maximumSize`: The maximum length, in bytes, of the expected data. The   function will not return more data than you specify in this parameter. 
- `actualSize`: A pointer to a size variable. On return, the length, in bytes, of the data for the specified descriptor. If this value is larger than the value of the   parameter, the buffer pointed to by   was not large enough to contain all of the data for the descriptor, though   does not write beyond the end of the buffer. If the buffer was too small, you can resize it and call   again.

## See Also

- [func AEGetArray(UnsafePointer<AEDescList>!, AEArrayType, AEArrayDataPointer!, Size, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!, UnsafeMutablePointer<Int>!) -> OSErr](1445720-aegetarray.md)
  Extracts data from an Apple event array created with the `AEPutArray` function and stores it as a standard array of fixed size items in the specified buffer.
- [func AEGetNthDesc(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1448326-aegetnthdesc.md)
   Copies a descriptor from a specified position in a descriptor list into a specified descriptor; typically used when your application needs to pass the extracted data to another function as a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447539-aegetnthptr)*