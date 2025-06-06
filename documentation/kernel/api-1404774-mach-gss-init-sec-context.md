# mach_gss_init_sec_context

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
kern_return_t mach_gss_init_sec_context(mach_port_t server, gssd_mechtype mech, gssd_byte_buffer intoken, mach_msg_type_number_t intokenCnt, uint32_t uid, gssd_string princ_namestr, gssd_string svc_namestr, uint32_t flags, uint32_t gssd_flags, gssd_ctx *context, gssd_cred *cred_handle, uint32_t *ret_flags, gssd_byte_buffer *key, mach_msg_type_number_t *keyCnt, gssd_byte_buffer *outtoken, mach_msg_type_number_t *outtokenCnt, uint32_t *major_stat, uint32_t *minor_stat);
```

## See Also

- [mach_gss_accept_sec_context](1404602-mach_gss_accept_sec_context.md)
- [mach_gss_accept_sec_context_v2](1404573-mach_gss_accept_sec_context_v2.md)
- [mach_gss_hold_cred](1404537-mach_gss_hold_cred.md)
- [mach_gss_init_sec_context_v2](1404594-mach_gss_init_sec_context_v2.md)
- [mach_gss_init_sec_context_v3](1642105-mach_gss_init_sec_context_v3.md)
- [mach_gss_log_error](1404710-mach_gss_log_error.md)
- [mach_gss_lookup](1404794-mach_gss_lookup.md)
- [mach_gss_unhold_cred](1404585-mach_gss_unhold_cred.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1404774-mach_gss_init_sec_context)*