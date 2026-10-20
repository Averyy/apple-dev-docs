# AEStreamOpenKeyDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Marks the beginning of a key descriptor in an `AEStreamRef`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEStreamOpenKeyDesc(_ ref: AEStreamRef!, _ key: AEKeyword, _ newType: DescType) -> OSStatus
```

```c
OSStatus AEStreamOpenKeyDesc(AEStreamRef ref, AEKeyword key, DescType newType);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

Use this routine to mark the beginning of a keyword/descriptor definition in an Apple event record. After calling this routine, you should call [`AEStreamWriteData(_:_:_:)`](./api-1442610-aestreamwritedata.md) one or more times to write the record data to the stream. When you are done writing data, you must call [`AEStreamCloseDesc(_:)`](./api-1449272-aestreamclosedesc.md) to complete the record definition. 

This routine must be called only as part of an Apple event record definition. You cannot use this routine to write keyword/descriptor definitions to other descriptor types, such as an `AEDesc` or `AEDescList`, even if those types are nested inside an Apple event record. In situations where you need to create nested records, this routine opens a new keyword/descriptor definition in the Apple event record associated with the most recent call to [`AEStreamOpenRecord(_:_:)`](./api-1447141-aestreamopenrecord.md). 

## Parameters

- `ref`: An [`AEStreamRef`](./aestreamref.md) containing the stream data.
- `key`: The `AEKeyword` associated with the new descriptor being added to the stream. See [`AEKeyword`](./aekeyword.md).
- `newType`: A type code for the new `AEDesc` being added to the stream. See [`DescType`](./desctype.md).

## See Also

### Creating Apple Event Structures Using Streams
- [func AEStreamClose(AEStreamRef!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](./api-1449821-aestreamclose.md)
  Closes and deallocates an `AEStreamRef`.
- [func AEStreamCloseDesc(AEStreamRef!) -> OSStatus](./api-1449272-aestreamclosedesc.md)
  Marks the end of a descriptor in an `AEStreamRef`.
- [func AEStreamCloseList(AEStreamRef!) -> OSStatus](./api-1448185-aestreamcloselist.md)
  Marks the end of a list of descriptors in an `AEStreamRef`.
- [func AEStreamCloseRecord(AEStreamRef!) -> OSStatus](./api-1449522-aestreamcloserecord.md)
  Marks the end of a record in an `AEStreamRef`.
- [func AEStreamCreateEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32) -> AEStreamRef!](./api-1446562-aestreamcreateevent.md)
  Creates a new Apple event and opens a stream for writing data to it.
- [func AEStreamOpen() -> AEStreamRef!](./api-1447732-aestreamopen.md)
  Opens a new `AEStreamRef` for use in building a descriptor.
- [func AEStreamOpenDesc(AEStreamRef!, DescType) -> OSStatus](./api-1446544-aestreamopendesc.md)
  Marks the beginning of a descriptor in an `AEStreamRef`.
- [func AEStreamOpenEvent(UnsafeMutablePointer<AppleEvent>!) -> AEStreamRef!](./api-1445366-aestreamopenevent.md)
  Opens a stream for an existing Apple event.
- [func AEStreamOpenList(AEStreamRef!) -> OSStatus](./api-1448594-aestreamopenlist.md)
  Marks the beginning of a descriptor list in an `AEStreamRef`.
- [func AEStreamOpenRecord(AEStreamRef!, DescType) -> OSStatus](./api-1447141-aestreamopenrecord.md)
  Marks the beginning of an Apple event record in an `AEStreamRef`.
- [func AEStreamOptionalParam(AEStreamRef!, AEKeyword) -> OSStatus](./api-1444481-aestreamoptionalparam.md)
  Designates a parameter in an Apple event as optional.
- [func AEStreamSetRecordType(AEStreamRef!, DescType) -> OSStatus](./api-1447704-aestreamsetrecordtype.md)
  Sets the type of the most recently created record in an `AEStreamRef`.
- [func AEStreamWriteAEDesc(AEStreamRef!, UnsafePointer<AEDesc>!) -> OSStatus](./api-1448487-aestreamwriteaedesc.md)
  Copies an existing descriptor into an `AEStreamRef`.
- [func AEStreamWriteData(AEStreamRef!, UnsafeRawPointer!, Size) -> OSStatus](./api-1442610-aestreamwritedata.md)
  Appends data to the current descriptor in an `AEStreamRef`.
- [func AEStreamWriteDesc(AEStreamRef!, DescType, UnsafeRawPointer!, Size) -> OSStatus](./api-1450387-aestreamwritedesc.md)
  Appends the data for a complete descriptor to an `AEStreamRef`.
- [func AEStreamWriteKey(AEStreamRef!, AEKeyword) -> OSStatus](./api-1448750-aestreamwritekey.md)
  Marks the beginning of a keyword/descriptor pair for a descriptor in an `AEStreamRef`.
- [func AEStreamWriteKeyDesc(AEStreamRef!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSStatus](./api-1442568-aestreamwritekeydesc.md)
  Writes a complete keyword/descriptor pair to an `AEStreamRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442897-aestreamopenkeydesc)*