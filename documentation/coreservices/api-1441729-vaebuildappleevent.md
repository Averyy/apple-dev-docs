# vAEBuildAppleEvent(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vAEBuildAppleEvent(_ theClass: AEEventClass, _ theID: AEEventID, _ addressType: DescType, _ addressData: UnsafeRawPointer!, _ addressLength: Size, _ returnID: Int16, _ transactionID: Int32, _ resultEvt: UnsafeMutablePointer<AppleEvent>!, _ error: UnsafeMutablePointer<AEBuildError>!, _ paramsFmt: UnsafePointer<CChar>!, _ args: CVaListPointer) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Passing an argument list to `vAEBuildAppleEvent` corresponds to passing a series of individual parameters to the [`AEBuildAppleEvent`](1573757-aebuildappleevent.md) function.

This function and related “AEBuild” routines provide a very simple translation service for converting specially formatted strings into complex Apple event descriptors. Normally, creating complex Apple event descriptors requires a large number of calls to Apple event Manager routines to build up the descriptor piece by piece. The `vAEBuildAppleEvent` function and related routines allow you to consolidate all of the calls required to construct a complex Apple event descriptor into a single system call that creates the desired structure as directed by a format string that you provide.

## Parameters

- `theClass`: The event class for the resulting Apple event. See  .
- `theID`: The event id for the resulting Apple event. See  .
- `addressType`: The address type for the addressing information described in the next two parameters: usually one of  ,  , or  . See  .
- `addressData`: A pointer to the address information.
- `addressLength`: The number of bytes pointed to by the   parameter.
- `returnID`: The return ID for the created Apple event. If you pass a value of  , the Apple Event Manager assigns the created Apple event a return ID that is unique to the current session. If you pass any other value, the Apple Event Manager assigns that value for the ID.
- `transactionID`: The transaction ID for this Apple event. A transaction is a sequence of Apple events that are sent back and forth between the client and server applications, beginning with the client’s initial request for a service. All Apple events that are part of a transaction must have the same transaction ID. You can specify the   constant if the Apple event is not one of a series of interdependent Apple events.
- `result`: A pointer to a descriptor where the resulting descriptor should be stored. See   for a description of the data type.
- `error`: A pointer to an   structure where additional information about any errors that occur will be saved. This is an optional parameter and you can pass   if this information is not required. See   for the syntax error codes that can be returned in this structure.
- `paramsFmt`: An AEBuild format string describing the AppleEvent record to be created. The format of these strings is described in Technical Note TN2106,  . 
- `args`: A variable array of arguments to be substituted into the   format string. See the ANSI C Interfaces documentation for a description of the   data type.

## See Also

- [func AEPrintDescToHandle(UnsafePointer<AEDesc>!, UnsafeMutablePointer<Handle?>!) -> OSStatus](1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [func vAEBuildDesc(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [func vAEBuildParameters(UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441729-vaebuildappleevent)*