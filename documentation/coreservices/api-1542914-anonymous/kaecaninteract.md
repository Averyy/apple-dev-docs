# kAECanInteract

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kAECanInteract = 0x00000020
```

#### Discussion

The user interaction preference—the server application can interact with the user in response to the Apple event. By convention, you set the bit specified by this constant if the user needs to supply information to the server. If you set the bit and the server allows interaction, the `AEInteractWithUser` function either brings the server application to the foreground or posts a notification request. When you send an Apple event to a local application, the default is to set this bit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542914-anonymous/kaecaninteract)*