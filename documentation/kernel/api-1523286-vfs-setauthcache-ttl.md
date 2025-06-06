# vfs_setauthcache_ttl

**Framework**: Kernel  
**Kind**: func

Enable credential caching and set time-to-live of cached authorized credentials for files in this filesystem.

**Availability**:
- macOS 10.5+

## Declaration

```swift
void vfs_setauthcache_ttl(mount_t mp, int ttl);
```

#### Return_value

void.

#### Discussion

If a filesystem is set to allow caching credentials, the VFS layer can authorize previously-authorized actions from the same vfs_context_t without calling down to the filesystem (though it will not deny based on the cache).

## Parameters

- `mp`: Mount for which to set cache lifetime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523286-vfs_setauthcache_ttl)*