# init(directories:)

**Framework**: Virtualization  
**Kind**: init

Creates the directory share with a set of directories on the host.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(directories: [String : VZSharedDirectory])
```

#### Discussion

The dictionary string keys are the names for the directory. The keys must be valid names or the system raises an exception and the app exits.

## Parameters

- `directories`: Directories on the host to expose to the guest VM by name.

## See Also

- [class func validateName(String) throws](vzmultipledirectoryshare/validatename(_:).md)
  Check if a name is a valid directory name.
- [convenience init()](vzmultipledirectoryshare/init.md)
  Initializes the directory share with an empty set of directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/init(directories:))*