# init(tag:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a configuration for a VIRTIO file system device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(tag: String)
```

```objc
- (instancetype) initWithTag:(NSString *) tag;
```

## Discussion

The system presents the `tag` as a label in the guest identifying this device for mounting. The `tag` must be valid, which you can check with [`validateTag(_:)`](./validatetag%28_%29.md).

## Parameters

- `tag`: The label identifying this device in the guest.

## See Also

### Related Documentation
- [class func validateTag(String) throws](./validatetag%28_%29.md)
  Checks to see whether a Virtio tag is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofilesystemdeviceconfiguration/init(tag:))*