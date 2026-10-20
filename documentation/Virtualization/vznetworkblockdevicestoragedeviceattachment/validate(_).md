# validate(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Type Method

Checks if the URL is a valid network block device URL.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class func validate(_ URL: URL) throws
```

```objc
+ (BOOL) validateURL:(NSURL *) URL error:(NSError **) error;
```

#### Discussion

This method checks that the URL is well-formed; however, it doesn’t attempt to access the URL. See the [NBD URL specification](https://github.com/NetworkBlockDevice/nbd/blob/master/doc/uri.md) on GitHub for more detailed descriptions of valid URIs.

## Parameters

- `URL`: The NBD URL to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/validate(_:))*