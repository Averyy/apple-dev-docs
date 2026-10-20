# mach_gss_accept_sec_context_v2

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.7+

## Declaration

```c
kern_return_t mach_gss_accept_sec_context_v2(mach_port_t server, gssd_byte_buffer intoken, mach_msg_type_number_t intokenCnt, gssd_nametype svc_nt, gssd_byte_buffer svc_princ, mach_msg_type_number_t svc_princCnt, uint32_t *gssd_flags, gssd_ctx *context, gssd_cred *cred_handle, uint32_t *flags, uint32_t *uid, gssd_gid_list gids, mach_msg_type_number_t *gidsCnt, gssd_byte_buffer *key, mach_msg_type_number_t *keyCnt, gssd_byte_buffer *outtoken, mach_msg_type_number_t *outtokenCnt, uint32_t *major_stat, uint32_t *minor_stat);
```

## See Also

### Security
- [mach_gss_accept_sec_context](./api-1404602-mach_gss_accept_sec_context.md)
- [mach_gss_hold_cred](./api-1404537-mach_gss_hold_cred.md)
- [mach_gss_init_sec_context](./api-1404774-mach_gss_init_sec_context.md)
- [mach_gss_init_sec_context_v2](./api-1404594-mach_gss_init_sec_context_v2.md)
- [mach_gss_init_sec_context_v3](./api-1642105-mach_gss_init_sec_context_v3.md)
- [mach_gss_log_error](./api-1404710-mach_gss_log_error.md)
- [mach_gss_lookup](./api-1404794-mach_gss_lookup.md)
- [mach_gss_unhold_cred](./api-1404585-mach_gss_unhold_cred.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1404573-mach_gss_accept_sec_context_v2)*