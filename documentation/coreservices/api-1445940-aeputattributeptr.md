# AEPutAttributePtr(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutAttributePtr(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to add an attribute to. See the   data type.
- `theAEKeyword`: See  .
- `typeCode`: The descriptor type for the attribute to add. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataPtr`: A pointer to the data for the attribute to add.
- `dataSize`: The length, in bytes, of the data for the attribute to add.

## See Also

- [func AEPutAttributeDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](1441790-aeputattributedesc.md)
  Adds a descriptor and a keyword to an Apple event as an attribute.
- [func AEPutParamDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](1447576-aeputparamdesc.md)
  Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [func AEPutParamPtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445940-aeputattributeptr)*