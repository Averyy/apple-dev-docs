# disabled

**Framework**: os  
**Kind**: property  
**Role**: Type Property

A shared signposter that doesn’t emit signposts at runtime.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
static var disabled: OSSignposter { get }
```

#### Discussion

You can use the signposter this property returns to disable signposts in your production builds without having to refactor your code, as the following example demonstrates:

```swift
let signposter: OSSignposter
#if DEBUG
signposter = OSSignposter()
#else
signposter = OSSignposter.disabled
#endif
```

To determine if a signposter can emit signposts, use the [`isEnabled`](./isenabled.md) property.

## See Also

### Creating a Signposter
- [init()](./init%28%29.md)
  Creates a signposter that uses the default subsystem.
- [init(subsystem: String, category: String)](./init%28subsystem,category%29-94xpb.md)
  Creates a signposter that uses the specified subsystem and category.
- [init(subsystem: String, category: OSLog.Category)](./init%28subsystem,category%29-4vdri.md)
  Creates a signposter that uses the specified subsystem and system-defined log category.
- [init(logger: Logger)](./init%28logger%29.md)
  Creates a signposter that uses the subsystem and category of an existing logger.
- [init(logHandle: OSLog)](./init%28loghandle%29.md)
  Creates a signposter that uses the subsystem and category of an existing log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/disabled)*