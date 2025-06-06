# mbuf_allocpacket_list

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_allocpacket_list(unsigned int numpkts, mbuf_how_t how, size_t packetlen, unsigned int *maxchunks, mbuf_t *mbuf);
```

#### Return_value

Returns 0 upon success or the following error code: EINVAL - Invalid parameter ENOMEM - Not enough memory available ENOBUFS - Buffers not big enough for the maximum number of chunks requested

#### Discussion

Allocate a linked list of packets. According to the requested length, each packet will made of a chain of one or more mbufs. The mbuf type will be set to MBUF_TYPE_DATA. The caller may specify the maximum number of element for each mbuf chain making up a packet.

## Parameters

- `numpkts`: Number of packets to allocate
- `how`: Blocking or non-blocking
- `packetlen`: The total length of the packet mbuf to be allocated. The length must be greater than zero.
- `maxchunks`: An input/output pointer to the maximum number of mbufs segments making up the chain. On input, if maxchunks is zero, or the value pointed to by maxchunks is zero, the packet will be made of as few or as many buffer segments as necessary to fit the length. The allocation will fail with ENOBUFS if the number of segments requested is too small and the sum of the maximum size of each individual segment is less than the packet length. On output, if the allocation succeed and maxchunks is non zero, it will point to the actual number of segments allocated. Additional notes for packetlen greater than 4096 bytes: the caller may pass a non-NULL maxchunks and initialize it with zero such that upon success, it can find out whether or not the system configuration allows for larger than 4096 bytes cluster allocations, by checking on the value pointed to by maxchunks. E.g. a request for 9018 bytes may result in 1 chunk when jumbo clusters are available, or 3 chunks otherwise.
- `Upon`: success, *mbuf will be a reference to the new mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535681-mbuf_allocpacket_list)*