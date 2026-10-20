# identifier

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The unique BSD name of this network interface.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (copy, readonly) NSString * identifier;
```

#### Discussion

BSD names for the host computer’s Ethernet interfaces include `en0`, `en1`, and so on.

## See Also

### Getting the interface description
- [var localizedDisplayName: String?](./localizeddisplayname.md)
  A user-visible name for the network interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbridgednetworkinterface/identifier)*