# AESendMessage(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Sends an AppleEvent to a target process without some of the overhead required by `AESend`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AESendMessage(_ event: UnsafePointer<AppleEvent>!, _ reply: UnsafeMutablePointer<AppleEvent>!, _ sendMode: AESendMode, _ timeOutInTicks: Int) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The `AESendMessage` function allows you to send Apple events without linking to the entire Carbon framework, as required by `AESend(_:_:_:_:_:_:_:)`. Linking with Carbon brings in the HIToolbox framework, which requires that your application have a connection to the window server. Daemons and other applications that have no interface but wish to send and receive Apple events can use the following functions for working with Apple events at a lower level: `AESendMessage`, [`AEGetRegisteredMachPort()`](1449736-aegetregisteredmachport.md), [`AEDecodeMessage(_:_:_:)`](1447827-aedecodemessage.md), and [`AEProcessMessage(_:)`](1444387-aeprocessmessage.md). See the descriptions for those functions for more information on when you might use them.

If the target of an event sent with `AESendMessage` is the current process (as specified by using `typeProcessSerialNumber` of `{ 0, kCurrentProcess }` in the Apple event being sent), the Apple event is dispatched directly to the appropriate event handler in your process and not serialized.

##### 1819521

The `AESendMessage` function is both asynchronous and thread-safe, so you could, for example, set up a thread to send an Apple event and wait for a reply. If you use threads, you must add a `typeReplyPortAttr` attribute to your event that identifies the Mach port on which to receive the reply.

However, due to a bug that was present prior to OS X version 10.5, you could not safely dispose of a Mach port you created to use as the reply port. Disposing of the port could, rarely, lead to a crash, while failing to dispose of if leaked resources. The sample code project AESendThreadSafe shows how to safely work around the bug in earlier Mac OS versions.

## Parameters

- `event`: A pointer to the Apple event to send.
- `reply`: A pointer to a reply Apple event. On return, contains the reply Apple event from the server application, if you specified the   flag in the   parameter. If you specify the   flag in the   parameter, you receive the reply Apple event in your event queue. If you specify   flag, the reply Apple event is a null descriptor (one with descriptor type  ). If you specify   in the   parameter, and if the function returns successfully (see function result below), your application is responsible for using the   function to dispose of the descriptor returned in the   parameter.
- `sendMode`: Specifies various options for how the server application should handle the Apple event. To obtain a value for this parameter, you add together constants to set bits that specify the reply mode, the interaction level, the application switch mode, the reconnection mode, and the return receipt mode. For more information, see  .
- `timeOutInTicks`: If the reply mode specified in the   parameter is  , or if a return receipt is requested, this parameter specifies the length of time (in ticks) that the client application is willing to wait for the reply or return receipt from the server application before timing out. Most applications should use the   constant, which tells the Apple Event Manager to provide an appropriate timeout duration. If the value of this parameter is  , the Apple event never times out. These constants are described in  .

## See Also

- [func AEGetRegisteredMachPort() -> mach_port_t](1449736-aegetregisteredmachport.md)
  Returns the Mach port (in the form of a `mach_port_t`) that was registered with the bootstrap server for this process.
- [func AEDecodeMessage(UnsafeMutablePointer<mach_msg_header_t>!, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!) -> OSStatus](1447827-aedecodemessage.md)
  Decodes a Mach message and converts it into an Apple event and its related reply.
- [func AEProcessMessage(UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus](1444387-aeprocessmessage.md)
  Decodes and dispatches a low level Mach message event to an event handler, including packaging and returning the reply to the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442994-aesendmessage)*