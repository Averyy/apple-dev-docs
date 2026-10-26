# Volume Mount Options

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify how an alias should be resolved.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kResolveAliasFileNoUI](./api-1444436-volume_mount_options/kresolvealiasfilenoui.md)
  The Alias Manager should resolve the alias without presenting a user interface.
- [kResolveAliasTryFileIDFirst](./api-1444436-volume_mount_options/kresolvealiastryfileidfirst.md)
  The Alias Manager should search for the alias target using file IDs before searching using the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444436-volume_mount_options)*