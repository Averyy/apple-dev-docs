# ctl_recvsize

**Framework**: Kernel  
**Kind**: structp

Override the default receive size. If set to zero, the default receive size will be used, and this default value is set to this field to be retrieved by the caller.

**Availability**:
- macOS 10.13+

## Declaration

```swift
u_int32_t ctl_recvsize;
```

## See Also

- [ctl_name](kern_ctl_reg/1809212-ctl_name.md)
  A Bundle ID string of up to MAX_KCTL_NAME bytes (including the ending zero). This string should not be empty.
- [ctl_id](kern_ctl_reg/1809214-ctl_id.md)
  The control ID may be dynamically assigned or it can be a 32-bit creator code assigned by DTS. For a DTS assigned creator code the CTL_FLAG_REG_ID_UNIT flag must be set. For a dynamically assigned control ID, do not set the CTL_FLAG_REG_ID_UNIT flag. The value of the dynamically assigned control ID is set to this field when the registration succeeds.
- [ctl_unit](kern_ctl_reg/1809215-ctl_unit.md)
  A separate unit number to register multiple units that share the same control ID with DTS assigned creator code when the CTL_FLAG_REG_ID_UNIT flag is set. This field is ignored for a dynamically assigned control ID.
- [ctl_flags](kern_ctl_reg/1809219-ctl_flags.md)
  CTL_FLAG_PRIVILEGED and/or CTL_FLAG_REG_ID_UNIT.
- [ctl_sendsize](kern_ctl_reg/1809220-ctl_sendsize.md)
  Override the default send size. If set to zero, the default send size will be used, and this default value is set to this field to be retrieved by the caller.
- [ctl_connect](kern_ctl_reg/1809225-ctl_connect.md)
  Specify the function to be called whenever a client connects to the kernel control. This field must be specified.
- [ctl_disconnect](kern_ctl_reg/1809228-ctl_disconnect.md)
  Specify a function to be called whenever a client disconnects from the kernel control.
- [ctl_send](kern_ctl_reg/1809230-ctl_send.md)
  Specify a function to handle data send from the client to the kernel control.
- [ctl_setopt](kern_ctl_reg/1809233-ctl_setopt.md)
  Specify a function to handle set socket option operations for the kernel control.
- [ctl_getopt](kern_ctl_reg/1809236-ctl_getopt.md)
  Specify a function to handle get socket option operations for the kernel control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kern_ctl_reg/1809224-ctl_recvsize)*