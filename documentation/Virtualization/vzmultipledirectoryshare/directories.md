# directories

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The directories on the host to expose to the guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var directories: [String : VZSharedDirectory] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,VZSharedDirectory *> * directories;
```

## Discussion

The dictionary string keys are the names for the directory. The keys must be valid names or the system raises an exception.

## See Also

### Related Documentation
- [class func validateName(String) throws](./validatename%28_%29.md)
  Check if a name is a valid directory name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare/directories)*