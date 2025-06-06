# vfs_iterate

**Framework**: Kernel  
**Kind**: func

Iterate over all mountpoints with a callback. Used, for example, by sync().

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_iterate(int flags, int (*callout)(struct mount *, void *), void *arg);
```

#### Return_value

0 for success, else an error code.

## Parameters

- `flags`: Unused.
- `callback`: Function which takes a mount and arbitrary passed-in "arg," and returns one of VFS_RETURNED_DONE or VFS_CLAIMED_DONE: end iteration and return success. VFS_RETURNED or VFS_CLAIMED: continue iterating. Anything else: continue iterating.
- `arg`: Arbitrary data to pass to callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523233-vfs_iterate)*