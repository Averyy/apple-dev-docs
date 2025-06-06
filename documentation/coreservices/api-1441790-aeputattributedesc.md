# AEPutAttributeDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Adds a descriptor and a keyword to an Apple event as an attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPutAttributeDesc(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ theAEDesc: UnsafePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The `AEPutAttributeDesc` function takes a descriptor and a keyword and adds them to an Apple event as an attribute. If the descriptor type required for the attribute is different from the descriptor type of the descriptor, the Apple Event Manager attempts to coerce the descriptor into the required type, with one exception: the Apple Event Manager does not attempt to coerce the data for an address attribute, thereby allowing applications to use their own address types. 

##### 1770167

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to add an attribute to. See the   data type.
- `theAEKeyword`: See  .
- `theAEDesc`: A pointer to the descriptor to assign to the attribute. The descriptor type of the specified descriptor should match the defined descriptor type for that attribute. See  .

## See Also

- [func AEPutAttributePtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1445940-aeputattributeptr.md)
  Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.
- [func AEPutParamDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](1447576-aeputparamdesc.md)
  Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [func AEPutParamPtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441790-aeputattributedesc)*