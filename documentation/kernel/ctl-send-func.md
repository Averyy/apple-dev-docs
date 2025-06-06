# ctl_send_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef errno_t (*ctl_send_func)(kern_ctl_ref kctlref, u_int32_t unit, void *unitinfo, mbuf_t m, int flags);
```

#### Discussion

The ctl_send_func is used to receive data sent from the client to the kernel control.

## Parameters

- `kctlref`: The control ref of the kernel control.
- `unit`: The unit number of the kernel control instance the client has connected to.
- `unitinfo`: The user-defined private data initialized by the ctl_connect_func callback.
- `m`: The data sent by the client to the kernel control in an mbuf chain. Your function is responsible for releasing the mbuf chain.
- `flags`: The flags specified by the client when calling send/sendto/sendmsg (MSG_OOB/MSG_DONTROUTE).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ctl_send_func)*