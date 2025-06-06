# AEGetNthDesc(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

 Copies a descriptor from a specified position in a descriptor list into a specified descriptor; typically used when your application needs to pass the extracted data to another function as a descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetNthDesc(_ theAEDescList: UnsafePointer<AEDescList>!, _ index: Int, _ desiredType: DescType, _ theAEKeyword: UnsafeMutablePointer<AEKeyword>!, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

If the Nth descriptor in the list is itself an Apple event record and the desired type is not wildcard, record, or list, `AEGetNthDesc` will fail with an `errAECoercionFailed` error. This behavior prevents coercion problems. 

You may find the [`AEGetNthPtr(_:_:_:_:_:_:_:_:)`](1447539-aegetnthptr.md) function convenient for retrieving data for direct use in your application, as it includes automatic coercion. 

##### 1770194

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list to get the descriptor from. See  .
- `index`: A one-based positive integer indicating the position of the descriptor to get.   returns an error if you pass zero, a negative number, or a value that is out of range.
- `desiredType`: See  .
- `theAEKeyword`: A pointer to a keyword. On successful return, the keyword for the specified descriptor, if you are getting data from a list of keyword-specified descriptors; otherwise,   returns the value  . Some keyword constants are described in   and  . See  .
- `result`: A pointer to a descriptor. On successful return, a copy of the descriptor specified by the   parameter, coerced, if necessary, to the descriptor type specified by the   parameter. On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it. See  .

## See Also

- [func AEGetArray(UnsafePointer<AEDescList>!, AEArrayType, AEArrayDataPointer!, Size, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!, UnsafeMutablePointer<Int>!) -> OSErr](1445720-aegetarray.md)
  Extracts data from an Apple event array created with the `AEPutArray` function and stores it as a standard array of fixed size items in the specified buffer.
- [func AEGetNthPtr(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1447539-aegetnthptr.md)
  Gets a copy of the data from a descriptor at a specified position in a descriptor list; typically used when your application needs to work with the extracted data directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448326-aegetnthdesc)*