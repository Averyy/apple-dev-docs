# cellUpdateHandler

**Framework**: UIKit  
**Kind**: property

The block that updates the contents of the placeholder cell.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cellUpdateHandler: ((UITableViewCell) -> Void)? { get set }
```

#### Discussion

Specify a block that configures or updates the appearance of your placeholder cell. The table view calls this block when the placeholder cell becomes visible, and at other appropriate times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewplaceholder/cellupdatehandler)*