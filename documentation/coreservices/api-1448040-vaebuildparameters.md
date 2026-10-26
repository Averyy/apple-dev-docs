# vAEBuildParameters(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vAEBuildParameters(_ event: UnsafeMutablePointer<AppleEvent>!, _ error: UnsafeMutablePointer<AEBuildError>!, _ format: UnsafePointer<CChar>!, _ args: CVaListPointer) -> OSStatus
```

```c
OSStatus vAEBuildParameters(AppleEvent *event, AEBuildError *error, const char *format, va_list args);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

Passing an argument list to `vAEBuildParameters` corresponds to passing a series of individual parameters to the [`AEBuildParameters`](./api-1573755-aebuildparameters.md) function.

This function and related “AEBuild” routines provide a very simple translation service for converting specially formatted strings into complex Apple event descriptors. Normally, creating complex Apple event descriptors requires a large number of calls to Apple event Manager routines to build up the descriptor piece by piece. The `vAEBuildParameters` function and related routines allow you to consolidate all of the calls required to construct a complex Apple event descriptor into a single system call that creates the desired structure as directed by a format string that you provide.

## Parameters

- `event`: The Apple event to which you are adding parameters. See [`AppleEvent`](./appleevent.md).
- `error`: A pointer to an `AEBuildError` structure where additional information about any errors that occur will be saved. This is an optional parameter and you can pass `NULL` if this information is not required. See [`AEBuildError`](./aebuilderror.md).
- `format`: An `AEBuild` format string describing the `AEDesc` parameters to be created.
- `args`: A reference to a previously defined, variable argument parameter list to use with the descriptor-string. The file `<stdarg.h>` defines macros for declaring and using the `va_list` data type.

## See Also

### Creating Apple Event Structures in Memory
- [func AEPrintDescToHandle(UnsafePointer<AEDesc>!, UnsafeMutablePointer<Handle?>!) -> OSStatus](./api-1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [func vAEBuildAppleEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](./api-1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [func vAEBuildDesc(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](./api-1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [AEBuildAppleEvent](./api-1573757-aebuildappleevent.md)
  Constructs an entire Apple event in a single call.
- [AEBuildDesc](./api-1573758-aebuilddesc.md)
  Provides a facility for compiling AEBuild descriptor strings into Apple event descriptors (`AEDesc`).
- [AEBuildParameters](./api-1573755-aebuildparameters.md)
  Adds additional parameters or attributes to an existing Apple event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448040-vaebuildparameters)*