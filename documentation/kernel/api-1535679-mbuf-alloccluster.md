# mbuf_alloccluster

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_alloccluster(mbuf_how_t how, size_t *size, char **addr);
```

#### Return_value

0 on success or ENOMEM if failure. If the caller requests greater than 4096 bytes and the system is unable to fulfill the request due to the lack of jumbo clusters support based on the configuration, this routine will return ENOTSUP. In this case, the caller is advised to use 4096 bytes or smaller during subseqent requests.

#### Discussion

Allocate a cluster that can be later attached to an mbuf by calling mbuf_attachcluster(). The allocated cluster can also be freed (without being attached to an mbuf) by calling mbuf_freecluster(). At the moment this routine will either return a cluster of 2048, 4096 or 16384 bytes depending on the requested size. Note that clusters greater than 4096 bytes might not be available in all configurations; the caller must additionally check for ENOTSUP (see below).

## Parameters

- `how`: Blocking or non-blocking.
- `size`: Pointer to size of requested cluster. Sizes up to 2048 will be rounded up to 2048; sizes greater than 2048 and up to 4096 will be rounded up to 4096. Sizes greater than 4096 will be rounded up to 16384.
- `addr`: Pointer to the address of the requested cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535679-mbuf_alloccluster)*