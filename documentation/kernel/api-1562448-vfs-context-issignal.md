# vfs_context_issignal

**Framework**: Kernel  
**Kind**: func

Get a bitfield of pending signals for the BSD process associated with a vfs_context_t.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_context_issignal(vfs_context_t ctx, sigset_t mask);
```

#### Return_value

Bitfield of pending signals.

#### Discussion

The bitfield is constructed using the sigmask() macro, in the sense of bits |= sigmask(SIGSEGV).

## Parameters

- `ctx`: Context whose associated process to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562448-vfs_context_issignal)*