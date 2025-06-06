# AESendMode

**Framework**: Core Services  
**Kind**: tdef

Specify send preferences to the `AESend` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AESendMode = Int32
```

#### Discussion

You use these constants with the `sendMode` parameter to the `AESend(_:_:_:_:_:_:_:)` function to specify how the server application should handle the reply mode, the interaction level, the application switch mode, the reconnection mode, the return receipt mode, the recording mode, and whether to process non-reply Apple events. To obtain a value for this parameter, you add together constants to set the appropriate bits for the Apple event you are about to send. The following paragraphs provide additional information about how you use these constants.

You can set only one flag reply preference (`kAENoReply`, `kAEQueueReply`, or `kAEWaitReply`), one user interaction preference (`kAENeverInteract`, `kAECanInteract`, or `kAEAlwaysInteract`), and one recording and execution preference (`kAEDontRecord` or `kAEDontExecute`). 

Before the Apple Event Manager sends a reply event back to the client application, the `keyAddressAttr` attribute contains the address of the client application. After the client receives the reply event, the `keyAddressAttr` attribute contains the address of the server application.

If you specify `kAEWaitReply`, the Apple Event Manager uses the Event Manager to send the event. The Apple Event Manager then calls the `WaitNextEvent` function on behalf of your application, causing your application to yield the processor and giving the server application a chance to receive and handle the Apple event. Your application continues to yield the processor until the server handles the Apple event or the request times out.

Specify the `kAEWantReceipt` flag if your application wants notification that the server application has accepted the Apple event. If you specify this flag, your application receives a return receipt as a high-level event.

If you specify the `kAEWantReceipt` flag and the server application does not accept the Apple event within the time specified by the `timeOutInTicks` parameter to `AESend`, the `AESend` function returns a timeout error. Note that `AESend` also returns a timeout error if your application sets the `kAEWaitReply` flag and does not receive the reply Apple event within the time specified by the `timeOutInTicks` parameter.

You use one of the three flags—`kAENeverInteract`, `kAECanInteract`, and `kAEAlwaysInteract`—to specify whether the server should interact with the user when handling the Apple event. Specify `kAENeverInteract` if the server should not interact with the user when handling the Apple event. You might specify this constant if you don’t want the user to be interrupted while the server is handling the Apple event.

Use the `kAECanInteract` flag if the server should interact with the user when the user needs to supply information to the server. Use the `kAEAlwaysInteract` flag if the server should interact with the user whenever the server normally asks a user to confirm a decision or interact in any other way, even if no additional information is needed from the user. Note that it is the responsibility of the server and client applications to agree on how to interpret the `kAEAlwaysInteract` flag. 

If the client application does not set any one of the user interaction flags, the Apple Event Manager sets a default, depending on the location of the target of the Apple event. If the server application is on a remote computer, the Apple Event Manager sets the `kAENeverInteract` flag as the default. If the target of the Apple event is on the local computer, the Apple Event Manager sets the `kAECanInteract` flag as the default.

The server application should call `AEInteractWithUser` if it needs to interact with the user. If both the client and the server allow user interaction, the Apple Event Manager attempts to bring the server to the foreground if it is not already the foreground process. If both the `kAECanSwitchLayer` and the `kAEWaitReply` flags are set, and if the client application is the active application on the local computer, the Apple Event Manager brings the server application directly to the front. Otherwise, the Apple Event Manager posts a notification request asking the user to bring the server application to the front, regardless of whether the `kAECanSwitchLayer` flag is set. This ensures that the user will not be interrupted by an unexpected application switch. 

Specify the `kAEDontRecord` flag if your application is sending an Apple event to itself that you don’t want to be recorded. When Apple event recording has been turned on, every event that your application sends to itself will be automatically recorded by the Apple Event Manager except those sent with the `kAEDontRecord` flag set.

Specify the `kAEDontExecute` flag if your application is sending an Apple event to itself for recording purposes only—that is, if you want the Apple Event Manager to send a copy of the event to the recording process but you do not want your application actually to receive the event.

See also [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

##### 1770279

The `kAEDontReconnect` and `kAEWantReceipt` constants are deprecated and unsupported in macOS.

## Topics

### Constants
- [var kAENoReply: Int](kaenoreply.md)
  The reply preference—your application does not want a reply Apple event. If you set the bit specified by this constant, the server processes the Apple event as soon as it has the opportunity.
- [var kAEQueueReply: Int](kaequeuereply.md)
  The reply preference—your application wants a reply Apple event. If you set the bit specified by this constant, the reply appears in your event queue as soon as the server has the opportunity to process and respond to your Apple event.
- [var kAEWaitReply: Int](kaewaitreply.md)
- [var kAEDontReconnect: Int](kaedontreconnect.md)
- [var kAEWantReceipt: Int](kaewantreceipt.md)
- [var kAENeverInteract: Int](kaeneverinteract.md)
- [var kAECanInteract: Int](kaecaninteract.md)
- [var kAEAlwaysInteract: Int](kaealwaysinteract.md)
- [var kAECanSwitchLayer: Int](kaecanswitchlayer.md)
- [var kAEDontRecord: Int](kaedontrecord.md)
- [var kAEDontExecute: Int](kaedontexecute.md)
- [var kAEProcessNonReplyEvents: Int](kaeprocessnonreplyevents.md)
  Allow processing of non-reply Apple events while awaiting a synchronous Apple event reply (you specified `kAEWaitReply` for the reply preference).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aesendmode)*