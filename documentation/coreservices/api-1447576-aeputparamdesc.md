# AEPutParamDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutParamDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to add a parameter to. See the [`AppleEvent`](appleevent.md) data type.
- `theAEKeyword`: The keyword specifying the parameter to add. If the Apple event already has a parameter with this keyword, the parameter is replaced. Some keyword constants are described in [`Keyword Parameter Constants`](apple_events/1527206-keyword_parameter_constants.md). See [`AEKeyword`](aekeyword.md).
- `theAEDesc`: A pointer to the descriptor for the parameter to add. See [`AEDesc`](aedesc.md).

## See Also

- [func AEPutAttributeDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](1441790-aeputattributedesc.md)
  Adds a descriptor and a keyword to an Apple event as an attribute.
- [func AEPutAttributePtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1445940-aeputattributeptr.md)
  Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.
- [func AEPutParamPtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447576-aeputparamdesc)*