# validateName(_:)

**Framework**: Virtualization  
**Kind**: method

Check if a name is a valid directory name.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func validateName(_ name: String) throws
```

#### Discussion

The name must not be empty, have characters unsafe for file systems, be longer than `NAME_MAX`, or using a reserved name such as the Unix “.” or “..” current and parent directory filenames.

## Parameters

- `name`: The name to validate.

## See Also

- [class func canonicalizedName(from: String) -> String?](vzmultipledirectoryshare/canonicalizedname(from:).md)
  Transforms a string to be a valid directory name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/validatename(_:))*