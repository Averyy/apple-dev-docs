# HVGLPartLoader

**Framework**: hvf  
**Kind**: class

Special loader object for an HVGL table in memory, which must be Double-aligned Typically this is from a memory-mapped font

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class HVGLPartLoader
```

## Topics

### Initializers
- [init?(hvglTable: UnsafeRawBufferPointer, hvpmTable: UnsafeRawBufferPointer?)](hvglpartloader/init(hvgltable:hvpmtable:).md)
  Returns nil if the data is malformed or missing
### Instance Properties
- [var glyphCount: Int](hvglpartloader/glyphcount.md)
  The number of glyphs (externally visible parts) in the hvgl table
- [var partCount: Int](hvglpartloader/partcount.md)
  The number of parts (all parts) in the hvgl table
- [var tableVersion: (major: Int, minor: Int)](hvglpartloader/tableversion.md)
  The version of the hvgl table this loader supports


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvglpartloader)*