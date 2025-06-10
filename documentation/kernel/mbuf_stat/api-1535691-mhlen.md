# mhlen

**Framework**: Kernel  
**Kind**: structp

Length of data in an mbuf with a packet header.

**Availability**:
- macOS 10.6+

## Declaration

```swift
u_int32_t mhlen;
```

## See Also

- [mbufs](mbuf_stat/1535703-mbufs.md)
  Number of mbufs (free or otherwise).
- [clusters](mbuf_stat/1535704-clusters.md)
  Number of clusters (free or otherwise).
- [clfree](mbuf_stat/1535715-clfree.md)
  Number of free clusters.
- [drops](mbuf_stat/1535754-drops.md)
  Number of times allocation failed.
- [wait](mbuf_stat/1535798-wait.md)
  Number of times allocation blocked.
- [drain](mbuf_stat/1535647-drain.md)
  Number of times protocol drain functions were called.
- [mtypes](mbuf_stat/1535632-mtypes.md)
  An array of counts of each type of mbuf allocated.
- [mcfail](mbuf_stat/1535713-mcfail.md)
  Number of times m_copym failed.
- [mpfail](mbuf_stat/1535668-mpfail.md)
  Number of times m_pullup failed.
- [msize](mbuf_stat/1535673-msize.md)
  Length of an mbuf.
- [mclbytes](mbuf_stat/1535727-mclbytes.md)
  Length of an mbuf cluster.
- [minclsize](mbuf_stat/1535802-minclsize.md)
  Minimum length of data to allocate a cluster. Anything smaller than this should be placed in chained mbufs.
- [mlen](mbuf_stat/1535678-mlen.md)
  Length of data in an mbuf.
- [bigclusters](mbuf_stat/1535797-bigclusters.md)
  Number of big clusters.
- [bigclfree](mbuf_stat/1535733-bigclfree.md)
  Number of unused big clusters.
- [bigmclbytes](mbuf_stat/1535618-bigmclbytes.md)
  Length of a big mbuf cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/mbuf_stat/1535691-mhlen)*