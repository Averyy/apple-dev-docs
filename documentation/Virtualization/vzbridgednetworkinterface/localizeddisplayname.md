# localizedDisplayName

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A user-visible name for the network interface.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var localizedDisplayName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * localizedDisplayName;
```

#### Discussion

An example interface name is `Ethernet`. Use this string when you need to display the name of the interface to the user.

## See Also

### Getting the interface description
- [var identifier: String](./identifier.md)
  The unique BSD name of this network interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbridgednetworkinterface/localizeddisplayname)*