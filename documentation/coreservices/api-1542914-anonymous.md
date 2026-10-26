# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kAEAlwaysInteract](./api-1542914-anonymous/kaealwaysinteract.md)
- [kAECanInteract](./api-1542914-anonymous/kaecaninteract.md)
- [kAECanSwitchLayer](./api-1542914-anonymous/kaecanswitchlayer.md)
- [kAEDoNotAutomaticallyAddAnnotationsToEvent](./api-1542914-anonymous/kaedonotautomaticallyaddannotationstoevent.md)
- [kAEDontExecute](./api-1542914-anonymous/kaedontexecute.md)
- [kAEDontReconnect](./api-1542914-anonymous/kaedontreconnect.md)
- [kAEDontRecord](./api-1542914-anonymous/kaedontrecord.md)
- [kAENeverInteract](./api-1542914-anonymous/kaeneverinteract.md)
- [kAENoReply](./api-1542914-anonymous/kaenoreply.md)
  The reply preference—your application does not want a reply Apple event. If you set the bit specified by this constant, the server processes the Apple event as soon as it has the opportunity.
- [kAEProcessNonReplyEvents](./api-1542914-anonymous/kaeprocessnonreplyevents.md)
  Allow processing of non-reply Apple events while awaiting a synchronous Apple event reply (you specified `kAEWaitReply` for the reply preference).
- [kAEQueueReply](./api-1542914-anonymous/kaequeuereply.md)
  The reply preference—your application wants a reply Apple event. If you set the bit specified by this constant, the reply appears in your event queue as soon as the server has the opportunity to process and respond to your Apple event.
- [kAEWaitReply](./api-1542914-anonymous/kaewaitreply.md)
- [kAEWantReceipt](./api-1542914-anonymous/kaewantreceipt.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542914-anonymous)*