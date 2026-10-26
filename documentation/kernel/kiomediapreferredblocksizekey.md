# kIOMediaPreferredBlockSizeKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IOMedia objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOMediaPreferredBlockSizeKey
```

#### Discussion

The kIOMediaPreferredBlockSizeKey property has an OSNumber value and describes the media's natural block size in bytes. This information is useful to clients that want to optimize access to the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiomediapreferredblocksizekey)*