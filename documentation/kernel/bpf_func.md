# BPF_FUNC

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.6+

## Declaration

```c
typedef int (*BPF_FUNC)(struct ifnet *, struct mbuf *);
```

#### Discussion

Prototype for the BPF tap handler. This will disappear when the correct DLIL header file is included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/bpf_func)*