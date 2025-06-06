# AEStreamClose(_:_:)

**Framework**: Core Services  
**Kind**: func

Closes and deallocates an `AEStreamRef`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEStreamClose(_ ref: AEStreamRef!, _ desc: UnsafeMutablePointer<AEDesc>!) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Use this function to dispose of an `AEStreamRef` you created using [`AEStreamCreateEvent(_:_:_:_:_:_:_:)`](1446562-aestreamcreateevent.md), [`AEStreamOpen()`](1447732-aestreamopen.md), or [`AEStreamOpenEvent(_:)`](1445366-aestreamopenevent.md). To retrieve the resulting descriptor from the stream prior to disposal, pass in a pointer to an `AEDesc` structure in the `desc` parameter. If this parameter exists, `AEStreamClose` fills in the descriptor with the stream data. If the stream contains invalid information, possibly due to improperly balanced calls to “AEStream” functions, the returned descriptor type is set to `typeNull`. 

Regardless of any errors returned by this function, it is always safe to call [`AEDisposeDesc(_:)`](1444208-aedisposedesc.md) on the returned descriptor. 

Specifying `NULL` for the `desc` parameter causes `AEStreamClose` to discard the stream data and dispose of the `AEStreamRef`. When you call `AEStreamClose` in this way, you do not need to worry about balancing nested calls to “AEStream” functions. This technique is particularly useful during error-handling situations where you need to dispose of a stream but do not know its exact state. 

## Parameters

- `ref`: An  containing the stream data.
- `desc`: A pointer to a descriptor for receiving a the stream data, or   if you want to discard the data. See  .

## See Also

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
- [func AEStreamWriteKeyDesc(AEStreamRef!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSStatus](1442568-aestreamwritekeydesc.md)
  Writes a complete keyword/descriptor pair to an `AEStreamRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449821-aestreamclose)*