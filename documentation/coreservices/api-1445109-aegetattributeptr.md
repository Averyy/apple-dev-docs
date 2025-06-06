# AEGetAttributePtr(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetAttributePtr(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

To get Apple event attribute data for your application to use directly, call `AEGetAttributePtr`. To get a descriptor for an Apple event attribute to pass on to another Apple Event Manager routine, call [`AEGetAttributeDesc(_:_:_:_:)`](1450314-aegetattributedesc.md).

Before calling `AEGetAttributePtr`, you can call the [`AESizeOfAttribute(_:_:_:_:)`](1445764-aesizeofattribute.md) function to determine a size for the `dataPtr` buffer. However, unless you specify `typeWildCard` for the `desiredType` parameter, `AEGetAttributePtr` may coerce the data, which may cause the size of the data to change. 

##### 1770187

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to get the attribute data from. See  .
- `theAEKeyword`: The keyword that specifies the desired attribute. Some keyword constants are described in  . See  .
- `desiredType`: See  .
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the attribute data pointed to by  . The returned type is either the same as the type specified by the   parameter or, if the desired type was type wildcard, the true type of the descriptor. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataPtr`: A pointer to a buffer, local variable, or other storage location, created and disposed of by your application. The size in bytes must be at least as large as the value you pass in the   parameter. On return, contains the attribute data.
- `maximumSize`: The maximum length, in bytes, of the expected attribute data. The   function will not return more data than you specify in this parameter. 
- `actualSize`: A pointer to a size variable. On return, the length, in bytes, of the data for the specified Apple event attribute. If this value is larger than the value you passed in the   parameter, the buffer pointed to by   was not large enough to contain all of the data for the attribute, though   does not write beyond the end of the buffer. If the buffer was too small, you can resize it and call   again.

## See Also

- [func AEGetAttributeDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450314-aegetattributedesc.md)
  Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.
- [func AEGetParamDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449233-aegetparamdesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.
- [func AEGetParamPtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445109-aegetattributeptr)*