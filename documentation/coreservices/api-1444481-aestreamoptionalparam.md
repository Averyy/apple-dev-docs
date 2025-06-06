# AEStreamOptionalParam(_:_:)

**Framework**: Core Services  
**Kind**: func

Designates a parameter in an Apple event as optional.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEStreamOptionalParam(_ ref: AEStreamRef!, _ key: AEKeyword) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Calls to this routine must be preceded by a call to either [`AEStreamCreateEvent(_:_:_:_:_:_:_:)`](1446562-aestreamcreateevent.md) or [`AEStreamOpenEvent(_:)`](1445366-aestreamopenevent.md). 

The descriptor associated with the specified `key` does not need to exist before you call this routine. 

## Parameters

- `ref`: An   containing the stream data.
- `key`: The   associated with any keyword/descriptor pair in an Apple event. See  .

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
- [func AEStreamWriteKeyDesc(AEStreamRef!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSStatus](1442568-aestreamwritekeydesc.md)
  Writes a complete keyword/descriptor pair to an `AEStreamRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444481-aestreamoptionalparam)*