# AEPutParamDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutParamDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr
```

```c
OSErr AEPutParamDesc(AppleEvent *theAppleEvent, AEKeyword theAEKeyword, const AEDesc *theAEDesc);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to add a parameter to. See the [`AppleEvent`](./appleevent.md) data type.
- `theAEKeyword`: The keyword specifying the parameter to add. If the Apple event already has a parameter with this keyword, the parameter is replaced.

  Some keyword constants are described in [Keyword Parameter Constants](./apple_events/api-1527206-keyword_parameter_constants.md).

  See [`AEKeyword`](./aekeyword.md).
- `theAEDesc`: A pointer to the descriptor for the parameter to add. See [`AEDesc`](./aedesc.md).

## See Also

### Adding Parameters and Attributes to Apple Events and Apple Event Records
- [func AEPutAttributeDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](./api-1441790-aeputattributedesc.md)
  Adds a descriptor and a keyword to an Apple event as an attribute.
- [func AEPutAttributePtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](./api-1445940-aeputattributeptr.md)
  Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.
- [func AEPutParamPtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](./api-1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [AEPutKeyDesc](../applicationservices/apple_event_manager/api-1805634-aeputkeydesc.md)
  Inserts a descriptor and a keyword into an Apple event record as an Apple event parameter.
- [AEPutKeyPtr](../applicationservices/apple_event_manager/api-1805645-aeputkeyptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event record as an Apple event parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447576-aeputparamdesc)*