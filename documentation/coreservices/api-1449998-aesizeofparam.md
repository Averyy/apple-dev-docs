# AESizeOfParam(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AESizeOfParam(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to get the parameter data from. See  .
- `theAEKeyword`: The keyword that specifies the desired parameter. Some keyword parameter constants are described in  . See  .
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the Apple event parameter. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataSize`: A pointer to a size variable. On return, the length, in bytes, of the data in the Apple event parameter.

## See Also

- [func AESizeOfAttribute(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1445764-aesizeofattribute.md)
  Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.
- [func AESizeOfNthItem(UnsafePointer<AEDescList>!, Int, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1447307-aesizeofnthitem.md)
  Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449998-aesizeofparam)*