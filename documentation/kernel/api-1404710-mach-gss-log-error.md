# mach_gss_log_error

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
kern_return_t mach_gss_log_error(mach_port_t server, gssd_string mnt, uint32_t uid, gssd_string source, uint32_t major_stat, uint32_t minor_stat);
```

## See Also

- [mach_gss_accept_sec_context](1404602-mach_gss_accept_sec_context.md)
- [mach_gss_accept_sec_context_v2](1404573-mach_gss_accept_sec_context_v2.md)
- [mach_gss_hold_cred](1404537-mach_gss_hold_cred.md)
- [mach_gss_init_sec_context](1404774-mach_gss_init_sec_context.md)
- [mach_gss_init_sec_context_v2](1404594-mach_gss_init_sec_context_v2.md)
- [mach_gss_init_sec_context_v3](1642105-mach_gss_init_sec_context_v3.md)
- [mach_gss_lookup](1404794-mach_gss_lookup.md)
- [mach_gss_unhold_cred](1404585-mach_gss_unhold_cred.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1404710-mach_gss_log_error)*