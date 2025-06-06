# mbuf_mclhasreference

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
int mbuf_mclhasreference(mbuf_t mbuf);
```

#### Return_value

0 if there is no reference by another mbuf, 1 otherwise.

#### Discussion

Check if a cluster of an mbuf is referenced by another mbuf. References may be taken, for example, as a result of a call to mbuf_split or mbuf_copym

## Parameters

- `mbuf`: The mbuf with the cluster to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535799-mbuf_mclhasreference)*