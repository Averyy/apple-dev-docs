# AEGetParamDesc(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetParamDesc(_ theAppleEvent: UnsafePointer<AppleEvent>!, _ theAEKeyword: AEKeyword, _ desiredType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

 You typically call `AEGetParamDesc` to get a descriptor for an Apple event parameter to pass on to another Apple Event Manager routine. To get Apple event parameter data for your application to use directly, call [`AEGetParamPtr(_:_:_:_:_:_:_:)`](1444069-aegetparamptr.md).

If the actual parameter you are getting with `AEGetParamDesc` is a record, you can only request it as a `typeAERecord`, `typeAEList`, or `typeWildcard`. For any other type, `AEGetParamDesc` will return `errAECoercionFail`.

##### 1770190

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event to get the parameter descriptor from.
- `theAEKeyword`: A keyword that specifies the desired Apple event parameter. Some keyword constants are described in  .
- `desiredType`: If the requested Apple event parameter is not of the desired type, the Apple Event Manager attempts to coerce it to the desired type. However, if you pass a value of  , no coercion is performed, and the descriptor type of the returned descriptor is the same as the descriptor type of the Apple event parameter.
- `result`: A pointer to a descriptor. On successful return, a copy of the descriptor for the specified Apple event parameter, coerced, if necessary, to the descriptor type specified by the   parameter. On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it.

## See Also

- [func AEGetAttributeDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450314-aegetattributedesc.md)
  Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.
- [func AEGetAttributePtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1445109-aegetattributeptr.md)
  Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.
- [func AEGetParamPtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449233-aegetparamdesc)*