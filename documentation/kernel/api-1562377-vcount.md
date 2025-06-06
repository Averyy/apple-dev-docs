# vcount

**Framework**: Kernel  
**Kind**: func

Count total references to a given file, disregarding "kusecount" (event listener, as with O_EVTONLY) references.

**Availability**:
- macOS 10.5+

## Declaration

```swift
int vcount(vnode_t vp);
```

#### Return_value

Count of references.

#### Discussion

For a regular file, just return (usecount-kusecount); for device files, return the sum over all vnodes 'v' which reference that device of (usecount(v) - kusecount(v)). Note that this is merely a snapshot and could be invalid by the time the caller checks the result.

## Parameters

- `vp`: The vnode whose references to count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562377-vcount)*