# canonicalizedName(from:)

**Framework**: Virtualization  
**Kind**: method

Transforms a string to be a valid directory name.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func canonicalizedName(from name: String) -> String?
```

#### Return Value

Returns a String with the canonicalized name, or `nil` if there was an error.

## Parameters

- `name`: The name to transform.

## See Also

- [class func validateName(String) throws](vzmultipledirectoryshare/validatename(_:).md)
  Check if a name is a valid directory name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/canonicalizedname(from:))*