# bpfattach

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
void bpfattach(ifnet_t interface, u_int data_link_type, u_int header_length);
```

#### Discussion

Registers an interface with BPF. This allows bpf devices to attach to your interface to capture packets. Your interface will be unregistered automatically when your interface is detached.

## Parameters

- `interface`: The interface to register with BPF.
- `data_link_type`: The data link type of the interface. See the DLT_* defines in bpf.h.
- `header_length`: The length, in bytes, of the data link header.

## See Also

### bpf
- [bpf_attach](./api-1589700-bpf_attach.md)
- [bpf_tap_in](./api-1589470-bpf_tap_in.md)
- [bpf_tap_out](./api-1589576-bpf_tap_out.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1589467-bpfattach)*