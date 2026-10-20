# numberOfSections

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of sections in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var numberOfSections: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger numberOfSections;
```

#### Discussion

[`UITableView`](../uitableview.md) gets the value in this property from its data source and caches it.

## See Also

### Getting the number of rows and sections
- [func numberOfRows(inSection: Int) -> Int](./numberofrows%28insection%29.md)
  Returns the number of rows (table cells) in a specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/numberofsections)*