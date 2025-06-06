# vfs_authcache_ttl

**Framework**: Kernel  
**Kind**: func

Determine the time-to-live of cached authorized credentials for files in this filesystem.

**Availability**:
- macOS 10.5+

## Declaration

```swift
int vfs_authcache_ttl(mount_t mp);
```

#### Return_value

Cache lifetime in seconds. CACHED_RIGHT_INFINITE_TTL indicates that credentials never expire.

#### Discussion

If a filesystem is set to allow caching credentials, the VFS layer can authorize previously-authorized actions from the same vfs_context_t without calling down to the filesystem (though it will not deny based on the cache).

## Parameters

- `mp`: Mount for which to check cache lifetime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523180-vfs_authcache_ttl)*