# AEDecodeMessage(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Decodes a Mach message and converts it into an Apple event and its related reply.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDecodeMessage(_ header: UnsafeMutablePointer<mach_msg_header_t>!, _ event: UnsafeMutablePointer<AppleEvent>!, _ reply: UnsafeMutablePointer<AppleEvent>!) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The Apple Event Manager provides the following functions (in macOS only) for working with Apple events at a lower level: [`AEGetRegisteredMachPort()`](1449736-aegetregisteredmachport.md), `AEDecodeMessage`, [`AESendMessage(_:_:_:_:)`](1442994-aesendmessage.md), and [`AEProcessMessage(_:)`](1444387-aeprocessmessage.md). See the descriptions for those functions for more information on when you might use them.

## Parameters

- `header`: A pointer to a Mach message header for the event to be decoded.
- `event`: A pointer to a null Apple event descriptor (one with descriptor type  ). On successful completion, contains the decoded Apple event. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it.
- `reply`: A pointer to a null Apple event descriptor. On successful completion, contains the reply event from the decoded Apple event. To send the reply, you use the following:

## See Also

- [func AEGetRegisteredMachPort() -> mach_port_t](1449736-aegetregisteredmachport.md)
  Returns the Mach port (in the form of a `mach_port_t`) that was registered with the bootstrap server for this process.
- [func AESendMessage(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, AESendMode, Int) -> OSStatus](1442994-aesendmessage.md)
  Sends an AppleEvent to a target process without some of the overhead required by `AESend`.
- [func AEProcessMessage(UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus](1444387-aeprocessmessage.md)
  Decodes and dispatches a low level Mach message event to an event handler, including packaging and returning the reply to the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447827-aedecodemessage)*