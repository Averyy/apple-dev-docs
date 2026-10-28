# numberOfRows(inSection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of rows (table cells) in a specified section.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func numberOfRows(inSection section: Int) -> Int
```

```objc
- (NSInteger) numberOfRowsInSection:(NSInteger) section;
```

## Return Value

The number of rows in the section.

## Discussion

[`UITableView`](../uitableview.md) gets the value returned by this method from its data source and caches it.

## Parameters

- `section`: An index number that identifies a section of the table. Table views in a plain style have a section index of zero.

## See Also

### Getting the number of rows and sections
- [var numberOfSections: Int](./numberofsections.md)
  The number of sections in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/numberofrows(insection:))*