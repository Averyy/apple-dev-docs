# vn_getpath

**Framework**: Kernel  
**Kind**: func

Construct the path to a vnode.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vn_getpath(struct vnode *vp, char *pathbuf, int *len);
```

#### Return_value

0 for success or an error code.

#### Discussion

Paths to vnodes are not always straightforward: a file with multiple hard-links will have multiple pathnames, and it is sometimes impossible to determine a vnode's full path. vn_getpath() will not enter the filesystem.

## Parameters

- `vp`: The vnode whose path to obtain.
- `pathbuf`: Destination for pathname; should be of size MAXPATHLEN
- `len`: Destination for length of resulting path string. Result will include NULL-terminator in count--that is, "len" will be strlen(pathbuf) + 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562103-vn_getpath)*