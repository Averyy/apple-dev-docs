# vAEBuildDesc(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vAEBuildDesc(_ dst: UnsafeMutablePointer<AEDesc>!, _ error: UnsafeMutablePointer<AEBuildError>!, _ src: UnsafePointer<CChar>!, _ args: CVaListPointer) -> OSStatus
```

#### Return_value

A numeric result code indicating the success of the call. A value of `AEBuildSyntaxNoErr` (zero) means the call succeeded. You can use the `error` parameter to discover information about other errors. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Passing an argument list to `vAEBuildDesc` corresponds to passing a series of individual parameters to the [`AEBuildDesc`](1573758-aebuilddesc.md) function.

This function and related “AEBuild” routines provide a very simple translation service for converting specially formatted strings into complex Apple event descriptors. Normally, creating complex Apple event descriptors requires a large number of calls to Apple Event Manager routines to build up the descriptor piece by piece. The `vAEBuildDesc` function and related routines allow you to consolidate all of the calls required to construct a complex Apple event descriptor into a single system call that creates the desired structure as directed by a format string that you provide.

## Parameters

- `dst`: A pointer to a descriptor where the resulting descriptor should be stored. See  .
- `error`: A pointer to an   structure where additional information about any errors that occur will be saved. This is an optional parameter and you can pass   if this information is not required. See  .
- `src`: An   format string describing the descriptor to be created.
- `args`: A reference to a previously defined, variable argument parameter list to use with the descriptor-string. The file   defines macros for declaring and using the   data type.

## See Also

- [func AEPrintDescToHandle(UnsafePointer<AEDesc>!, UnsafeMutablePointer<Handle?>!) -> OSStatus](1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [func vAEBuildAppleEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [func vAEBuildParameters(UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446775-vaebuilddesc)*