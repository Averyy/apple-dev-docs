# AEBuildParameters

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Adds additional parameters or attributes to an existing Apple event.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus AEBuildParameters(AppleEvent *event, AEBuildError *error, const char *format, ...);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

This function can be called more than once to add any desired number of parameters or attributes to an existing Apple event. The Apple event should already have been created through either a call to [`AECreateAppleEvent`](./api-1448525-aecreateappleevent.md) or [`AEBuildAppleEvent`](./api-1573757-aebuildappleevent.md).

This function and related “AEBuild” routines provide a very simple translation service for converting specially formatted strings into complex Apple event descriptors. Normally, creating complex Apple event descriptors requires a large number of calls to Apple event Manager routines to build up the descriptor piece by piece. The `AEBuildDesc` function and related routines allow you to consolidate all of the calls required to construct a complex Apple event descriptor into a single system call that creates the desired structure as directed by a format string that you provide.

For additional information on using the AEBuild routines, see the descriptions for [`AEBuildAppleEvent`](./api-1573757-aebuildappleevent.md) and [`AEBuildDesc`](./api-1573758-aebuilddesc.md).

## Parameters

- `event`: The Apple event to which you are adding parameters. See [`AppleEvent`](./appleevent.md).
- `error`: A pointer to an `AEBuildError` structure where additional information about any errors that occur will be saved. This is an optional parameter and you can pass `NULL` if this information is not required. See [`AEBuildError`](./aebuilderror.md).
- `format`: An `AEBuild` format string describing the parameters to be created. 

## See Also

### Creating Apple Event Structures in Memory
- [AEBuildAppleEvent](./api-1573757-aebuildappleevent.md)
  Constructs an entire Apple event in a single call.
- [AEBuildDesc](./api-1573758-aebuilddesc.md)
  Provides a facility for compiling AEBuild descriptor strings into Apple event descriptors (`AEDesc`).
- [AEPrintDescToHandle](./api-1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [vAEBuildAppleEvent](./api-1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [vAEBuildDesc](./api-1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [vAEBuildParameters](./api-1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1573755-aebuildparameters)*