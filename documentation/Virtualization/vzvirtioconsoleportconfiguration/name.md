# name

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The name of the port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

## Discussion

The default behavior is to not use a name unless set.

## See Also

### Configuring the port
- [var isConsole: Bool](./isconsole.md)
  A Boolean value that indicates whether this port is a console.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportconfiguration/name)*