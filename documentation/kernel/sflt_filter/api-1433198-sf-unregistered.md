# sf_unregistered

**Framework**: Kernel  
**Kind**: structp

Your function for being notified when your filter has been unregistered.

**Availability**:
- macOS 10.6+

## Declaration

```swift
sf_unregistered_func sf_unregistered;
```

## See Also

- [sf_handle](sflt_filter/1433190-sf_handle.md)
  A value used to find socket filters by applications. An application can use this value to specify that this filter should be attached when using the SO_NKE socket option.
- [sf_flags](sflt_filter/1433199-sf_flags.md)
  Indicate whether this filter should be attached to all new sockets or just those that request the filter be attached using the SO_NKE socket option. If this filter utilizes the socket filter extension fields, it must also set SFLT_EXTENDED.
- [sf_name](sflt_filter/1433212-sf_name.md)
  A name used for debug purposes.
- [sf_attach](sflt_filter/1433170-sf_attach.md)
  Your function for handling attaches to sockets.
- [sf_detach](sflt_filter/1433233-sf_detach.md)
  Your function for handling detaches from sockets.
- [sf_notify](sflt_filter/1433204-sf_notify.md)
  Your function for handling events. May be null.
- [sf_data_in](sflt_filter/1433174-sf_data_in.md)
  Your function for handling incoming data. May be null.
- [sf_data_out](sflt_filter/1433165-sf_data_out.md)
  Your function for handling outgoing data. May be null.
- [sf_connect_in](sflt_filter/1433268-sf_connect_in.md)
  Your function for handling inbound connections. May be null.
- [sf_connect_out](sflt_filter/1433264-sf_connect_out.md)
  Your function for handling outbound connections. May be null.
- [sf_bind](sflt_filter/1433208-sf_bind.md)
  Your function for handling binds. May be null.
- [sf_setoption](sflt_filter/1433206-sf_setoption.md)
  Your function for handling setsockopt. May be null.
- [sf_getoption](sflt_filter/1433191-sf_getoption.md)
  Your function for handling getsockopt. May be null.
- [sf_listen](sflt_filter/1433202-sf_listen.md)
  Your function for handling listen. May be null.
- [sf_ioctl](sflt_filter/1433284-sf_ioctl.md)
  Your function for handling ioctls. May be null.
- [sf_len](sflt_filter/1809366-sf_len.md)
  Length of socket filter extension structure; developers must initialize this to sizeof sflt_filter_ext structure. This field and all fields following it will only be valid if SFLT_EXTENDED flag is set in sf_flags field.
- [sf_ext_accept](sflt_filter/1809374-sf_ext_accept.md)
  Your function for handling inbound connections at accept time. May be null.
- [sf_ext_rsvd](sflt_filter/1809385-sf_ext_rsvd.md)
  Reserved for future use; you must initialize the reserved fields with zeroes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sflt_filter/1433198-sf_unregistered)*