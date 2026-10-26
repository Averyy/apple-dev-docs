# AESizeOfParam(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AESizeOfParam(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: UnsafeMutablePointer<DescType>!, _ dataSize: UnsafeMutablePointer<Size>!) -> OSErr
```

```c
OSErr AESizeOfParam(const AppleEvent *theAppleEvent, AEKeyword theAEKeyword, DescType *typeCode, Size *dataSize);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to get the parameter data from. See [`AppleEvent`](./appleevent.md).
- `theAEKeyword`: The keyword that specifies the desired parameter. Some keyword parameter constants are described in [Keyword Parameter Constants](./apple_events/api-1527206-keyword_parameter_constants.md). See [`AEKeyword`](./aekeyword.md).
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the Apple event parameter. For a list of AppleScript’s predefined descriptor types, see [Descriptor Type Constants](./apple_events/api-1542788-descriptor_type_constants.md). See [`DescType`](./desctype.md).
- `dataSize`: A pointer to a size variable. On return, the length, in bytes, of the data in the Apple event parameter.

## See Also

### Getting the Sizes and Descriptor Types of Descriptors
- [func AESizeOfAttribute(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](./api-1445764-aesizeofattribute.md)
  Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.
- [func AESizeOfNthItem(UnsafePointer<AEDescList>!, Int, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](./api-1447307-aesizeofnthitem.md)
  Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.
- [AESizeOfKeyDesc](../applicationservices/apple_event_manager/api-1806296-aesizeofkeydesc.md)
  Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449998-aesizeofparam)*