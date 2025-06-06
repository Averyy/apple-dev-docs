# vfs_clearauthcache_ttl

**Framework**: Kernel  
**Kind**: func

Remove time-to-live controls for cached credentials on a filesytem. Filesystems with remote authorization decisions (opaque) will still have KAUTH_VNODE_SEARCH rights cached for a default of CACHED_LOOKUP_RIGHT_TTL seconds.

**Availability**:
- macOS 10.5+

## Declaration

```swift
void vfs_clearauthcache_ttl(mount_t mp);
```

#### Return_value

void.

## Parameters

- `mp`: Mount for which to clear cache lifetime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523469-vfs_clearauthcache_ttl)*