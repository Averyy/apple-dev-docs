# mach_gss_lookup

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.8+

## Declaration

```c
kern_return_t mach_gss_lookup(mach_port_t server, uint32_t uid, int32_t asid, mach_port_t *gssd_session_port);
```

## See Also

### Security
- [mach_gss_accept_sec_context](./api-1404602-mach_gss_accept_sec_context.md)
- [mach_gss_accept_sec_context_v2](./api-1404573-mach_gss_accept_sec_context_v2.md)
- [mach_gss_hold_cred](./api-1404537-mach_gss_hold_cred.md)
- [mach_gss_init_sec_context](./api-1404774-mach_gss_init_sec_context.md)
- [mach_gss_init_sec_context_v2](./api-1404594-mach_gss_init_sec_context_v2.md)
- [mach_gss_init_sec_context_v3](./api-1642105-mach_gss_init_sec_context_v3.md)
- [mach_gss_log_error](./api-1404710-mach_gss_log_error.md)
- [mach_gss_unhold_cred](./api-1404585-mach_gss_unhold_cred.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1404794-mach_gss_lookup)*