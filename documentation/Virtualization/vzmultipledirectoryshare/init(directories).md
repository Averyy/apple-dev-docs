# init(directories:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates the directory share with a set of directories on the host.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(directories: [String : VZSharedDirectory])
```

```objc
- (instancetype) initWithDirectories:(NSDictionary<NSString *,VZSharedDirectory *> *) directories;
```

#### Discussion

The dictionary string keys are the names for the directory. The keys must be valid names or the system raises an exception and the app exits.

## Parameters

- `directories`: Directories on the host to expose to the guest VM by name.

## See Also

### Related Documentation
- [class func validateName(String) throws](./validatename%28_%29.md)
  Check if a name is a valid directory name.
### Creating a directory share
- [convenience init()](./init%28%29.md)
  Initializes the directory share with an empty set of directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/init(directories:))*