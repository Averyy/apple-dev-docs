# mbuf_freem_list

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
int mbuf_freem_list(mbuf_t mbuf);
```

#### Return_value

The number of mbufs freed.

#### Discussion

Frees linked list of mbuf chains. Walks through mnextpackt and does the equivalent of mbuf_freem to each.

## Parameters

- `mbuf`: The first mbuf in the linked list to free.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535787-mbuf_freem_list)*