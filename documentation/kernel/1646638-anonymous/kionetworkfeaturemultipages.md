# kIONetworkFeatureMultiPages

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIONetworkFeatureMultiPages = 0x008
```

#### Discussion

Set this bit if the driver is capable of handling packets coming down from the network stack that reside in virtually, but not in physically contiguous span of the external mbuf clusters. In this case, the data area of a packet in the external mbuf cluster might cross one or more physical pages that are disjoint, depending on the interface MTU and the packet size. Such a use of larger than system page size clusters by the network stack is done for better system efficiency. Drivers that utilize the IOMbufNaturalMemoryCursor with the getPhysicalSegmentsWithCoalesce interfaces and enumerate the list of vectors should set this flag for possible gain in performance during bulk data transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturemultipages)*