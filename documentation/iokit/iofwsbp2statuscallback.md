# IOFWSBP2StatusCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef void (*IOFWSBP2StatusCallback)(void *refCon, IOReturn status);
```

## Parameters

- `refCon`: Reference constant supplied when the notification was registered.
- `status`: Indicates success or failure of operation.

## See Also

### Callbacks
- [IOFWSBP2FetchAgentWriteCallback](./iofwsbp2fetchagentwritecallback.md)
- [IOFWSBP2LoginCallback](./iofwsbp2logincallback.md)
- [IOFWSBP2LogoutCallback](./iofwsbp2logoutcallback.md)
- [IOFWSBP2NotifyCallback](./iofwsbp2notifycallback.md)
- [IOFWSBP2ORBAppendCallback](./iofwsbp2orbappendcallback.md)
- [IOFWSBP2ORBCompleteCallback](./iofwsbp2orbcompletecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwsbp2statuscallback)*