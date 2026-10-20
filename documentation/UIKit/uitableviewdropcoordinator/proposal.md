# proposal

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The proposal for how to incorporate the dropped items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var proposal: UITableViewDropProposal { get }
```

```objc
@property (nonatomic, readonly) UITableViewDropProposal * proposal;
```

#### Discussion

If your drag delegate implements the [`tableView(_:dropSessionDidUpdate:withDestinationIndexPath:)`](../uitableviewdropdelegate/tableview%28_,dropsessiondidupdate,withdestinationindexpath%29.md) method, this object contains the information that you provided when making your drop proposal for the given location.

## See Also

### Getting the session information
- [var session: any UIDropSession](./session.md)
  The drop session containing information about the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator/proposal)*