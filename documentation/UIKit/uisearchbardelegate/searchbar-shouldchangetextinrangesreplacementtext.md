# searchBar(_:shouldChangeTextInRanges:replacementText:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextInRanges ranges: [NSValue], replacementText: String) -> Bool
```

#### Return Value

Returns true if the text at the `ranges` should be replaced.

#### Discussion

Asks the delegate if the text at the specified `ranges` should be replaced with `text`.

If this method returns YES then the search bar will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementText` before deleting the text at the other ranges. If the delegate does not implement this method then the `searchBar:shouldChangeTextInRange:replacementText:` method will be called and passed the union range instead. If the delegate also does not implement that method then YES is assumed.

## Parameters

- `searchBar`: The search bar asking the delegate
- `ranges`: The ranges of the text that should be deleted before replacing
- `replacementText`: The replacement text


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextinranges:replacementtext:))*