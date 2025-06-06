# AEPrintDescToHandle(_:_:)

**Framework**: Core Services  
**Kind**: func

Provides a pretty printer facility for displaying the contents of Apple event descriptors.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEPrintDescToHandle(_ desc: UnsafePointer<AEDesc>!, _ result: UnsafeMutablePointer<Handle?>!) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The data handle returned in the `result` parameter contains a text string formatted using the “AEBuild” syntax. This string is useful for looking at the contents of Apple events sent by other applications and for debugging your own descriptors.

`AEPrintDescToHandle` prints the contents of `AEDesc`, `AERecord`, and `AEDescList` descriptors in a format that is suitable for input to [`AEBuildDesc`](1573758-aebuilddesc.md). `AEPrintDescToHandle` also attempts display coerced Apple event records as the coerced record type instead of as the original type. Any data structures that cannot be identified are displayed as hexadecimal data.

`AEPrintDescToHandle` prints the contents of Apple events in a slightly different format. For these events, the event class and event ID appear at the beginning of the output string, followed by the contents of the event enclosed in curly braces. In addition, each attribute is printed with its four-character identifier and preceded by an ampersand character. You cannot use the output string to recreate the Apple event from [`AEBuildAppleEvent`](1573757-aebuildappleevent.md).

## Parameters

- `desc`: A pointer to a descriptor containing the information to be printed. See  .
- `result`: A pointer to a location for a new   data type. On return, contains a new handle allocated by the Memory Manager.

## See Also

- [func vAEBuildAppleEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [func vAEBuildDesc(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [func vAEBuildParameters(UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445158-aeprintdesctohandle)*