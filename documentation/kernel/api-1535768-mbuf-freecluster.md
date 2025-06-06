# mbuf_freecluster

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_freecluster(caddr_t addr, size_t size);
```

#### Discussion

Free a cluster that was previously allocated by a call to mbuf_alloccluster(). The caller must pass the actual size of the cluster as returned by mbuf_alloccluster(), which at this point must be either 2048, 4096 or 16384 bytes.

## Parameters

- `addr`: The address of the cluster.
- `size`: The actual size of the cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535768-mbuf_freecluster)*