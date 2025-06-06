# mbuf_data_to_physical

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
addr64_t mbuf_data_to_physical(void *ptr);
```

#### Return_value

The 64 bit physical address of the mbuf data or NULL if ptr does not point to data stored in an mbuf.

#### Discussion

mbuf_data_to_physical is a replacement for mcl_to_paddr. Given a pointer returned from mbuf_data of mbuf_datastart, mbuf_data_to_physical will return the phyical address for that block of data. Note that even though the data is in virtually contiguous span, the underlying physical pages might not be physically contiguous. Because of this, callers must ensure to call this routine for each page boundary. Device drivers that deal with DMA are strongly encouraged to utilize the IOMbufNaturalMemoryCursor and walk down the list of vectors instead of using this interface to obtain the physical address. Use of this routine is therefore discouraged.

## Parameters

- `ptr`: A pointer to data stored in an mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535757-mbuf_data_to_physical)*