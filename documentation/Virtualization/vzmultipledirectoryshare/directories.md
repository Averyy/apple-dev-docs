# directories

**Framework**: Virtualization  
**Kind**: property

The directories on the host to expose to the guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var directories: [String : VZSharedDirectory] { get }
```

#### Discussion

The dictionary string keys are the names for the directory. The keys must be valid names or the system raises an exception.

## See Also

- [class func validateName(String) throws](vzmultipledirectoryshare/validatename(_:).md)
  Check if a name is a valid directory name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/directories)*