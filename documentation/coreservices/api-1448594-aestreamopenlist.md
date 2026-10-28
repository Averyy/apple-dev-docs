# AEStreamOpenList(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Marks the beginning of a descriptor list in an `AEStreamRef`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEStreamOpenList(_ ref: AEStreamRef!) -> OSStatus
```

```c
OSStatus AEStreamOpenList(AEStreamRef ref);
```

## Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

## Discussion

This routine marks the beginning of a sequence of zero or more descriptor definitions that you use to build an `AEDescList` structure. After calling this routine, you can write any number of `AEDesc`, `AEDescList`, or `AERecord` structures to the stream as elements of the list. When you are done, you must call [`AEStreamCloseList(_:)`](./api-1448185-aestreamcloselist.md) to complete the `AEDescList` definition. 

## Parameters

- `ref`: An [`AEStreamRef`](./aestreamref.md) containing the stream data.

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
- [func AEStreamOpenKeyDesc(AEStreamRef!, AEKeyword, DescType) -> OSStatus](./api-1442897-aestreamopenkeydesc.md)
  Marks the beginning of a key descriptor in an `AEStreamRef`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448594-aestreamopenlist)*