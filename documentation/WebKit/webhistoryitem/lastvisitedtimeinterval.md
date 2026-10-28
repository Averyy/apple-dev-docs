# lastVisitedTimeInterval

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The last time and date the receiver’s page was visited.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var lastVisitedTimeInterval: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval lastVisitedTimeInterval;
```

## Discussion

The interval is from a reference date as determined by [`NSDate`](../../Foundation/nsdate.md).

## See Also

### Getting other attributes
- [var icon: NSImage!](./icon.md)
  The icon for the receiver’s page, or `nil` if none exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitem/lastvisitedtimeinterval)*