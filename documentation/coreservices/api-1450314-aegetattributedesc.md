# AEGetAttributeDesc(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetAttributeDesc(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

To get Apple event attribute data for your application to use directly, call [`AEGetAttributePtr(_:_:_:_:_:_:_:)`](1445109-aegetattributeptr.md). To get a descriptor for an Apple event attribute to pass on to another Apple Event Manager routine, call `AEGetAttributeDesc`. 

##### 1770186

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to get the attribute descriptor from. See  .
- `theAEKeyword`: The keyword that specifies the desired attribute. Some keyword constants are described in  . See  .
- `result`: A pointer to a descriptor. On successful return, a copy of the specified Apple event attribute, coerced, if necessary, to the descriptor type specified in  . On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it. See  .

## See Also

- [func AEGetAttributePtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1445109-aegetattributeptr.md)
  Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.
- [func AEGetParamDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449233-aegetparamdesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.
- [func AEGetParamPtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450314-aegetattributedesc)*