# canonicalizedName(from:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Type Method

Transforms a string to be a valid directory name.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func canonicalizedName(from name: String) -> String?
```

```objc
+ (NSString *) canonicalizedNameFromName:(NSString *) name;
```

## Return Value

Returns a String with the canonicalized name, or `nil` if there was an error.

## Parameters

- `name`: The name to transform.

## See Also

### Directory name utility methods
- [class func validateName(String) throws](./validatename%28_%29.md)
  Check if a name is a valid directory name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/canonicalizedname(from:))*