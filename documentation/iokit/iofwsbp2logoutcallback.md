# IOFWSBP2LogoutCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef void (*IOFWSBP2LogoutCallback)(void *refCon, FWSBP2LogoutCompleteParams *params);
```

## Parameters

- `refCon`: Reference constant supplied when the notification was registered.
- `params`: Structure containing additional information about the status of the logout.

## See Also

### Callbacks
- [IOFWSBP2FetchAgentWriteCallback](./iofwsbp2fetchagentwritecallback.md)
- [IOFWSBP2LoginCallback](./iofwsbp2logincallback.md)
- [IOFWSBP2NotifyCallback](./iofwsbp2notifycallback.md)
- [IOFWSBP2ORBAppendCallback](./iofwsbp2orbappendcallback.md)
- [IOFWSBP2ORBCompleteCallback](./iofwsbp2orbcompletecallback.md)
- [IOFWSBP2StatusCallback](./iofwsbp2statuscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwsbp2logoutcallback)*