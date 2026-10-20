# isConsole

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this port is a console.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var isConsole: Bool { get set }
```

```objc
@property BOOL isConsole;
```

#### Discussion

The framework may mark the console port for use as the system console. The default is `false`.

## See Also

### Configuring the port
- [var name: String?](./name.md)
  The name of the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportconfiguration/isconsole)*