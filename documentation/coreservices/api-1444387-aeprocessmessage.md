# AEProcessMessage(_:)

**Framework**: Core Services  
**Kind**: func

Decodes and dispatches a low level Mach message event to an event handler, including packaging and returning the reply to the sender.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEProcessMessage(_ header: UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The Apple Event Manager provides the following functions (in macOS only) for working with Apple events at a lower level: [`AEGetRegisteredMachPort()`](1449736-aegetregisteredmachport.md), [`AEDecodeMessage(_:_:_:)`](1447827-aedecodemessage.md), [`AESendMessage(_:_:_:_:)`](1442994-aesendmessage.md), and `AEProcessMessage`. See the descriptions for those functions for more information on when you might use them.

If your daemon or other code has initialized a Mach port and is listening on it for Apple events and other messages, it can call `AEProcessMessage` to handle any incoming events it identifies as Apple events, while handling other types of events itself. `AEProcessMessage` will dispatch the event to an event handler (by calling `AEDecodeMessage` for you) and package and return the reply to the sender, simplifying handling for your code.

The Apple Event Manager reserves Mach message IDs in the range 0 to 999 for its own use. `AEProcessMessage` returns a `paramErr` result code if the Mach message did not contain an Apple event. 

## Parameters

- `header`: A pointer to the received Mach message that should be processed. The contents of the message header are invalid after calling this method.

## See Also

- [func AEGetRegisteredMachPort() -> mach_port_t](1449736-aegetregisteredmachport.md)
  Returns the Mach port (in the form of a `mach_port_t`) that was registered with the bootstrap server for this process.
- [func AEDecodeMessage(UnsafeMutablePointer<mach_msg_header_t>!, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!) -> OSStatus](1447827-aedecodemessage.md)
  Decodes a Mach message and converts it into an Apple event and its related reply.
- [func AESendMessage(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, AESendMode, Int) -> OSStatus](1442994-aesendmessage.md)
  Sends an AppleEvent to a target process without some of the overhead required by `AESend`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444387-aeprocessmessage)*