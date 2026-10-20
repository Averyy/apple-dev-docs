# systemVersion

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The version of the operating system.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var systemVersion: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * systemVersion;
```

#### Discussion

This property contains the numerical version number of the system. For example, the value is `2.0` for the initial release of watchOS 2.

## See Also

### Reading System Information
- [var systemName: String](./systemname.md)
  The name of the operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/systemversion)*