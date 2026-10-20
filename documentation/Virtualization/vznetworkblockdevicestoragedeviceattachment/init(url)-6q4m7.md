# init(url:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a new network block device (NBD) storage attachment from an NDB Uniform Resource Indicator (URI) represented as a URL that you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
convenience init(url URL: URL) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) URL error:(NSError **) error;
```

## Parameters

- `URL`: The NBD’s URI represented as a URL.

## See Also

### Creating network block device attachments
- [init(url: URL, timeout: TimeInterval, isForcedReadOnly: Bool, synchronizationMode: VZDiskSynchronizationMode) throws](./init%28url,timeout,isforcedreadonly,synchronizationmode%29.md)
  Creates a new network block device storage attachment from an NBD Uniform Resource Indicator (URI) represented as a URL, timeout value, and read-only and synchronization modes that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/init(url:)-6q4m7)*