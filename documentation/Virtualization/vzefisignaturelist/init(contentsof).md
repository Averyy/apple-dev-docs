# init(contentsOf:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a signature list from a file.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(contentsOf url: URL) throws
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

## Parameters

- `url`: The URL to a file containing signature data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturelist/init(contentsof:))*