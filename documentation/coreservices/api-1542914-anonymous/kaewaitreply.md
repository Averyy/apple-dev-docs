# kAEWaitReply

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kAEWaitReply = 0x00000003
```

#### Discussion

The reply preference—your application wants a reply Apple event and is willing to give up the processor while waiting for the reply. For example, if the server application is on the same computer as your application, your application yields the processor to allow the server to respond to your Apple event.

If you set the bit specified by this constant, you must provide an idle function. This function should process any update events, null events, operating-system events, or activate events that occur while your application is waiting for a reply. For more information on idle routines, see `AEInteractWithUser`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542914-anonymous/kaewaitreply)*