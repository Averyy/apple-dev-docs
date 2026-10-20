# bigmclbytes

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

Length of a big mbuf cluster.

**Availability**:
- macOS 10.6+

## Declaration

```c
u_int32_t bigmclbytes;
```

## See Also

### Fields
- [mbufs](./api-1535703-mbufs.md)
  Number of mbufs (free or otherwise).
- [clusters](./api-1535704-clusters.md)
  Number of clusters (free or otherwise).
- [clfree](./api-1535715-clfree.md)
  Number of free clusters.
- [drops](./api-1535754-drops.md)
  Number of times allocation failed.
- [wait](./api-1535798-wait.md)
  Number of times allocation blocked.
- [drain](./api-1535647-drain.md)
  Number of times protocol drain functions were called.
- [mtypes](./api-1535632-mtypes.md)
  An array of counts of each type of mbuf allocated.
- [mcfail](./api-1535713-mcfail.md)
  Number of times m_copym failed.
- [mpfail](./api-1535668-mpfail.md)
  Number of times m_pullup failed.
- [msize](./api-1535673-msize.md)
  Length of an mbuf.
- [mclbytes](./api-1535727-mclbytes.md)
  Length of an mbuf cluster.
- [minclsize](./api-1535802-minclsize.md)
  Minimum length of data to allocate a cluster. Anything smaller than this should be placed in chained mbufs.
- [mlen](./api-1535678-mlen.md)
  Length of data in an mbuf.
- [mhlen](./api-1535691-mhlen.md)
  Length of data in an mbuf with a packet header.
- [bigclusters](./api-1535797-bigclusters.md)
  Number of big clusters.
- [bigclfree](./api-1535733-bigclfree.md)
  Number of unused big clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/mbuf_stat/1535618-bigmclbytes)*