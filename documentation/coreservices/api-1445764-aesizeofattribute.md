# AESizeOfAttribute(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AESizeOfAttribute(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to get the attribute data from. See [`AppleEvent`](appleevent.md).
- `theAEKeyword`: The keyword that specifies the attribute. Some keyword constants are described in [`Keyword Attribute Constants`](apple_events/1542920-keyword_attribute_constants.md). See [`AEKeyword`](aekeyword.md).
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the attribute. For a list of AppleScript’s predefined descriptor types, see [`Descriptor Type Constants`](apple_events/1542788-descriptor_type_constants.md). Can be `NULL`. See [`DescType`](desctype.md).
- `dataSize`: A pointer to a size variable. On return, the length, in bytes, of the data in the attribute. Can be `NULL`.

## See Also

- [func AESizeOfNthItem(UnsafePointer<AEDescList>!, Int, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1447307-aesizeofnthitem.md)
  Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.
- [func AESizeOfParam(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1449998-aesizeofparam.md)
  Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445764-aesizeofattribute)*