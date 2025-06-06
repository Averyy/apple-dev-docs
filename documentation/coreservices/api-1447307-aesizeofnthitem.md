# AESizeOfNthItem(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AESizeOfNthItem(_ theAEDescList: UnsafePointer<AEDescList>!, _ index: Int, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list containing the descriptor. See  .
- `index`: A one-based positive integer indicating the position of the descriptor to get the data size for.   returns an error if you pass zero, a negative number, or a value that is out of range.
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the descriptor. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataSize`: A pointer to a size variable. On return, the length (in bytes) of the data in the descriptor.

## See Also

- [func AESizeOfAttribute(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1445764-aesizeofattribute.md)
  Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.
- [func AESizeOfParam(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1449998-aesizeofparam.md)
  Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447307-aesizeofnthitem)*