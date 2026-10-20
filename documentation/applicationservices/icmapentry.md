# ICMapEntry

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct ICMapEntry
```

```c
typedef struct ICMapEntry {
    ...
} ICMapEntry;
```

## Topics

### Initializers
- [init()](./icmapentry/api-1462224-init.md)
- [init(totalLength: Int16, fixedLength: ICFixedLength, version: Int16, fileType: OSType, fileCreator: OSType, postCreator: OSType, flags: ICMapEntryFlags, extension: Str255, creatorAppName: Str255, postAppName: Str255, MIMEType: Str255, entryName: Str255)](./icmapentry/api-1463249-init.md)
### Instance Properties
- [var MIMEType: Str255](./icmapentry/api-1462908-mimetype.md)
- [var creatorAppName: Str255](./icmapentry/api-1463557-creatorappname.md)
- [var entryName: Str255](./icmapentry/api-1463382-entryname.md)
- [var `extension`: Str255](./icmapentry/api-1459990-extension.md)
- [var fileCreator: OSType](./icmapentry/api-1461576-filecreator.md)
- [var fileType: OSType](./icmapentry/api-1459150-filetype.md)
- [var fixedLength: ICFixedLength](./icmapentry/api-1461563-fixedlength.md)
- [var flags: ICMapEntryFlags](./icmapentry/api-1461969-flags.md)
- [var postAppName: Str255](./icmapentry/api-1464312-postappname.md)
- [var postCreator: OSType](./icmapentry/api-1460179-postcreator.md)
- [var totalLength: Int16](./icmapentry/api-1464080-totallength.md)
- [var version: Int16](./icmapentry/api-1462319-version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/icmapentry)*