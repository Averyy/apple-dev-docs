# init(url:readOnly:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initialize with a host directory.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(url: URL, readOnly: Bool)
```

```objc
- (instancetype) initWithURL:(NSURL *) url readOnly:(BOOL) readOnly;
```

## Discussion

## Parameters

- `url`: A local file URL to expose to the guest.
- `readOnly`: A Boolean value that indicates whether to expose the directory as read-only to the guest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzshareddirectory/init(url:readonly:)-8j5z)*