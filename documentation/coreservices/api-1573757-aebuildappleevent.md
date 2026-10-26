# AEBuildAppleEvent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Constructs an entire Apple event in a single call.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus AEBuildAppleEvent(AEEventClass theClass, AEEventID theID, DescType addressType, const void *addressData, Size addressLength, SInt16 returnID, SInt32 transactionID, AppleEvent *result, AEBuildError *error, const char *paramsFmt, ...);
```

#### Return Value

A numeric result code indicating the success of the call. A value of `AEBuildSyntaxNoErr` (zero) means the call succeeded. You can use the `error` parameter to discover information about other errors. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

**IMPORTANT:** Following the parameters described above, the `AEBuildAppleEvent` function takes a variable number of parameters as specified by the format string provided in the `paramsFmt` parameter.

This function and related “AEBuild” routines (including [`AEBuildDesc`](./api-1573758-aebuilddesc.md) and [`AEBuildParameters`](./api-1573755-aebuildparameters.md), and the variable-argument versions, [`vAEBuildAppleEvent`](./api-1441729-vaebuildappleevent.md), [`vAEBuildDesc`](./api-1446775-vaebuilddesc.md), and [`vAEBuildParameters`](./api-1448040-vaebuildparameters.md)) provide a very simple translation service for converting specially formatted strings into complex Apple event descriptors. Normally, creating complex Apple event descriptors requires a large number of calls to Apple event Manager routines to build up the descriptor piece by piece. The `AEBuildAppleEvent` function and related routines allow you to consolidate all of the calls required to construct a complex Apple event descriptor into a single system call that creates the desired structure as directed by a format string that you provide.

In many ways, the AEBuild routines are very much like the standard C library's `printf` suite of routines. The syntax for the format string that you provide is very simple and allows for the substitution of data items into the Apple event descriptors being created.

The `AEBuildAppleEvent` function is similar to [`AECreateAppleEvent`](./api-1448525-aecreateappleevent.md), but in addition to creating the Apple event, it also constructs the parameters for the event from the last three arguments. You can use `AEBuildAppleEvent` to build an entire Apple event, or [`AEBuildParameters`](./api-1573755-aebuildparameters.md) to add additional parameters to an existing Apple event.

The syntax of the formatting string for an entire Apple event (as passed to `AEBuildAppleEvent`) is almost identical to that used to represent the contents of an Apple event, without the curly braces. The event is defined as a sequence of name-value pairs, with optional parameters preceded with a tilde (~) character. The syntax is described in Technical Note TN2106, [AEBuild*, AEPrint*, and Friends](http://developer.apple.com/technotes/tn/tn2045.html).

It is important to note that the identifier for the direct parameter in an Apple event, specified by the constant `keyDirectObject`, is four minus signs (`'----'`). The minus sign has special meaning in AEBuild strings, and it should always be enclosed in single quotes when it is used to identify the direct parameter for an Apple event in a descriptor string.

##### Version-Notes

Prior to OS X version 10.3, `AEBuildAppleEvent` would fail if you supplied a data parameter with size greater than 32767 bytes.

## Parameters

- `theClass`: The event class for the resulting Apple event. See [`AEEventClass`](./aeeventclass.md).
- `theID`: The event id for the resulting Apple event. See [`AEEventID`](./aeeventid.md).
- `addressType`: The address type for the addressing information described in the next two parameters: usually one of `typeApplSignature`, `typeProcessSerialNumber`, or `typeKernelProcessID`. See [`DescType`](./desctype.md).
- `addressData`: A pointer to the address information.
- `addressLength`: The number of bytes pointed to by the `addressData` parameter.
- `returnID`: The return ID for the created Apple event. If you pass a value of `kAutoGenerateReturnID`, the Apple Event Manager assigns the created Apple event a return ID that is unique to the current session. If you pass any other value, the Apple Event Manager assigns that value for the ID.
- `transactionID`: The transaction ID for this Apple event. A transaction is a sequence of Apple events that are sent back and forth between the client and server applications, beginning with the client’s initial request for a service. All Apple events that are part of a transaction must have the same transaction ID. You can specify the `kAnyTransactionID` constant if the Apple event is not one of a series of interdependent Apple events.
- `result`: A pointer to a descriptor where the resulting descriptor should be stored. See [`AppleEvent`](./appleevent.md) for a description of the data type.
- `error`: A pointer to an `AEBuildError` structure where additional information about any errors that occur will be saved. This is an optional parameter and you can pass `NULL` if this information is not required. See [`AEBuildError`](./aebuilderror.md) for a description of the data type.
- `paramsFmt`: An AEBuild format string describing the AppleEvent record to be created. The format of these strings is described in Technical Note TN2106, [AEBuild*, AEPrint*, and Friends](http://developer.apple.com/technotes/tn/tn2045.html). That technote also describes possible error return codes for syntax errors in the format string.

## See Also

### Creating Apple Event Structures in Memory
- [AEBuildDesc](./api-1573758-aebuilddesc.md)
  Provides a facility for compiling AEBuild descriptor strings into Apple event descriptors (`AEDesc`).
- [AEBuildParameters](./api-1573755-aebuildparameters.md)
  Adds additional parameters or attributes to an existing Apple event.
- [AEPrintDescToHandle](./api-1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [vAEBuildAppleEvent](./api-1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [vAEBuildDesc](./api-1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [vAEBuildParameters](./api-1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1573757-aebuildappleevent)*