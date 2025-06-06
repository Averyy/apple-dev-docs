# AEStreamWriteKeyDesc(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Writes a complete keyword/descriptor pair to an `AEStreamRef`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEStreamWriteKeyDesc(_ ref: AEStreamRef!, _ key: AEKeyword, _ newType: DescType, _ data: UnsafeRawPointer!, _ length: Size) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Use this routine to add a descriptor to the currently open `AERecord` inside a stream. You cannot use this routine to write parameters to any other types of descriptors, even if they are nested inside of an `AERecord`. This routine can only be called in between calls to [`AEStreamOpenRecord(_:_:)`](1447141-aestreamopenrecord.md) and [`AEStreamCloseRecord(_:)`](1449522-aestreamcloserecord.md). 

This method is analogous to the Apple Event Manager routine [`AEPutParamPtr(_:_:_:_:_:)`](1449263-aeputparamptr.md), except it is for use with streams.

## Parameters

- `ref`: An   containing the stream data.
- `key`: The   associated with the new descriptor being added to the stream. See  .
- `newType`: A type code for the new   being added to the stream. See  .
- `data`: A pointer to the block of memory containing the descriptor data. This routine copies the memory block immediately, so you do not need to retain it for the benefit of this routine.
- `length`: The number of bytes pointed to by the   parameter.

## See Also

- [func AEStreamClose(AEStreamRef!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1449821-aestreamclose.md)
  Closes and deallocates an `AEStreamRef`.
- [func AEStreamCloseDesc(AEStreamRef!) -> OSStatus](1449272-aestreamclosedesc.md)
  Marks the end of a descriptor in an `AEStreamRef`.
- [func AEStreamCloseList(AEStreamRef!) -> OSStatus](1448185-aestreamcloselist.md)
  Marks the end of a list of descriptors in an `AEStreamRef`.
- [func AEStreamCloseRecord(AEStreamRef!) -> OSStatus](1449522-aestreamcloserecord.md)
  Marks the end of a record in an `AEStreamRef`.
- [func AEStreamCreateEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32) -> AEStreamRef!](1446562-aestreamcreateevent.md)
  Creates a new Apple event and opens a stream for writing data to it.
- [func AEStreamOpen() -> AEStreamRef!](1447732-aestreamopen.md)
  Opens a new `AEStreamRef` for use in building a descriptor.
- [func AEStreamOpenDesc(AEStreamRef!, DescType) -> OSStatus](1446544-aestreamopendesc.md)
  Marks the beginning of a descriptor in an `AEStreamRef`.
- [func AEStreamOpenEvent(UnsafeMutablePointer<AppleEvent>!) -> AEStreamRef!](1445366-aestreamopenevent.md)
  Opens a stream for an existing Apple event.
- [func AEStreamOpenKeyDesc(AEStreamRef!, AEKeyword, DescType) -> OSStatus](1442897-aestreamopenkeydesc.md)
  Marks the beginning of a key descriptor in an `AEStreamRef`.
- [func AEStreamOpenList(AEStreamRef!) -> OSStatus](1448594-aestreamopenlist.md)
  Marks the beginning of a descriptor list in an `AEStreamRef`.
- [func AEStreamOpenRecord(AEStreamRef!, DescType) -> OSStatus](1447141-aestreamopenrecord.md)
  Marks the beginning of an Apple event record in an `AEStreamRef`.
- [func AEStreamOptionalParam(AEStreamRef!, AEKeyword) -> OSStatus](1444481-aestreamoptionalparam.md)
  Designates a parameter in an Apple event as optional.
- [func AEStreamSetRecordType(AEStreamRef!, DescType) -> OSStatus](1447704-aestreamsetrecordtype.md)
  Sets the type of the most recently created record in an `AEStreamRef`.
- [func AEStreamWriteAEDesc(AEStreamRef!, UnsafePointer<AEDesc>!) -> OSStatus](1448487-aestreamwriteaedesc.md)
  Copies an existing descriptor into an `AEStreamRef`.
- [func AEStreamWriteData(AEStreamRef!, UnsafeRawPointer!, Size) -> OSStatus](1442610-aestreamwritedata.md)
  Appends data to the current descriptor in an `AEStreamRef`.
- [func AEStreamWriteDesc(AEStreamRef!, DescType, UnsafeRawPointer!, Size) -> OSStatus](1450387-aestreamwritedesc.md)
  Appends the data for a complete descriptor to an `AEStreamRef`.
- [func AEStreamWriteKey(AEStreamRef!, AEKeyword) -> OSStatus](1448750-aestreamwritekey.md)
  Marks the beginning of a keyword/descriptor pair for a descriptor in an `AEStreamRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442568-aestreamwritekeydesc)*